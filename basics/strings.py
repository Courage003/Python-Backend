#Strings are just plain text
name = 'Dhruv'
print('Hi.\nHow are you?')
print(name)

#\ is used to break the line or to print the quotes as well
print('Hi.\'How are you?')
print(name[1])
print(name.upper())
print(name.lower())

#We can check for upper as well lower cases as well
print(name.islower())
print(name.isupper())

#adding on more functionalities
print(name.upper().isupper())  #returns True

#To get length of string
print(len(name))

#to get index number of any char
print(name.index('h'))

#to replace any char
print(name.replace('D', 'S')) #Shruv

