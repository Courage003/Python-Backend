#Basic Calculator

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter operator: ')

if op == '+':
    print(num1 + num2)

elif op == '-':
    print(num1 - num2)

elif op == '*':
    print(num1 * num2)

elif op == '/':
    print(abs(num1 / num2))        

else: 
    print('Invalid operator')
    
        