# Building a Simple Login and Signup system

print('Create Account')
username = input('Enter username: ')
password = input('Enter password: ')

print('Your account has been created successfully')
print('Login now')

username2 = input('Enter username: ')
password2 = input('Enter password: ')

if username == username2 and password == password2:
    print('Logged In successfully')

else:
    print('Invalid Credentials')    
