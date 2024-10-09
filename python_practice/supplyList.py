supplies = []

while True:
    print('Enter supply item ' + str(len(supplies) + 1) + ' (or enter nothing to end list)')
    name = input()
    if name == '':
        break
    supplies = supplies + [name]
print('Supplies are: ')
for name in supplies:
    print(' -' + name)
print('\n')
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
