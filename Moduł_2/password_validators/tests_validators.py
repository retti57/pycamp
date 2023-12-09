""" Tests for classes from validators.py """
import pytest
from validators import (PasswordValidator,
                        LengthValidator,
                        NumbersValidator,
                        SpecialCharacterValidator,
                        UpperLetterValidator,
                        LowerLetterValidator,
                        HaveIBeenPWNDValidator,
                        ValidationError)

pass0 = '123456'
pass1 = 'ZAQ!2wsxCDE#'
pass2 = 'ZAQ!wsxCDE#'
pass3 = 'ZAQ2wsxCDE'
pass4 = 'ZAQ!ws'


def test_have_i_been_pwnd_vaildator_by_mocking_negative(requests_mock):
    """test if password has been leaked ( without connection to api ) to check functionality"""
    # pass0: '123456789'
    # pass0_hash: 'F7C3BC1D808E04732ADF679965CCC34CA7AE3441'
    data = "C1D808E04732ADF679965CCC34CA7AE3441:15\r\n0E90BD707CE709E96F2A3346CF26510260C:138"
    requests_mock.get('https://api.pwnedpasswords.com/range/F7C3B', text=data)
    validator = HaveIBeenPWNDValidator('123456789')
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'This password has leaked. Try another one!' in str(error.value)


def test_have_i_been_pwnd_validator_by_mocking_positive(requests_mock):
    """test if password has NOT been leaked ( without connection to api ) to check functionality"""
    # pass0: '123456789'
    # pass0_hash: 'F7C3BC1D808E04732ADF679965CCC34CA7AE3441'
    validator = HaveIBeenPWNDValidator('123456789')

    data = "C2D808E04732ADF679965CCC34CA7AE3441:15\r\n0E90BD707CE709E96F2A3346CF26510260C:138"
    requests_mock.get('https://api.pwnedpasswords.com/range/F7C3B', text=data)
    validator.is_valid()
    assert validator.is_valid() is True


def test_length_validator_positive():
    validator = LengthValidator(pass1)
    assert validator.is_valid() is True


def test_length_validator_negative():
    """test of length validator class / negative case"""
    validator = LengthValidator(pass4)
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must have at least 8 characters' in str(error.value)

    validator = LengthValidator(pass3)
    with pytest.raises(ValidationError) as error:
        validator.is_valid(12)
        assert 'Text must have at least 12 characters' in str(error.value)


def test_numbers_validator_positive():
    """test of numbers validator class / positive case"""
    assert NumbersValidator(pass3).is_valid() is True


def test_numbers_validator_negative():
    """test of numbers validator class / negative case"""
    validator = NumbersValidator(pass2)
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain numbers' in str(error.value)


def test_spec_char_validator_positive():
    """test of spec_char validator class / positive case"""
    assert SpecialCharacterValidator(pass2).is_valid() is True


def test_spec_char_validator_negative():
    """test of spec_char validator class / negative case"""
    validator = SpecialCharacterValidator(pass3)
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain special characters' in str(error.value)


def test_upper_validator_positive():
    """test of upper letter validator class / positive case"""
    assert UpperLetterValidator(pass3).is_valid() is True


def test_upper_validator_negative():
    """test of upper letter validator class / negative case"""
    validator = UpperLetterValidator(pass2.lower())
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain UPPERCASE letter' in str(error.value)


def test_lower_validator_positive():
    """test of lower letter validator class / positive case"""
    assert LowerLetterValidator(pass2.lower()).is_valid() is True


def test_lower_validator_negative():
    """test of lower letter validator class / negative case"""
    validator = LowerLetterValidator(pass3.upper())
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain lowercase letter' in str(error.value)


def test_password_validator():
    """test of PasswordValidator with different inputs"""
    validator = PasswordValidator('Marokok1')

    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain special characters' in str(error.value)

    # with connection
    validator = PasswordValidator('!@#123qweASD')
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'This password has leaked. Try another one!' in str(error.value)
