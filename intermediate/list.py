#basically a list of different attributes of different values fixed into a value

countries = ['USA', 'India', 'UK', 'Australia', 'Ghana']
print(countries)
print(countries[0])
print(countries[0][1]) #S

#print from particular index of array
print(countries[1:]) 
#except USA


#print from one index to other
print(countries[1:3])

name= 'dhruv'
print(type(name))

print(type(countries))

#replace USA with Russia
countries[0]='Russia'
print(countries)

#accessing list from end
print(countries[-1])

#from beginning: 0
#from end: -1

print(len(countries))

#diffrent data types can be added into one list

lis1= ['USA', 2, True, 'Dhruv']
print(type(lis1(1)))

#list constructor

name= list(('Dhruv', 182, True))


