print('simple calculator with all the standard items')

num_1 = int(input('Input the first number: '))
num_2 = int(input('Input the second number:'))
function_statment_1 = 'Enter the operation you want to perform on the numbers'
function_statment_2 = '.All in small letters: '
print('multiply, divide, add, subtract (Commands)')
function = input(function_statment_1 + function_statment_2)

if function == 'multiply':
    print('Your multiplied answer is: ' + str(num_1 * num_2))
else:
    print('')
if function == 'divide':
    print('Your divided answer is: ' + str(num_1 / num_2)) 
else:
    print('') 
if function == 'add':
    print('Your added answer is: ' + str(num_1 + num_2))   
else:
    print('')
if function == 'subtract':
    print('Your subtracted answer is: ' + str(num_1 - num_2))   
else:
    print('')  

print('For Errors report a issuses in the repo (https://github.com/ranger-code/python-calculator)')    