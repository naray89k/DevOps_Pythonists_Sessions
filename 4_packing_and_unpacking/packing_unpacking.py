# PACKING

# # tuple packing
# ================================================

emp_info = 'Python', 5, 'Developer'
print(emp_info)

# Output:('Python', 5, 'Developer')
print(type(emp_info))
# # Output:<class 'tuple'>
#
#
# # tuple unpacking
# ================================================
#
skill, exp, role = emp_info
print(skill)  # Output:Python
print(exp)  # Output:5
print(role)  # Output:Developer
#
# # Unpacking the elements of one Python list
# ================================================
#
emp_info = ['Python', 5, 'Developer']
#
# # List unpacking
# ================================================
skill, exp, role = emp_info
print(skill)  # Output:Python
print(exp)  # Output:5
print(role)  # Output:Developer
#
# # Unpacking two Python lists to a single tuple/list
# ================================================
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
num = *even, *odd
print(num)
# # Output:(2, 4, 6, 8, 1, 3, 5, 7, 9)
#
# # unpacking range object
# ================================================

a, b = range(0, 2)
print(a)  # Output :0
print(b)  # Output: 1

# # Extended unpacking (tuples)
# ================================================

num = [1, 2, 3, 4, 5]

# # unpacking only first and second element. Remaining all elements to be captured in a list
a, b, *c = num
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: [3,4,5]

#
# # Extended unpacking (lists)
# ================================================

num = [1, 2, 3, 4, 5]

# # unpacking only first and second element. Remaining all elements to be captured in a list
a, b, *c = num
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: [3,4,5]

#
# # unpacking first and rest of elements
# ================================================

num = (1, 2, 3, 4, 5)

first, *rest = num
print(first)  # Output: 1
print(rest)  # Output: [2,3,4,5]

# # unpacking first,middle,last elements
# ================================================

num = (1, 2, 3, 4, 5)
first, *middle, last = num
print(first)
# # Output: 1
print(middle)
# # Output: [2,3,4]
print(last)
# # Output: 5


# # ignoring value "green" while tuple unpacking
# ================================================

t = ("red", "green", "blue")
t1, _, t2 = t
print(t1)  # Output:red
print(t2)  # Output:blue

# # Ignoring multiple values in tuple unpacking
# ================================================

num = [1, 2, 3, 4, 5, 6]
# # Ignoring all values except first and last element in tuple.
t1, *_, t2 = num
print(t1)  # Output: 1
print(t2)  # Output: 6
