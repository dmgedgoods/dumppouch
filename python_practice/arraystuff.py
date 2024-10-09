catNames = [] # empty array

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + # the array is empty (0), so we add one to get the index
          ' (or enter nothing to stop)') 
    name = input()
    if name == '': # if name is blank, move to the next instruction
        break
    catNames = catNames + [name] # list concatenation
print('Cat names are: ')
for name in catNames:
    print(' ' + name)

