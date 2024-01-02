
print("Welcome to Ray's calculator!")

operator = ''
def persantage(x, y):
    return (x*y)/100.0

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


operatorError = True
while operatorError:
     operator = input("Choose an operation (+, -, *, /, p[percent]): ")
     if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == 'p':
          # Return an error message if the user enters an invalid operator
          operatorError = False
     else:
          print("Invalid operator! Select one of the following: +, -, *, /, p")
          operatorError = True



# Performing the operation based on the selected operator

if operator== "p":
    number1 = float(input("Enter the first number(% of): "))
    number2 = float(input("Enter the second number: "))
else:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

if operator == "+":
    result = addition(number1, number2)
elif operator == "-":
    result = subtraction(number1, number2)
elif operator == "*":
    result = multiplication(number1, number2)
elif operator == "/":
    result = division(number1, number2)
elif operator == "p":
    result = persantage(number1, number2)
else:
    # Return an error message if the user enters an invalid operator
    result = "Error: Invalid operator"

# Result 
print(f"The result:         {result}")

