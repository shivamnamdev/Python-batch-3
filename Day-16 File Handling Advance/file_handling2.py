

# Open and Close were necessary every time   

# file = open("Testing.txt", "r")
# file.read() 
# file.close()

# Using with keyword
with open("Testing.txt", "r") as file:
    var = file.read()
    
print(var)  


# Short hand technique
# file = open("Testing.txt", "r")
# print(file.read())
print("*"*10)
print(open("Testing.txt", "r").read())  


with open("Testing.txt", "a") as file:
    file.write("\nThis is a new line using append")

# Readline() --> reads one line at a time
with open("Testing.txt", "r") as file:
    print(file.readline(5))
    print(file.readline(4))
    print(file.readline(3))
    print(file.readline(2))
    print(file.readline(1))
    
    print(file.readline())
    print(file.readline(-99))
    lines = file.readlines() # returns list of lines
    

# This file is opening through with keyword

with open("CopingContent.txt", "w") as file:
    file.writelines(lines) # writes list of lines to file


# Program to search a word in a file

# File read karoge
# line by line dekhenge ki wo word h ya nahi
# agr hoga to print krenge
print("*"*10)
# with open("PythonFileForTesting.txt", "r") as file:
#     line = file.readline()
#     if "python" in line:
#         print(line)
        
#     line = file.readline()
#     if "python" in line:
#         print(line)
        
#     line = file.readline()
#     if "python" in line:
#         print(line)        

#     line = file.readline()
#     if "python" in line:
#         print(line)                
      
      
with open("PythonFileForTesting.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if "python" in line:
            print(line)  
    
with open("PythonFileForTesting.txt", "r") as file:
    for line in file:
        if "python" in line:
            print(line)          
        
             