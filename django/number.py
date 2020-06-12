# number = int(input('enter the value'))
# if number>0:
#      print('positive')
# elif number<0:
#      print('negative')
# else:
#      print('non-negative')

a = int(input('enter the value'))
b = int(input('enter the value'))
c = int(input('enter the value'))
if a>b and a>c:
    largest = a
elif b>a and b>c:
    largest = b
else:
    largest = c
print("The largest number is",largest)
