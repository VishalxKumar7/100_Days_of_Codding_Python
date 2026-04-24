### DICTIONARY

# Initializing the Dictionary
programming_dictionary = {
    "Bug":"An error in a program that prvents the program from executing",
    "Function": "A piece of code that you can call over and over again."
}

# Printing the one value from the dict using its Key 
print(programming_dictionary["Bug"])

# Adding new key-value pair in dict
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating a empty dict
empty_dict = {}

# Wipe an existing dict
# programming_dictionary = {}
# print(programming_dictionary)


# Edit an item in a dict
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through a dictionary
for x, y in programming_dictionary.items():
    print(f"{x}: {y}")
