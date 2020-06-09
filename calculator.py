print ('CALCULATOR')
print ('--------------')

print ('1=tambah\n2=kurang\n3= kali\n4=bagi')
operation = (input('Please type in the math operation you would like to complete: '))

number_1 = float(input('Enter your first number: '))
number_2 = float(input('Enter your second number: '))

if operation == 1:
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == 2:
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == 3:
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == 4:
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('not valid')