#if statement generally gives up the condition
#i write a number
#the number is divisible by 2
#    the number is an even number
#not divisible by 2
#    the number is an odd number

a = 16
b = 16

if a>b:
    print(str(a) + ' is greater than '+ str(b))

elif a==b:
    print(str(a) + ' is equal to ' + str(b))    

else:
    print(str(b) + ' is greater than '+ str(a)) 


#Python automatically inputs everything as string    



#Simple program
value = input('Enter value: ')

if type(value)==str:
    print(value + ' is a string')

elif type(value)==int:
    print(value + ' is an integer')

elif type(value)==list:
    print(value + ' is a list')

else:
    print('We don\'t know the data type of ' + value)




#Program for checking even number

num = int(input('Enter a number: '))

if num%2 == 0:
    print('Even number')
else:
    print('Odd number')
    
        