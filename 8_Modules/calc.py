print("Running from calc.py")

def addition(*varargs):
    result = 0
    for arg in varargs:
        result += arg
    return result

def multiplication(*varargs):
    product = 1
    for arg in varargs:
        product *= arg
    return product

if __name__ == '__main__':
    print("This code block is imported")
    dict1 = {
        'name': 'Narayanan',
        'Salary': 600000
    }
