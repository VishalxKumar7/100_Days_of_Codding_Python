# len() only works for string, list, tuple, bytes, range, dict, sets
# len(123)
# TypeError: object of type 'int' has no len()
# print(len("Hello"))

# To check type of data
# print(type(123))
# print(type("123"))
# print(type(23.54))
# print(type(True))


# Type Coverstion
# print("123" + "456")  # String
# a = int("123")
# b = int("456")

# print(a+b)  # Sum of Two integers


# Exercise
name = input("Enter your name: ")
length = len(name)

print(type(name))
print(type(length))

print("Number of letter in your name: " + str(length))  # Coverting int in str
