# Nested If-elif-else Conditions
print("Welcome to the rollercoaster!")
height = int(input("Enter the height: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets $12")
    
    want_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if want_photo == "y":
        bill += 3
    
    print(f"You final bill is {bill}")

else:
    print("You can't ride the rollercoaster")