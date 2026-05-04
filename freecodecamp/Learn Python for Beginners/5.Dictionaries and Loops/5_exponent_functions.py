
print(2**3)

base = int(input(f"Introduce the base:"))
power = int(input(f"Introduce the power:"))

print(base**power)

# It's the same but I copy it also to learn

def raise_to_power (base_num,power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(raise_to_power(3,2))