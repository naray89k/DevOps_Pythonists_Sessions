import re

global_dict = {key: val for key, val in globals().items()}

# for elem in globals():
#     print(elem)

# collect the list of inbuilt exceptions/errors from python builtins
# print("===================================")
# print("LIST OF BUILT-IN EXCEPTIONS")
# exception_pattern = re.compile(r'exception|error|warning|\w+exit|notimplemented', re.I)
# for elem in dir(global_dict['__builtins__']):
#     if exception_pattern.search(elem):
#         print(elem)
# print("===================================")


# =================================================================================
# Exception Handling Concepts
# =================================================================================

def process_file(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as file_obj:
            for line in file_obj.readlines():
                print(line)
    except FileNotFoundError as fnfe:
        print(f"Exception found: {fnfe.__class__}")
        print(f"Error Message: {fnfe}")
        print()


def process_file_without_exception(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file_obj:
        for line in file_obj.readlines():
            print(line)


# Functions Without Exceptions
# def numerical_addition(*varargs):
#     result = 0
#     for arg in varargs:
#         result += arg
#     return result
#
# def numerical_multiplication(*varargs):
#     product = 1
#     for arg in varargs:
#         product *= arg
#     return product

# Functions With Exceptions (generic exceptions)
def numerical_addition(*varargs):
    try:
        result = 0
        for arg in varargs:
            result += arg
        return result
    except Exception as exp:
        print(exp.__class__)
        print(exp)
        print()


def string_addition(*varargs):
    try:
        result = ''
        for arg in varargs:
            result += arg
        return result
    except Exception as exp:
        print(exp.__class__)
        print(exp)
        print()


def numerical_multiplication(*varargs):
    product = 1
    for arg in varargs:
        product *= arg
    return product


def string_multiplication(*varargs):
    try:
        product = ''
        for arg in varargs:
            product *= arg
            print(product)
        return product
    except TypeError as te:
        print(te.__class__, te)
        print()
    except Exception as exp:
        print(exp.__class__)
        print(exp)
        print()


def capture_generic_exception(number):
    try:
        if number > 10:
            print("Number greater than 10")
    except TypeError as te:
        print(te.__class__)
        print(te)
        print()


if __name__ == '__main__':
    process_file("narayanan.txt")
    # process_file_without_exception("narayanan.txt")
    capture_generic_exception("text")

    full_name = string_addition('Narayanan ', 'Krishnan')
    full_name = string_addition(1, 'Krishnan')
    print('string_addition:', full_name)

    sum_of_numbers = numerical_addition(1, 2, 3, 4, 5, 6, 7, 8, 9, "txt")
    print('sum_of_numbers:', sum_of_numbers)

    product_of_numbers = numerical_multiplication(1, 2, 3, 4, 5)
    print('product_of_numbers:', product_of_numbers)

    string_product = string_multiplication('Narayanan', 2, 3)
    print('string_product:', string_product)

