
file = open("6.Error Handling, Files and Modules\\3_employees.txt", "r")

# print(file.readlines())

for employee in file.readlines():
    print(employee)

file.close()