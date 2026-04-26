### Global Variable

enemies = 1

"""This will show the error. We can print acces the global operator but can not perform any
 operation with that because the global variable could be used my more than one function and
 if we change the value it will effect every function that is using that global variable
"""
# def increase_enemies():
#     enemies += 1 
#     print(enemies)      

# increase_enemies()

""" To perform some operation be have tell that assine is as global variable inside the function"""
# def increase_enemies():
#     global enemies      # But it is not prefered. We should avoid it 
#     enemies += 1
#     print(f"enemeies outside funtion: {enemies}")

# increase_enemies()
# print(f"enemies ouside function: {enemies}")

def increase_enemies(enemy):
    
    return enemy + 1

enemy =increase_enemies(enemies)
print(f"enemies ouside function: {enemy}")