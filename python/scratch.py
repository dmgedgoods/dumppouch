#name = 'Mary'
#password = 'swordfish'
name = input()
password = input()

if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access Granted')
    else:
        print('Wrong password')
