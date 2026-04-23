### Simple greet function
# def greet():
#     print("Hi, How are you!")
#     print("Welcome to this beautiful place")
#     print("Have a grate day")

# greet()


# # Funtion that allowed input
# def greet_with_name(name):    # Here "name" is the Parameter
#     print(f"Hello {name}")
#     print("How are you")
#     print("Have a grate day!")

# greet_with_name("vishal")   # "Vishal" is the Argument that is send to the Parameter



# # Function with more than one input
# def greet_with(name, location, places):     # Multiple Parameret
#     print(f"Hi {name}")
#     print(f"Welcome to {location}")
#     print(f"We have {places} places to visit")

# greet_with("Vishal", "Delhi", 8)       # Multiple Argument. Order of Argument matters. Send Argument in same sequence as the Parameter
# greet_with(location="Mumbai", name="Harsh", places=9)  # But if you are sending the Argument with Perameters then order dosen't matter




def calculate_love_score(name1, name2):
    list = []
    for letter in name1 + name2:
        list.append(letter)
        
    T = list.count('t')
    R = list.count('r')
    U = list.count('u')
    E = list.count('e')
    
    Total1 = T + R + U + E
    
    L = list.count('l')
    O = list.count('o')
    V = list.count('v')
    
    Total2 = L + O + V + E
    
    print(f"Love Score {Total1}{Total2}")    
    
    
    
    
name1 = input("Enter the first name: ").lower()
name2 = input("Enter the second name: ").lower()

calculate_love_score(name1, name2)