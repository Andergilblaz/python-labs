#----------------------
# Narcissistic Number -
#----------------------

# Determine whether a positive integer is narcissistic.
# A number is narcissistic if the sum of its digits each raised
# to the power of the number of digits equals the number itself.
# Example: 153 -> 1**3 + 5**3 + 3**3 = 153

# Tests:
# 1. is_narcissistic(153) -> True
# 2. is_narcissistic(154) -> False
# 3. is_narcissistic(371) -> True
# 4. is_narcissistic(512) -> False
# 5. is_narcissistic(9)   -> True
# 6. is_narcissistic(11)  -> False
# 7. is_narcissistic(9474)-> True
# 8. is_narcissistic(6549)-> False

def is_narcissistic(n):
    
    power = len(str(n))

    result = 0
    for digit in str(n):
        result += (int(digit) ** power)
        
    # Better
    return result == n

    # if result == n:
    #     return True
    # else:
    #     return False

    # print (result)
    # print(int(power))
    # print(n_list)

    # return n

print(is_narcissistic(153))