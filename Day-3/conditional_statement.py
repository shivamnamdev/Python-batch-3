
# print("Print this")
# print("Print not this")
# print("Print not this again")
# print("this should work")
# print("this shouldn't work")
# print("this shouldn't work too")

# Conditional statment: which enable a statement to be run or not
# if condition is true then -> do the action
# 1. if statement
# 2. if-else statement
# 3. elif statement


# if True-condition:
#     code

########## EXample: 1 ##############

print("Print this")
print("Print not this")
print("before condition")
if 5 % 2: # if this condition is true -> go into the block
    print("conditional values") # and perform these actions
    print("conditional values")
print("non-conditional value")

# In java
# if (condition){ 
#     print           
#                }
a = int(input())
if a > 0:
    print("")
    
    
# If-else statement

if True:
    print("This is working because condition is true")
else:
    print("This is working because condition is false")
    
    
a = int(input("enter your age:"))

if 0 <= a <=100: #if 0 less than a and a is less than 100
    print("valid age")
else:
    print("invalid age")
    
if a >= 0 and a <= 100: #if 0 >= a and a <= 100
    print("valid age")
else:
    print("invalid age")            