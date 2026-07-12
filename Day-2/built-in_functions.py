
# print("first sentence", end=' ')
# print("second sentence")

# print("first value", "second value", 1,10.2, False, sep=',')


# # Escape Characters

# # \n -> newline
# # \t -> tab
# # \" -> "
# # \\ -> \

# print("This is my \"project\".  and this is my backslash \\")

# # INPUT function
# print(input("Enter the first value: "))

# inp = input("Enter the second value: ")
# print(type(inp))

# age = int(input("Give me your age: "))



# # typecasting - typeconversion
# print(type(int(inp))) # <class 'int'>
# print(type(float(int(inp)))) # <class 'float'>
# print(type(str(float(int(inp))))) # <class 'str'>

# stringvalue = input("take a new input:")
# print(type(stringvalue))
# # Traceback (most recent call last):
# #   File "/Users/shivamnamdev/shivam/python-step-by-step/Day -2/built-in_functions.py", line 35, in <module>
# #     print(int(stringvalue))
# # ValueError: invalid literal for int() with base 10: 'This is my new input in string'

# len function
i = 10
f = 10.0
b = False
s = "String value.     "
# print(len(i)) TypeError: object of type 'int' has no len()
# print(len(f)) TypeError: object of type 'float' has no len()
# print(len(b)) TypeError: object of type 'bool' has no len()
print(len(s))
