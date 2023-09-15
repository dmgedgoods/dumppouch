hotelRate = 150
cutHigh = 67
cutLow = 63

print("Enter years married: ")
yearsMarried = int(input())
print("How many days to stay?")
stayDays = int(input())

if yearsMarried > cutLow and yearsMarried < cutHigh:
    print(f'{"You stay for 1/2 off!  $"}{int((stayDays * hotelRate) / 2)}')
else:
    print(f'{"Pay full price!  $"}{int(stayDays * hotelRate)}')

