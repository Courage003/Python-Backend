
list2 = ['banana', 'apples', 'mango', 'oranges']
#list1.extend(list2)
#print(list1)

#joining two lists

#pushing into list
list2.append('papaya')
print(list2)
print(len(list2))

#pushing at specific index
list2.insert(1, 'cherry')
print(list2)

#popping from list
list2.remove('banana')
print(list2)

#deleting everything from list
#list2.clear()
print(list2)

#print particular index value
print(list2.index('mango'))

#frequency of any value
print(list2.count('mango'))

#sorting the list

list1= [2, 7, 8, 1]

list1.sort()
print(list1)

#printing list in reverse order
list2.reverse()
print(list2)

#duplicate a list
list3 = list2.copy()
print(list3)


#deleting last value from list
list2.pop()
list2.pop(1)
print(list2)

del list2[0]
print(list2)


