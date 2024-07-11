import random

#cat = ['fat', 'gray', 'angry']
#size = cat[0]
#color = cat[1]
#disposition = cat[2]

cat = ['fat', 'gray', 'angry']
size, color, disposition = cat
print(f'My cat is {size}, {color} and {disposition}.')

for index, item in enumerate(cat):
    print(f'Index {index} in supplies is: {item}')

print(random.choice(cat))
