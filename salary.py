print ('Salary Computation')
print ('---------------------')

input1 = int(input('Enter working hour: '))
input2 = int(input('Enter rate per hour: '))

if input1>40 :
    print ('You get500 bonus' + str((input1*input2)+500))
else :
    print ('Thankyou for the hardwork!' + str(input1*input2)) 

