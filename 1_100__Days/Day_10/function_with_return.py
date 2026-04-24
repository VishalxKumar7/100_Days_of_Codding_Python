## FUNCTION WITH OUTPUT

# returning the function
def function_1(text):
    """ Take a first and last name and format it to return the title case"""  ## DocString """This is"""
    return text + text

# Returning the function with camle case
def function_2(text):
    return text.title()

# Passing the Arguemnt to one function which is returned by other function
output = function_2(function_1("hello my name is vishal ")) 
print(output)

# print(function_1("Capital of India is Delhi"))
# print(function_2("capITAl of India IS delhi"))


# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"{formated_f_name} {formated_l_name}"

# formated_name = format_name(f_name="vishal", l_name="kumar")
# print(formated_name)