# FUNCTION WITHOUT ARGUMENTS:
def my_func():
    print("Function without argument")
    print("Say Hello!")


my_func()


# my_func(1) ----> not right

# FUNCTION WITH ARGUMENTS:
def custom_range(start, end, step):
    num = start
    while num <= end:
        print(num)
        num += step


# custom_range(0, 100, 3)
# custom_range(0, 300, 15)
# custom_range() ----> not right


def func_with_varargs(*arguments):
    print("Arguments Passed")
    for arg in arguments:
        print(arg)


func_with_varargs(1, 2, 3)
func_with_varargs("One", "Three", "Two", "Four")
func_with_varargs([1, 2, 3])


def func_with_keyvalue_pairs(start=0, end=100, step=1):
    num = start
    while num <= end:
        print(num)
        num += step

# func_with_keyvalue_pairs(0)
# func_with_keyvalue_pairs(50, 60)
# func_with_keyvalue_pairs(step=3, start=0, end=30)

def func_with_var_keyvalue_pairs(**keyarguments):
    print("Arguments Passed")
    for key, value in keyarguments.items():
        print(key, value)


func_with_var_keyvalue_pairs(step=3, start=0, end=30)
# func_with_var_keyvalue_pairs(3, 0, 30) ----> not right


def func_with_varargs_varkwargs(*args, **kwargs):
    print("Positional Arguments Passed")
    for arg in args:
        print(arg)

    print("Keyword Arguments Passed")
    for key, value in kwargs.items():
        print(key, value)


func_with_varargs_varkwargs(3, 30, start=0)

