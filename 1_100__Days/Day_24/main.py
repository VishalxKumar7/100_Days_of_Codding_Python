
#### Normal way to open File
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# #### Prefered way to Open Files
# with open("my_file.txt") as f:
#     content = f.read()
#     print(content)

# #### Write in the file
# with open("my_file.txt", "w") as f:  # using only "w" will delete all the previous contents of the and write the new content
#     f.write("How are you")           # If the file don't exist and you Open it with the "w" mode it will create the file first then write the content


#### Append to the file
with open("C:/Python/100_days_of_coding/1_100__Days/Day_24/my_file.txt", 'r') as f:
    content = f.read()
    print(content)