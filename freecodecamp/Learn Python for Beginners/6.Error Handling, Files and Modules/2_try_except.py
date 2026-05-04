
try:
    value = 10/0
    number = int(input("Introduce a number:"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print(f"Invalid number")

