# main.py
import sys

print(f'-----------------------------------------------------------')

print(f'-------- Running main.py - module name: {__name__} --------')

import module1

print(module1)

module1.pprint_dict('main.globals', globals())

print(sys.path)

print(f'---------------------- End of main.py ------------------')
