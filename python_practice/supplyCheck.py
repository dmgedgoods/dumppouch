supplies = ['pens', 'paper', 'grenades', 'binders']
print('Enter a supply: ')
name = input()
if name not in supplies:
    print('That item is not in the catalog: ' + name)
else:
    print(name + ' is in the catalog')
