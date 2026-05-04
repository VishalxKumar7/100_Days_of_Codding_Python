# num = [1, 2, 3]
# new_list = [n + 1 for n in num]
# print(new_list)

# name = "Angela"
# letters_list = [letter for letter in name]
# print(letters_list)

# range_list = [num * 2 for num in range(1,5)]
# print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_name = [name for name in names if len(name) < 5]
# print(short_name)

upper_case_name = [name.upper() for name in names if len(name) > 5]
print(upper_case_name)