import re

nums = [1, 2, 3, 4, 5]
country_capital = {"India": "Delhi",
                   "USA": "Washington",
                   "UK": "London",
                   "Germany": "Berlin"}
countries = {"India", "USA", "UK", "Germany"}
environments = ('DEV', 'TEST', 'UAT', 'PROD')
env = "DEV"

# # LIST METHODS
# # ============
print("LIST METHODS:")
print("-------------")
for elem in dir(nums):
    if not re.search(r'^__.*__$', elem, re.I):
        print(elem)
print()


# # DICT METHODS
# # ============
# print()
# print("DICTIONARY METHODS:")
# print("-------------------")
# for elem in dir(country_capital):
#     if not re.search(r'^__.*__$', elem, re.I):
#         print(elem)
# print()


# # SET METHODS
# # ============
# print()
# print("SET METHODS:")
# print("-------------------")
# for elem in dir(countries):
#     if not re.search(r'^__.*__$', elem, re.I):
#         print(elem)
# print()


# # TUPLE METHODS
# # ============
# print()
# print("TUPLE METHODS:")
# print("-------------------")
# for elem in dir(environments):
#     if not re.search(r'^__.*__$', elem, re.I):
#         print(elem)
# print()

# # STRING METHODS
# # ============
print()
print("STRING METHODS:")
print("-------------------")
for elem in dir(env):
    if not re.search(r'^__.*__$', elem, re.I):
        print(elem)
print()
