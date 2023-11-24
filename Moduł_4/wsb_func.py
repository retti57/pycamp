def create_user(db, usr_name):
    user_password = input('Hasło: ')
    confirm_password = input('Potwierdź hasło: ')
    if user_password == confirm_password:

        return (usr_name, user_password)
    else:
        return None

def check_user(db, usr):
    if usr in db.keys():
        user_password = input('Hasło: ')
        if user_password == db[usr]:
            return 'Logged in'
        else:
            return 'Incorrect password'
    else:
        return 'Not found'

def check_user_credential(db, usr):
    match check_user(db, usr):
        case 'Logged in':
            print('Logged In')
        case 'Incorrect password':
            print('Incorrect password')
        case 'Not found':
            question = input('Create user? [Y/N] ')
            if question in ['Y','y']:
                new_user_name, new_user_password = create_user(db, usr)
                db[new_user_name] = new_user_password
                print('created')

