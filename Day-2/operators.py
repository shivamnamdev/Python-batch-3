# # Operators: To perform operations between 1 or more than 1 variables/literals

# # 1. Arithmetic Operator
# # 2. Logical Operator
# # 3. Comparitive Operator
# # 4. Membership Operator
# # 5. Identity Operator
# # some more operators ....

# # 1. Arithmetic Operator

# # + - * / // ** %

# a, b = 2,4
# c, d = 6,8
# print(a + b) # 10
# print(a - b) # 6
# print(a * b) # 16
# print(a / b) # 4.0
# print(a // b) # only decimal 4
# print(a ** b) # exponential 64
# print(a % b) # remainder 0

# # BODMAS -> Bracket open -> Divide -> Multiply -> Add -> Subtract
# print(c//a*d+b-a)
# # 6/2*8+4-2
# # 3*8+4-2
# # 24+4-2
# # 26

# # with strings
# f = "my first string "
# s = "my second string"

# # for string + performs concatincation
# print(f + s)

# # for string * performs repeatation
# print("Python "* 10)

# # 2. Logical Operator
# # or and not

# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False
# print("*"*10)
# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False
# print("*"*10)
# print(not True) # False
# print(not False) # True


# # integer
# # False -> 0
# # True -> anything apart from 0

# # float
# # False -> 0.0
# # True -> anything apart from 0.0

# # String
# # False -> ""
# # True -> "<anything in string>"

# print(0 and "No" and False) # 0
# print("Yes" and "No") # No
# print("yes" and "no" and "") #
# print("1" or 1) # 1
# print(0 or "") # Null
# print(not -1) # False
# print(not "") # True
# print(not "String") # False
# print(not None) # True
# print("" or 0 or 1.1 or False) # 1.1
# print("" and 0 and 1.1 and False) # 

# # 3. Comparitive Operator -> true or false return
# #  < > <= >= == !=

# a = 2
# b = 4

# print(a == b) # both are equal? False
# print(a < b) # less than? True
# print(a > b) # Greater than? False
# print(a <= b) # < or == -> True
# print(a >= b) # > or == -> False
# print(a != b) # not == -> True

# 4. Membership Operator

# in
print('poori' in "poornima") # False
print('poor' in "poornima") # True

print('P' in "poornima") # False
print('P' not in "poornima") # True

# print(3 in 333) TypeError: argument of type 'int' is not iterable