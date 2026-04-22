# Using Random Module
import random

# random_num = random.randint(2, 8)
# print(random_num)

# random_number = random.random()       # .random generate random number between 0 to 1
# print(random_number)


# random_number = random.random()*10
# print(random_number)

### Ramdom Floating ponit number
# float_num = random.uniform(1, 10)
# print(float_num)


# Print Head and Tails
random_heads_tails = random.randint(0, 1)

if random_heads_tails == 0:
    print("Heads")
else:
    print("Tails")