print("This program will find the maximum of three numbers.")

a = float(input("Please enter the first number: "))
b = float(input("Please enter the second number: "))
c = float(input("Please enter the third number: "))

if a >= b and a >= c:
    max_number = a  
elif b >= a and b >= c:
    max_number = b  
else:
    max_number = c

print(f"The maximum of {a}, {b}, and {c} is: {max_number}")