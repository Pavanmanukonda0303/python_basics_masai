print("This is a simple calculator program that can perform basic arithmetic operations based on the operator selected.")

number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))  
operator = input("Please enter the operator (+, -, *, /): ")

if operator == '+':
    result = number1 + number2
    print(f"The result of {number1} + {number2} is: {result}")
elif operator == '-':
    result = number1 - number2
    print(f"The result of {number1} - {number2} is: {result}")
elif operator == '*':
    result = number1 * number2
    print(f"The result of {number1} * {number2} is: {result}")
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
        print(f"The result of {number1} / {number2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")    
