# Forrest Siminoe
# UWYO COSC 1010
# 11/10/24
# Lab 8
# Lab Section: 13
def num_converter(num):
    isNeg = False
    if "-" in num:
        isNeg = True
        num = num.replace("-"," ")
    if "." in num:
        num_list = num.split(".")
        if len(num.list)==2 and num_list[0].isdigit() and num_list[1].isdigit():
            if isNeg:
                return -1 * float(num)
            else: 
                return float(num)
    elif num.isdigit():
        if isNeg:
            return -1 * int(num)
        else:
            return int(num)
    else:
        return False



# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

print("*" * 75)
# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
#squareroot== n**(1/2)
def squareroot(n):
    if n < 0:
        return None
    return n**(1/2)

def quadratic_formula(a,b,c):
    top_layer = b**2 - 4*a*c
    squareroot_toplayer = squareroot(top_layer)
    if squareroot_toplayer is None:
        return "No real solutions, top layer is neative"
    root_positive = (-b + top_layer/2*a)
    root_negative = (-b - top_layer/2*a)
    return root_positive, root_negative
def user_input():
    a = float(input("Enter a value for a: "))
    b = float(input("Enter a value for b: "))
    c = float(input("Enter a value for c: "))
    roots = quadratic_formula(a,b,c)
    if isinstance(roots, str):
        print(roots)
    else:
        print(f" The values of the quadratic equation are: {roots[0]}, {roots[1]}")
user_input()