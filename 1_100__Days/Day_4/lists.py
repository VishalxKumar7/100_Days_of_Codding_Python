# List is the mostly used data structure in python
states_of_us = ["Delaware", "Pennsylvania", "New Jersy", "Georgia", "Connecticut", "Arizona"]

# Printing the list by there position
# print(states_of_us[0])  # printing the list by there number
# print(states_of_us[1])
# print(states_of_us[-1])  # -1 is last item of the list
# print(states_of_us[-2])

# # Changing the item of the list
# states_of_us[1] = "Washington"
# print(states_of_us)

# # Adding in the list at the end
# states_of_us.append("Taxes")
# print(states_of_us)

states_of_us.extend(["California", "Florida"])   # or "insert"
print(states_of_us)