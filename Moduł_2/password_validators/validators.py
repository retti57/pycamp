"""This script consists of classes HashedPassword, PasswordValidator for PassValid.py"""
from abc import ABC, abstractmethod
from hashlib import sha1
from requests import get


class ValidationError(Exception):
    """ Interface of Validation Error class """


class Validator(ABC):
    """ Abstract class of Validator class """

    def __init__(self, to_check: str):
        self.password_to_validation = to_check

    @abstractmethod
    def is_valid(self):
        """ This is name of method to inherit """


class PasswordValidator(Validator):
    """ This class iterates through Validators """

    def is_valid(self) -> bool:
        """ Returns boolean information if all password validators met their requirements for given password """
        validators = [
            LengthValidator,
            NumbersValidator,
            SpecialCharacterValidator,
            UpperLetterValidator,
            LowerLetterValidator,
            HaveIBeenPWNDValidator
        ]

        return all([validator(self.password_to_validation).is_valid() for validator in validators])


class LengthValidator(Validator, ):
    """This Validator checks length of given password"""

    def is_valid(self, desired_length: int = 8) -> bool:
        """Returns boolean information if validator met their requirements"""
        if len(self.password_to_validation) >= desired_length:
            return True

        raise ValidationError(f'Text must have at least {desired_length} characters')


class NumbersValidator(Validator):
    """This Validator checks if numbers exists in given password"""

    def is_valid(self) -> bool:
        """Returns boolean information if validator met their requirements"""
        if any([x.isdigit() for x in self.password_to_validation]):
            return True

        raise ValidationError('Text must contain numbers')


class SpecialCharacterValidator(Validator):
    """This Validator checks if special characters exists in given password"""

    def is_valid(self) -> bool:
        """Returns boolean information if validator met their requirements"""
        if any([x for x in self.password_to_validation if x in '!@#$%^&*()']):
            return True

        raise ValidationError('Text must contain special characters')


class UpperLetterValidator(Validator):
    """This Validator checks if upper letters exists in given password"""

    def is_valid(self) -> bool:
        """Returns boolean information if validator met their requirements"""
        if any([x.isupper() for x in self.password_to_validation]):
            return True

        raise ValidationError('Text must contain UPPERCASE letter')


class LowerLetterValidator(Validator):
    """This Validator checks if lower letters  exists in given password"""

    def is_valid(self) -> bool:
        """Returns boolean information if validator met their requirements"""
        if any([x.islower() for x in self.password_to_validation]):
            return True

        raise ValidationError('Text must contain lowercase letter')


class HaveIBeenPWNDValidator(Validator):
    """ This Validator checks if password has leaked """

    def is_valid(self):
        """Returns boolean information if given password was registered on HaveIBeenPWND databases"""
        pass_hash = sha1(self.password_to_validation.encode('utf8')).hexdigest().upper()

        api_url = 'https://api.pwnedpasswords.com/range/' + pass_hash[:5]
        response = get(api_url)
        for line in response.text.splitlines():
            found_hash, _ = line.split(':')
            if found_hash == pass_hash[5:]:
                raise ValidationError('This password has leaked. Try another one!')
        return True
