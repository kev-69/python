# Print formatting with strings

# formatting with the .format() method
print("This is a string",format("inserted"))
print("The {} {} {}".format("quick", "brown", "fox"))

# you can also insert the formatted strings using their index
print("The new {1} {0} {2}".format("brown", "big", "bag"))

# also you can assign the arguments
print("The {l} {y} school {b}".format(l = "large", y = "yellow", b = "bus"))

# float formatting
result= 100/777
print(result)
print("The result is {}".format(result))

# we can also adjust the with and precision of the long floating point number
print("The result was {r:1.3f}".format(r = result))

# f strings
name = "Kevlar"
print(f"Hello {name}")