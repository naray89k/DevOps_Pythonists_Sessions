
# 1. Write a Python program to sum all the items in a list.

list1 = [1,2,3,4,5,6]
print(sum(list1))
max(list1)

# PRODUCT OF ELEMENTS
prod = 1
for elem in list1:
    prod = prod * elem
print(prod)

print(max(list1))

print(min(list1))

words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
n = 4

for word in words:
    if len(word) > 4:
        print(word)