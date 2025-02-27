# Tuples
# Tuples are just like lists, however the key difference is immutability
# Tuples also uses parenthesis()
# Tuples also allows indexing and slicing
my_tuple = (1, "a", 2, 3, 4, "b", "c", "b", "c", 2, 2)
print(my_tuple[-1]) # return the last element of the tuple
print(my_tuple[3])

# Tuple methods
print(my_tuple.index(3)) # return the index of the first time 3 appears in the tuple
print(my_tuple.count("a")) # returns the number of times a appears in the tuple