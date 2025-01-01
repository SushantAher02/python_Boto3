# Taking input as numbers (convert strings to float for broader support)
num_1 = float(input("Enter your num_1: "))
num_2 = float(input("Enter your num_2: "))

# Defining functions for operations
def addition():
    return num_1 + num_2

def subtraction():
    return num_1 - num_2

def multiplication():
    return num_1 * num_2

def division():
    # Handle division by zero
    if num_2 != 0:
        return num_1 / num_2
    else:
        return "Error: Division by zero is not allowed."

# Printing results
print("This is addition:", addition())
print("This is subtraction:", subtraction())
print("This is multiplication:", multiplication())
print("This is division:", division())
