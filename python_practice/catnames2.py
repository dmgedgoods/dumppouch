myPets = ['fluffy', 'princess', 'precious', 'satan']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('Sorry I do not have a pet with that name.')
else:
    print(name + ' is my pet.')
