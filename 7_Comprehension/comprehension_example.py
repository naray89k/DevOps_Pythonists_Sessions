


# LIST COMPREHENSION
# Traditional way
h_letters = []

for letter in "human":
    h_letters.append(letter)

print(h_letters)

# LIST COMPREHENSION
h_letters = [letter for letter in 'human']
print(h_letters)

# Conditionals in List Comprehension
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

# Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)


# DICT COMPREHENSION
persons = [
    {
        'name': 'Alice',
        'age': 30,
        'title': 'Data Scientist'
    },
    {
        'name': 'Bob',
        'age': 35,
        'title': 'Data Engineer'
    },
    {
        'name': 'Chris',
        'age': 23,
        'title': 'Machine Learning Engineer'
    }
]

print("dict comprehension")
data_employees = {}
for p in persons:
    if 'Data' in p['title']:
        data_employees[p['name']] = p['title']
print(data_employees)

# dict comprehension
data_employees = {p['name']:p['title'] for p in persons if 'Data' in p['title']}
print(data_employees)


# DICT COMPREHENSION
print("set comprehension")
data_employees = set()
for p in persons:
    if 'Data' in p['title']:
        data_employees.add(p['name'])
print(data_employees)

# set comprehension
data_employees = {p['name'] for p in persons if 'Data' in p['title']}
print(data_employees)


print("Generator")
def even_generator(numbers):
    return_list = []
    for n in numbers:
        if n % 2 == 0:
            #return_list.append(int(n/2))
            yield int(n/2)
    #return return_list

my_list = list(range(11))
eg = even_generator(my_list)
dir(eg)

for e in eg:
    print(e)

print(list(eg))
for e in eg:
    print(e)

eg = (int(number/2) for number in my_list if number % 2 == 0)

