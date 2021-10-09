
# EXAMPLE WITH TRY CATCH BLOCK

# def regular_str_to_int(str_arg):
#     return int(str_arg)


def str_to_int(str_arg):
    try:
        return int(str_arg)
    except ValueError as ve:
        print("Exception Message:", ve)


# Main Execution starts here ....
# value = regular_str_to_int("Narayanan")
value1 = str_to_int("Narayanan")
value2 = str_to_int("100")

print("Print Values:")
print(value1, value2)
