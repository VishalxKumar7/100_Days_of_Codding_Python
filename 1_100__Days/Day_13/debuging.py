from random import randint

dice_image = ['1','2','3','4','5','6']

dice_num = randint(1, 6)
print(dice_image[dice_num])

## The bug is that randint choosing number from 1 to 6 but dice_image indexes are from 0 to 5
dice_num = randint(0,5) # This is correct

## try:    except:

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("You have typed an invalid number please try again with numberical resul like 15")
    age = int(input("Enter your age: "))


if age < 18:
    print(f"you can drive at age {age}")
else:
    print(f"You can drive")