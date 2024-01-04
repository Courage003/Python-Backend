#return statement is used to get a response from a task being executed in the function
def my_function():
    return 5+4

print(my_function())

def add_numbers(num1, num2):
    return num1 + num2

num1= int(input('Enter first number: '))
num2= int(input('Enter second number: '))
print(add_numbers(num1, num2))

#return terminates the function