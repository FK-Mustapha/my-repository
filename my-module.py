#Text reverser function
message = input("Enter a text message")
def reverse_text(text):
    '''This function reverses a given code'''
    return text[::-1]
print(reverse_text(message))




def add(a, b):
    '''This function adds two numbers'''
    return a + b
def subtract(a, b):
    '''This function substracts two numbers'''
    return a - b
def multiply(a, b):
    '''This function multiplies two numbers'''
    return a * b
def divide(a, b):
    '''This function divides two numbers'''
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

print("Select operation: +, -, *, /")
operation = input("Enter operation: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    result = "Invalid operation"

print("Result:", result)



#too many function blocks used for the calculator program
