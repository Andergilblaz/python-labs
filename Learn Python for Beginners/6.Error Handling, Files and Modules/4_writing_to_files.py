
# a = Append: adds text to the end of the file
# w = Write: overwrites the file with new content
# r+ = Read + Write: allows both reading and writing

file = open("6.Error Handling, Files and Modules\\4_employees.txt", "a")

# If we run it twice, it will appear on the same line, so we need to be careful and add \n
print(file.write("\nFoxtrot - Video creator"))

file.close()