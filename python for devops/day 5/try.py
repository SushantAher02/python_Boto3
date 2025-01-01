import sys

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
elif operation == "sub":
    output = sub(num1, num2)
elif operation == "mul":
    output = mul(num1, num2)
else:
    output = "Invalid operation"
print(output)
