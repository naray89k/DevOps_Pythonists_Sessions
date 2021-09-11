# OPEN function

# READING A FILE:

# # Accessing file contents in for loop.
file_obj = open('content.txt')
for line in file_obj.readlines():
    print(line.strip())
file_obj.close()


# # Accessing file contents in with loop.
with open('content.txt') as file_obj:
    for line in file_obj.readlines():
        print(line.strip())

# WRITING A FILE:
# Accessing file contents in for loop.
file_obj = open('sessions-3.txt', 'w')
file_obj.write("This is a test file\n")
file_obj.close()

# Accessing file contents in with loop.
with open('sessions-3.txt', 'w') as file_obj:
    file_obj.write("This is a test file\n")
    text = ["This is second line\n",
            "This is third line\n"]
    file_obj.writelines(text)

# # APPEND TO A FILE:
# # Accessing file contents in for loop.
file_obj = open('sessions-3.txt', 'a')
file_obj.write("This is appended line\n")
file_obj.close()

# Accessing file contents in with block.
with open('sessions-3.txt', 'a') as file_obj:
    file_obj.write("This is a test file\n")
    text = ["This is sixth line\n", "This is seventh line\n"]
    file_obj.writelines(text)
