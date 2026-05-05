def is_narcissistic(n):
    
    n_list = []
    power = len(str(n))

    for digit in str(n):
        n_list.append(digit)


    i = 0
    result = 0

    while i < len(n_list):
        result = result + (int(n_list[i]) ** power) 
        i += 1
        
    if result == n:
        return True
    else:
        return False

    # print (result)
    # print(int(power))
    # print(n_list)

    # return n

print(is_narcissistic(153))