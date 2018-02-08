#!/usr/bin/env python3

""" A calculator function to do
    addition, subtraction, multiplication, division

   Args:
        User to select the calculator operation
        Input the numbers for the selected operation

    Returns:
        Output of the function invoked

    Usage:
    python3 calculator.py <URL>
"""

cal_operation = ""
cal_function = ""
output_to_user = ""


def add_function(a, b):
    """User to input the numbers for addition

    Args:
        2 integers(User input)

    Returns:
        Addition of 2 numbers
    """
    return float(a) + float(b)


def sub_function(a, b):
    """User to input the numbers for subtraction

    Args:
        2 integers(User input)

    Returns:
        Subtraction of 2 numbers
    """
    return float(a) - float(b)


def mul_function(a, b):
    """User to input the numbers for multiplication

    Args:
        2 integers(User input)

    Returns:
        multiplication of 2 numbers
    """
    return float(a) * float(b)


def div_function(a, b):
    """User to input the numbers for division

    Args:
        2 integers(User input)

    Returns:
        division of 2 numbers
    """
    return float(a) / float(b)


def cal_functions(calfunction):
    if calfunction == "1":
        cal_operation = "Addition"
    elif calfunction == "2":
        cal_operation = "Subtraction"
    elif calfunction == "3":
        cal_operation = "Division"
    elif calfunction == "4":
        cal_operation = "Multiplication"
    else:
        cal_operation = "Un-know operation"
    return cal_operation


calfunction = input("Calculator functions\n"
                    "1. Addition\n"
                    "2. Subtraction\n"
                    "3. Division\n"
                    "4. Multiplication\n"
                    "Please select any one of the above --> ")
userinput = cal_functions(calfunction)
print("You have selected ---> " + userinput)

(x, y) = input("Please enter any 2 numbers for " + userinput + " -- ").split()

if calfunction == "1":
    output_to_user = add_function(x, y)
elif calfunction == "2":
    output_to_user = sub_function(x, y)
elif calfunction == "3":
    output_to_user = div_function(x, y)
elif calfunction == "4":
    output_to_user = mul_function(x, y)
else:
    output_to_user = "Invalid operation"

print(userinput + " of " + x + " and " + y + " is " + str(output_to_user))
