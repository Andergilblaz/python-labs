num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, /, *): ")

if num1 < 0 or num2 < 0:
    print("The numbers are not compatible")
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("The operator is not compatible")