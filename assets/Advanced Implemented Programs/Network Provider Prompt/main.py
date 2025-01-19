from prompt import get_user_info, log_in,sign_up

x, y = get_user_info()


print('1. Login 2. Signup')
choice = input('>>>')

if choice == '1':
    log_in(x, y)
elif choice == '2':
    sign_up(x,y)
else:
    print('Byeee')