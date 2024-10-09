#def printPicnic(itemsDict, leftWidth, rightWidth):
#    print('PICNIC ITEMS:'.center(leftWidth + rightWidth, '-'))
#    for k, v in itemsDict.item():
#        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
#picnicItems = {'sandwiches': 3, 'drinks': 4, 'cookies': 600}
#print(picnicItems, 12, 5)
#print(picnicItems, 20, 6)
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 9000}

printPicnic(picnicItems, 20, 6)
