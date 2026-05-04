# *************************************(args)*********************************

# def add(*args):
#     # print(args)
#     # print(type(args))
#     print(args[1])

#     sum = 0
#     for n in args:
#         # print(n)
#         sum += n
#     return sum

# print(add(3, 5, 8))


# *************************************(kwargs)***********************************

# def calculate(n, **kwargs):
#     print(kwargs)
#     # print(type(kwargs))
#     # for key, values in kwargs.items():
#     #     print(key)
#     #     print(values)

#     # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(2, add = 3, multiply = 5)



class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")  # If do not send the value of the model it will not through the error it will that arg as 'None'.


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)