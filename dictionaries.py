# dictionaries are like object from js. they hold data in key:value pairs
my_dict = {"first_name":"Bismark", "last_name":"Obuobi"}

# note that we call the values with their respective keys and we use the [] where the index is the key
print(my_dict["first_name"])

# also a dictionary can also hold a list and or another dictionary
new_dict = {"name":"Kevlar",
            "school":"University of Ghana",
            "year_one_courses": ["dcit 101", "dcit 104", "dcit 105"]
            }
print(f"My name is {new_dict["name"]} schooling at {new_dict["school"]} and have read the these courses {new_dict["year_one_courses"][0]}, {new_dict["year_one_courses"][1]}, {new_dict["year_one_courses"][2]}")

# it is also possible to add a new key:value pair to a dictionary just like lists
my_os = {
    "first_os": "Windows 7",
    "second_os": "Windows 11",
}
my_os["third_os"] = "Ubuntu"
my_os["forth_os"] = "Mac OS"
print(my_os)

# we can also replace a particular key's value in a dictionary
my_os["first_os"] = "Windows 8"
print(my_os)

# Dictionary methods
print(my_os.keys()) # returns all the keys in the dictionary
print(my_os.values()) # returns all the values in the dictionary
print(my_os.__len__()) # returns the length of the dictionary
print(new_dict.get("year_one_courses")) # requires the key of the value you want to find(get) and returns the value
print(new_dict.items()) # returns the items in the dictionary in their pairs