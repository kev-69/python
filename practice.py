# Immutability
name = "Sam"
last_letters = name[1:]
print(last_letters)
print("T" + last_letters + "e")

# Concatination
x = "Hello world!"
x = x + "\nIt is beautiful outside"
print(x)

# String multiplication
letter = "B"
multiplied_string = letter * 10
print(multiplied_string)

# Builtin string methods
uppercase_x = x.upper()
print(uppercase_x)
print(uppercase_x.split())
# with the split method, you can also split on a particular letter
print(uppercase_x.split("O"))
# print(type(x))