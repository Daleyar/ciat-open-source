import sys

# -------------------------------------------------------- #
# -- CALCULATOR FUNCTIONS -------------------------------- #
# -------------------------------------------------------- #

# Add function
# a -- addend
# b -- augend
def add(a, b):
    return a + b

# Subtract function
# a -- minuend
# b -- subtrahend
def sub(a, b):
    return a - b

# Multiply function
# a -- multiplicand
# b -- multiplier
def mult(a, b):
    try:
        return a * b
    except Exception as e:
        print(f"Error during multiplication: {e}")
        return None

# Divide function
# a -- dividend
# b -- divisor
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        return None
    except Exception as e:
        print(f"Error during division: {e}")
        return None

# Modulo function
# a -- dividend
# b -- divisor
def mod(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print("Error: Modulo by zero is not allowed!")
        return None
    except Exception as e:
        print(f"Error during modulo operation: {e}")
        return None

# -------------------------------------------------------- #


# -------------------------------------------------------- #
# -- MAIN FUNCTIONAILTY -- DO NOT EDIT ------------------- #
# -------------------------------------------------------- #

a = None
b = None
op = None

while (True):
    # get input values
    a = input("Enter the first argument: ")
    op = input("Enter the operation: ")
    b = input("Enter the second argument: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print ("Invalid number argument...")
        op = None

    # decide function
    if (op != None):
        if (op == "+"):
            print ("Sum: ", add(a, b))
        elif (op == "-"):
            print ("Difference: ", sub(a, b))
        elif (op == "*"):
            print ("Product: ", mult(a, b))
        elif (op == "/"):
            print ("Quotient: ", div(a, b))
        elif (op == "%"):
            print ("Remainder: ", mod(a, b))
        else:
            print ("Invalid operation...")

    q = input("Quit? [y/n] ")
    if (q == "y" or q == "Y"):
        break

# -------------------------------------------------------- #