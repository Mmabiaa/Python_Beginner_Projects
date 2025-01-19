users = {}

def get_user_info():
    username = input('Username: ')
    password = input('Password: ')

    return username, password

def sign_up(username, password):
    if len(password) >= 8 and username:
        print('Signing up...')
        print('\n\n account successfully signed up')
    else:
        print('password must be at least 8 characters')
        get_user_info()
        sign_up(username, password)

    return users.update({username : password})

def log_in(username, password):

    if (username and password) in users.items():
        print('Logging in...')
        print('\n\n account successfully logged in')

    else:
        print('Please create an account and login')
        get_user_info()