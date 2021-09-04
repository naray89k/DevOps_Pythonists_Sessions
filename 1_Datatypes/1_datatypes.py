#
# Dictionary
#
country_capital = {"India": "Delhi",
                   "USA": "Washington",
                   "UK": "London",
                   "Germany": "Berlin",
                   "India": "Mumbai"}
print(country_capital)
country_capital["Norway"] = "Oslo"
country_capital["Kashmir"] = ["Jammu", "Srinagar"]

for key, val in country_capital.items():
    print(key, val)


print()
print("Accessing Dictionary Elements by Key")
print(country_capital["India"])


country_capital["India"] = "Chennai"
print()
print("Accessing Dictionary Elements by Key")
print(country_capital["India"])


#for elem in dir(country_capital):
#    if not elem.startswith('--'):
#        print(elem)

# =======================
# Set
# =======================

countries = {"India", "USA", "UK", "Germany"}
for elem in dir(countries):
    print(elem)

# ===========
# TUPLE
# ===========
one_elem_tuple = 1,3,4
regular_tuple = (1,2,3,4,5,6,7,8)
print(type(one_elem_tuple))
