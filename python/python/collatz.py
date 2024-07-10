import sys, os

clear = lambda: os.system('clear')
clear()

def collatz():
    number = int(input('Please enter a number: '))
    try:
        while number != 1:
            if number % 2 == 0:
                number = number // 2
            else:
                number = 3 * number + 1
            print(number)
    except KeyboardInterrupt:
        print('User exited')
        sys.exit()
        
collatz()
