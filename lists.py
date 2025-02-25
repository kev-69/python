my_list = [1, 2, 3, "one", "two", "three"]
print(my_list.__len__())
print(len(my_list))

# slicing and indexings also works with lists
print(my_list[3])
print(my_list[3:])

# we can also concatenate list
new_list = ["four", "five", "six", 4, 5, 6]
print(my_list + new_list)

arranged_numbers = my_list[:3] + new_list[3:]
print(arranged_numbers)
print(len(arranged_numbers))

arranged_words = my_list[3:] + new_list[:3]
print(arranged_words)
print(len(arranged_words))
# print(arranged_numbers + arranged_words)

# we can mutate list unlike strings
# lets change the arranged numbers to even numbers
arranged_numbers[0] = 2
arranged_numbers[1] = 4
arranged_numbers[2] = 6
arranged_numbers[3] = 8
arranged_numbers[4] = 10
arranged_numbers[5] = 12
print(arranged_numbers)

# lets change the words in the arranged words to caps
arranged_words[0] = arranged_words[0].upper()
arranged_words[1] = arranged_words[1].upper()
arranged_words[2] = arranged_words[2].upper()
arranged_words[3] = arranged_words[3].upper()
arranged_words[4] = arranged_words[4].upper()
arranged_words[5] = arranged_words[5].upper()
print(arranged_words)

# List methods
arranged_numbers.append("14")
arranged_words.append("SEVEN")
print(arranged_numbers)
print(arranged_words)

nums = [4, 32, 1, 424, 3, 34, 531]
nums.sort()
print(f"Sorted numbers list: {nums}")
nums.reverse()
print(f"Reversed numbers list: {nums}")
