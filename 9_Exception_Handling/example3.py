# EXAMPLE WITH TRY CATCH BLOCK

def division(dividend, divisor):
    return dividend / divisor


def division(dividend, divisor):
    print(f'executing division function')
    try:
        return dividend / divisor
    except ValueError as ve:
        print("Exception Message:", ve)
    except ZeroDivisionError as zde:
        print("Exception Message:", zde)
    except Exception as exp:
        print(exp.__class__, "Error Message:", exp)
    finally:
        print("Executing finally block")
        print()


# ======
# MAIN
# ======
# Main Execution starts here ....
# value3 = None
try:
    value1 = division(200, 100)
    value2 = division("200", 100)
    value3 = division(200)
except Exception as exp:
    print(exp.__class__)
    print(exp)
finally:
    print("Print Values:")
    print(value1, value2, value3)
