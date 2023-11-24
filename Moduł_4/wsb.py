from wsb_func import check_user_credential
user_dict = {
    'majki': '123',
    'Kamil': '124',
    'Kamil1': '234',
    'Kamil11': '765',
    'Kamil111': 'mama',
    'Kamil001': 'eee',
    'Rafcio': '876',
    'Betty': 'betty'
}


while True:
    user = input('Użytkownik: ')
    check_user_credential(user_dict, user)
    answer = input('Continue? [Y/N] ').lower()
    if answer != 'y':
       break
