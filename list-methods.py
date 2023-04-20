list1 = [2,3,6,1,4,5]
list2 = ['banana', 'apples', 'mango', 'mango', 'oranges']
list2.append('cherry')
list2.insert(1, 'strawberry')
list2.remove('banana')
list1.extend(list2)
print(list1)
print(list2.index('mango'))
print(list2.count('mango'))
list1.sort()
print(list1)
list2.reverse()
print(list2) 
#list2.clear()
print(list2)

#list3 = list2.copy()
#print(list3) 
list2.pop();
print(list2)


