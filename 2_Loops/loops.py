# name = "some_name"
# if name:
#     print("Hi! ")
#     print(name)
#
# for elem in range(1, 11):
#     print(elem)
#
# nums = [1, 2, 3, 4, 5]
# country_capital = {"India": "Delhi",
#                    "USA": "Washington",
#                    "UK": "London",
#                    "Germany": "Berlin"}
# countries = {"India", "USA", "UK", "Germany"}
# environments = ('DEV', 'TEST', 'UAT', 'PROD')
#
# # for loop example
# for country in countries:
#     print(country)
#
#
# # while example:
num = 70
while num <= 80:
    print(num)
    num += 1

num = 0
while num <= 100:
    print(num)
    num += 3


num = 0
while num <= 300:
    print(num)
    num += 15


def custom_range(start, end, step):
    num = start
    while num <= end:
        print(num)
        num += step


custom_range(0, 100, 3)
custom_range(0, 300, 15)
custom_range()



