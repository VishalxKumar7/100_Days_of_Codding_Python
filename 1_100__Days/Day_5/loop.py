#### For loop

## Traversing through the list using "For Loop"
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")


# ### Sum of the list
student_score = [150, 142, 185, 120, 171, 182, 24, 75, 97, 93, 47]

# sum = 0
# for score in student_score:
#     sum += score

# print(sum)


#### FIND OUT THE LARGEST NUMBER IN A LIST USING LOOP

max = 0
for score in student_score:
    if max < score:
        max = score

print(max)
