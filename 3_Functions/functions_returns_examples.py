# # Example: 1 (Function not implemented)
print("Example: 1 (Function not implemented)")


#
def add():
    pass


print(add())
#
# a = 3
# if a == 1:
#     pass
# else:
#     print("Do something")
# print("After pass effect")

# # Output:None
#
# # Example: 2 (Return statement not reached)
print("Example: 2 (Return statement not reached)")


def add(a, b):
    c = a + b
    if c > 10:
        return c


print(add(1, 2))

# # Output:None
#
#
# Example: 3 (No return statement)
print("Example: 3 (No return statement)")


def add(a, b):
    c = a + b


print(add(1, 2))
# # Output:None
#
# # The return type is a tuple
print("The return type is a tuple.")


def add(a, b):
    result = a + b
    return a, b, result


print(add(5, 10))
# # Output:(1,2,3)
#
#
# # The return statement having a single expression with a trailing comma returns a tuple.
print("The return statement having a single expression with a trailing comma returns a tuple.")


def add(a, b):
    result = a + b
    return result,


print(add(1, 2))
# # Output:(3,)
#
# # Returning multiple values using list displays
print("Returning multiple values using list displays")


def calc(a, b):
    sum = a + b
    dif = a - b
    mul = a * b
    div = a / b
    return [sum, dif, mul, div]


print(calc(5, 4))
# # Output:[9, 1, 20, 1.25]
#
# # Returning multiple values using dictionary displays
print("Returning multiple values using dictionary displays")


def calc(a, b):
    sum = a + b
    dif = a - b
    mul = a * b
    div = a / b
    return {"Addition": sum, "Subtraction": dif, "Multiplication": mul, "Division": div}


print(calc(5, 4))
# # Output:{'Addition': 9, 'Subtraction': 1, 'Multiplication': 20, 'Division': 1.25}
#
# # Returning multiple values using set displays
print("Returning multiple values using set displays")


def calc(a, b):
    sum = a + b
    dif = a - b
    mul = a * b
    div = a / b
    return {sum, dif, mul, div}


print(calc(5, 4))
# # Output:{9, 20, 1, 1.25}
#
# # Returning a single value from a function
print(" Returning a single value from a function")


def add(a, b):
    result = a + b
    return result


print(add(1, 2))
# # Output:3
#
print(add("Hello ", "Python"))
# # Output:Hello Python
#
print(add([1, 2], [3, 4]))
# # Output:[1, 2, 3, 4]
#
print(add((1, 2), (3, 4)))
#
# # Output:(1, 2, 3, 4)
#
# Multiple ‘return’ statements in a single function
print("Multiple ‘return’ statements in a single function")


def num(a):
    if a % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"


#
print(num(5))  # Output:Odd Number
print(num(30))  # Output:Even Number


#

# # ‘return’ vs. ‘print’ statements inside a function
# print("return vs print statements inside a function")
#
def add(a, b):
    r1 = a + b
    return r1


def sub(c, d):
    r2 = c - d
    return r2


# # We can assign the return value to a variable
r3 = add(3, 4)
print(r3)  # Output:7
# # We can pass the return value to another function also.
print(sub(r3, 5))  # Output:2
