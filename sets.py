# Sets
# Sets are unordered collection of unique elements
from PIL.ImageChops import duplicate

my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2)
print(my_set)

# You can also cast a list into a set. sometiimes to remove duplicate elements
my_list = [1, 2, 2, 1, 3, 1, 4, 5, 5, 6]
print(my_list)
print(set(my_list))