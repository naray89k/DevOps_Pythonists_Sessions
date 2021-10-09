import re


# EXAMPLE WITH TRY CATCH BLOCK

def full_name(first_name, second_name):
    if not re.search(r'^[a-z]+$', first_name, re.I):
        raise NameError(f"{first_name} is not in expected format")
    if not re.search(r'^[a-z]+$', second_name, re.I):
        raise NameError(f"{second_name} is not in expected format")
    return f"{first_name.strip()} {second_name.strip()}"


# ======
# MAIN
# ======
# Main Execution starts here ....
name = None
try:
    # name = full_name("Narayanan K", "Krishnan")
    name = full_name("Narayanan", "Krishnan")
except Exception as exp:
    print(exp.__class__)
    print(exp)
finally:
    print("Print Values:")
    print(f"Name:{name}")

