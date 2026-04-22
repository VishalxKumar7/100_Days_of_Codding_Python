#### RANGE WITH FOR LOOP

# for num in range(1,11):  # loop will print from 1 to 10 and it don't print 11
#     print(num)


# for num in range(1, 11, 3):  # loop will print the num by skiping 3 digits
#     print(num)


# sum = 0
# for num in range(1,101):
#     sum += num

# print(sum)

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 ==0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)