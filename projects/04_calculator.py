# python calculator

operator = input("Enter an operator:")
num1 = float (input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if operator == "+":
    result = num1 + num2
    print(round(result))  # here round is a function 

elif operator == "-":
    result = num1 - num2
    print(round(result))

elif operator == "*":
    result = num1 * num2
    print(round(result))

else:
    result = num1 / num2
    print(round(result))