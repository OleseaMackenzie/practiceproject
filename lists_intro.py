
friends = []  # empty list
players = list()  # creates empty list

nums = [4, 10, 6]
names = ['john', 'marka', 'jane']
bool_values = [True, False, True]
print(nums)
print(names)
# add elements, remove, update, read through values (access each value)

print('Hi, ', names[1].title())
print('Hi, ', names[0].title())
print('Hi, ', names[-1].title())
print('Hi, ', names[-2].title())
print('Hi, ', names[-3])
# print('Hi, ', names[3].title()) # IndexError: list index out of range
print("##### adding the elements to the list ######")
# listname.append(newvalue) - adds newvalue to the end of the list
names.append("alex")
print(names)
# listname.insert(index, value) - puts the 'value' to the 'index',
# other values shifter to the left, all indexes will be updated
names.insert(2, "araz")
print(names)
print("# updating the last element of the list 'alex'->'benny'")
names[-1] = 'benny'
print(names)
print("removing the values from the list--------")
print("# remove element by index : del listname[index]. removing 'jane' ")
del names[3]
print(names)
print("# remove element by index : listname.pop() removing last in the list")
deleted_name = names.pop()  # returns the value to the program after deleting
print(names)
names.pop(0)
print(names)
print('we deleted following names: ', deleted_name)
print("# remove element by value: listname.remove(value) ")
names.remove('araz')  # ValueError: list.remove(x): x not in list
print(names)


