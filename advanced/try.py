#error based method
try:
    x = int(input('Input an integer: '))
    print(x)
except ValueError: 
    print('Something went wrong...Please try again')

else:
    print('Nothing went wrong')

#else runs after successful completion
#finally runs in either of the cases

finally:
    print('try exceuted')                   