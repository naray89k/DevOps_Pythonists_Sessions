# GLOBAL VARIABLES:

list1 = [0, 1, 2, 3, 4]
list2 = ["one", "two", "last"]

# all()  ——> returns True when all the elements of an iterable object satisfies Truthiness
if all(list1):
    print("Inside all Loop")
else:
    print("There is one or more False element in the sequence")

# list1 = ['', None, [], 1]
if any(list1):
    print("Inside any Loop")
else:
    print("There is one or more False element in the sequence")

# dir() ——> Returns all attributes associated with an object.
# for elem in dir(list1):
#     print(elem)


# callable() ——> returns True when passed on object is callable.
print('list1.remove--->', callable(list1.remove))
print('list1--->', callable(list1))

# enumerate() ——> Returns index position and element in that position of Iterable Object
list2 = ["one", "two", "last"]
print(enumerate(list2))

for index, value in enumerate(list2):
    print(index, value)

# def func():
#    list2 = list(range(1, 11))
#    print(list2)

# func()
# print(list2)

# help() ——> Returns Help content of a function, which has doc_string in it.
print(help(print))

print(id(list1))


# ===============================
#  MAP

def square(num):
    return num * num


sum_of_numbers = list(map(square, range(1, 11)))
print(sum_of_numbers)



#[1 --> 10]