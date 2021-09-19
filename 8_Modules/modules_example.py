import sys
#from calc import multiplication, addition
import calc


# GLOBAL VARIABLE
a = 10


def func():
    global a
    a = 50
    b = 20
    print(f"Inside {__name__}")
    print(type(locals()))
    print(locals())
    print(globals())
    return 10


# for elem in sys.modules:
#    print(elem)

# GLOBALS
print("GLOBALS")
print(type(globals()))
print(globals())
print('--------')

# LOCALS
# print("LOCALS")
# func()
# print('-------')

# for key, value in sys.__dict__.items():
#     print(f'key:{key}', f'value:{value}')
# print('Current File and Module')
# print(globals()['__name__'])
# print(globals()['__file__'])
# print('-------')
# print()

# BUILT_INS
# print("Built-Ins")
# print('---------')
# for elem in dir(globals()['__builtins__']):
#     print(elem)
# print('---------')
# print()

# SYS MODULES
# print("SYS MODULES")
# print('---------')
# for elem in sys.modules:
#     print(elem)


print(sys.prefix)
print(sys.exec_prefix)
print(sys.path)

#print(addition(1, 2, 3, 4, 5))
#print(multiplication(1, 2, 3, 4, 5))
#print(calc.dict1)
print(calc.__dict__)
print(calc.__name__)
print(__name__)
