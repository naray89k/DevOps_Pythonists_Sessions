# =============================================================================================
# The list is a data structure in Python which contains a mutable, ordered sequence of elements.
# =============================================================================================

# Creating a list:
l1 = [1, 2, 3]
l2 = ['apple', 'banana', 'orange', 'grapes', 'mango']

# =============================================================================================
# LIST CONSTRUCTOR:
# list()
# List constructor takes sequence types and converts to list.It is used to convert tuple to list.
# =============================================================================================
t1 = (1, 2, 3)
l1 = list(t1)
print(l1)
# Output:
# [1, 2, 3]

# =============================================================================================
# ACCESSING ELEMENTS FROM LIST:
# List indices start from 0.
# =============================================================================================
# l1[0] -> 1 (first element in list l1)
# l2[2] -> orange (third element in list l2)
# l1[-1] -> 3 (Negative index -1 means starting from the end of the list)
# l1[-2] -> 2


# =============================================================================================
# LIST SLICING:
# We can specify range of indexes. start and stop. stop index is not included.
# =============================================================================================
l1 = [0, 1, 2, 3, 4, 5]
print(l1[1:4])
# Output:
[1, 2, 3]
# =============================================================================================

# =============================================================================================
# UPDATING LIST:
# Inserting elements into the list. insert method will insert elements into the list at a specified index.
l1 = [1, 2, 3]

# It will insert element 4 at index 3.
l1.insert(3, 4)
print(l1)

# It will update the element in the second index to ‘a’
l1[2] = 'a'
print(l1)
# Output:
# [1, 2, 3, 4]
# [1, 2, ‘a’, 4]

# =============================================================================================
# UPDATING NESTED LIST:
l1 = [1, 2, 3, [4, 5]]
l1[3][0] = 'a'
print(l1)
# Output:
# [1, 2, 3, ['a', 5]]
# =============================================================================================

# =============================================================================================
# ADDING ITEMS TO THE LIST:
# 1.append
# 2.extend

# append
# --------
# It will append the argument as a single item to the end of the list.
# The length of the list will be increased by 1.
a1 = [1, 2, 3]
a2 = [4, 5]
a1.append(a2)
print(a1)
# Output:
# [1, 2, 3, [4,5]]

b1 = [4, 5, 6]
b1.append(7)
print(b1)
# Output:
# [4, 5, 6, 7]

# Notes: append method will modify the original list

# EXTEND
# --------
# It will iterate through the argument and add each element to the list.
c1 = [1, 2, 3]
c2 = [4, 5, 6]
c1.extend(c2)
print(c1)
# Output:
# [1, 2, 3, 4, 5, 6]

# =============================================================================================


# =============================================================================================
# Removing Items from the list
# del
# pop()
# remove()
# clear()

# clear()
# clear method will empty the list. It will return an empty list.
a1 = [1, 2, 3]
a1.clear()
print(a1)
# Output:
# []

# del
# del keyword delete the list itself.
a1 = [1, 2, 3]
del a1
print(a1)
# Output:
# NameError: name ‘a1’ is not defined.

# remove()
# remove method will remove the element specified from the list.
a1 = [1, 2, 3]
a1.remove(1)
print(a1)
# Output:
# [2,3]
# If the element mentioned is not in the list, it will raise ValueError.

# pop()
# pop method will remove the item in the specified index from the list. If the index not specified, it will remove the last item from the list.

a1 = [1, 2, 3]
a1.pop(1)
print(a1)
# Output:
# [1,3]
a1.pop()
print(a1)
# Output:
# [1]
a1.pop(4)
print(a1[4])
# Output:
# IndexError: pop index out of range
# =============================================================================================


# Joining two lists:
a1 = [1, 2, 3]
a2 = [4, 5, 6]
a3 = a1 + a2
print(a3)
# Output:
# [1,2,3,4,5,6]


# =============================================================================================
# count:
# count will return the number of occurrences of a particular element mentioned.

a1 = [1, 2, 3, 4, 1, 5, 6, 1]
print(a1.count(1))
# Output:
# 3

# =============================================================================================
# Sort:
# sort method will sort the original list.
# Sorting in ascending order using sort function:
a1 = [2, 4, 6, 8, 0, 7, 5, 3, 1]
a1.sort()
print(a1)
# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Sorting in descending order using the sort method.

a2 = [2, 4, 6, 8, 0, 7, 5, 3, 1]
a2.sort(reverse=True)
print(a2)
# Output:
# [8, 7, 6, 5, 4, 3, 2, 1, 0]


# =============================================================================================
# reverse
# The reverse method is used to reverse the list. It will reverse the original list.
l1 = [1, 3, 5, 2, 4, 6, 8]
l1.reverse()
print(l1)
# Output:
# [8, 6, 4, 2, 5, 3, 1]

# =============================================================================================
# List functions:
# sorted()
# It will sort the list and return a new list. It won’t modify the original list.
# Sorting in ascending order using the sorted function:
a1 = [2, 4, 6, 8, 0, 7, 5, 3, 1]
a2 = sorted(a1)
print(f"Original List:{a1}")
print(f"Sorted List:{a2}")
# Output:
# Original List:[2, 4, 6, 8, 0, 7, 5, 3, 1]
# Sorted List:[0, 1, 2, 3, 4, 5, 6, 7, 8]

# Sorting in descending order using the sorted function:
a1 = [2, 4, 6, 8, 0, 7, 5, 3, 1]
a2 = sorted(a1, reverse=True)
print(f"Original List:{a1}")
print(f"Sorted List:{a2}")
# Output:
# Original List:[2, 4, 6, 8, 0, 7, 5, 3, 1]
# Sorted List:[8, 7, 6, 5, 4, 3, 2, 1, 0]

# =============================================================================================
# Reversed()
# The reversed function will reverse the elements in the list.
# It will return an iterator object.
# We can iterate through the iterator object or convert it to a list using a list().
a1 = [1, 3, 5, 2, 4, 6]
a2 = reversed(a1)
print(a2)
print(list(a2))
# Output:
# <list_reverseiterator object at 0x02817808>
# [6, 4, 2, 5, 3, 1]

# =============================================================================================
# min, max, sum,len
# min — returns the minimum number in the list
# max- return the maximum number in the list
# sum — return the sum of the numbers in the list
# len — return the number of elements in the list
a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(a1))
print(max(a1))
print(sum(a1))
print(len(a1))
# Output:
# 1
# 10
# 55
# 10
s1 = ['apple', 'banana', 'orange', 'grapes']
print(min(s1))
print(max(s1))
print(len(s1))
print(sum(s1))
# Output:
# apple
# orange
# 4
# TypeError: unsupported operand type(s) for +: ‘int’ and ‘str’

# =============================================================================================
# Check if an item exists in the list.
s1 = ['apple', 'banana', 'orange', 'grapes']
if 'apple' in s1:
    print("YES")
if 'grapes' not in s1:
    print("Grapes is not in the list ")
# Output:
# YES


# =============================================================================================
# copy,deepcopy
# copy function will return a copy of the list.
# Modifications done in the original list will not be reflected in the copied list.
# But modifications done in the nested list will be reflected in the copied list.
# deep copy function will return a deep copy of the list.
# Modifications done in the original list will not be reflected in the deep copied list.

import copy

l1 = [1, 2, 3, [4, 5]]
l2 = l1.copy()
print("Copied : {}".format(l2))
l3 = copy.deepcopy(l1)
print("Deep Copied: {}".format(l3))
l1[0] = 'a'
print("After updating elements in the list")
print(f"Original List:{l1}")
print(f"Copied List:{l2}")
print(f"Deep Copied List:{l3}")
l1[3][1] = 'b'
print("After updating elements in the nested list")
print(f"Original List:{l1}")
print(f"Copied List:{l2}")
print(f"Deep Copied List:{l3}")
# Output:
# Copied : [1, 2, 3, [4, 5]]
# Deep Copied: [1, 2, 3, [4, 5]]
# After updating elements in the list
# Original List:[‘a’, 2, 3, [4, 5]]
# Copied List:[1, 2, 3, [4, 5]]
# Deep Copied List:[1, 2, 3, [4, 5]]
# After updating elements in the nested list
# Original List:[‘a’, 2, 3, [4, ‘b’]]
# Copied List:[1, 2, 3, [4, ‘b’]]
# Deep Copied List:[1, 2, 3, [4, 5]]

# =============================================================================================
# Assignment Operator:
# Copy using assignment operator.

l1 = [1, 2, 3]
l2 = l1
print(l1)
print(l2)
l1[0] = 'a'
l2[1] = 'b'
print("After modifying both list l1 and l2")
print(l1)
print(l2)
# Output:
# [1, 2, 3]
# [1, 2, 3]
# After
# modifying
# both
# list
# l1 and l2
# [‘a’, ‘b’, 3]
# [‘a’, ‘b’, 3]

# In the above example, both l1 and l2 will be referring to the same object in the memory.
# So changes made in one list will be reflected in the other list too.

# CONCLUSION:
# 1. List methods which will update the original list append,extend,remove,clear,pop,insert,sort,reverse
# 2. List function which will return a new list and won’t modify the original list.
# sorted() , reversed(),copy(),deepcopy()
