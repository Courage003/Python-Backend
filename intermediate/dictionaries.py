#Dictionaries are used to store information in key value pairs

#Don't allow duplicate values

my_dict = {
    'name': 'Dhruv',
    'nationality': 'Indian',
    'age': 20,
    'qualification': 'College',
    'friends': ['Ankit', 'Soumyajit', 'Aditya']
}

print(my_dict)
print(my_dict['name'])

#Two keys with the same name are not allowed in dictionaries

print(len(my_dict))
print(my_dict['age'])
print(type(my_dict))


x= my_dict['name']
print(x)