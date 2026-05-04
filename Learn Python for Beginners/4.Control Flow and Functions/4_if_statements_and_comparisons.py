
def maxnum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return print(f"{num1} is the largest")
    elif num2 >= num1 and num2 >= num3:
        return print(f"{num2} is the largest")
    else:
        return print(f"{num3} is the largest")


num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

maxnum(num1, num2, num3)