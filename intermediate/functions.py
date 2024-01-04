#A bunch of code that performs a particular task
def greetings_function(name, age):
    print('Welcome ' + name+ '. You are '+str(age)+' years old.')

greetings_function('Dhruv',20)    
#greetings_function(name = 'Dhruv', age = 20)

#passing various amounts of arguments
def greetings_function(*names):
    print('Welcome ' + names[1])

greetings_function('Dhruv', 'Harsh', 'Daisy') 

#input values
def greetings1_function(name, age):
    print('Welcome ' + name+ '. You are '+str(age)+' years old.')

name=input('Enter your name: ')
age=input('Enter your age: ')
greetings1_function(name,age) 
