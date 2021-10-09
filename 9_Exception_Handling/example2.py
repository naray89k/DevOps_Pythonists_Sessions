
# EXAMPLE WITH TRY CATCH BLOCK

def division(dividend, divisor):
    return dividend/divisor


def division(dividend, divisor):
    try:
        return dividend / divisor
    except ValueError as ve:
        print("Exception Message:", ve)
    except ZeroDivisionError as zde:
        print(zde.__class__, "Exception Message:", zde)
    except Exception as exp:
        print(exp.__class__)
        print(exp)


# Main Execution starts here ....
value1 = division(200, 100)
print("Print Values:")
print("value1", value1)
print()

value2 = division("200", "100")
print("Print Values:")
print("value2", value2)
print()

value3 = division(200, 0)
print("Print Values:")
print("value3", value3)
print()


value4 = division(200)
print("Print Values:")
print("value4", value4)
print()

