# calling a function ---> comment
# Basic data types
print("This is my first program")
# Text -> string
print(23) # number -> integer
print(14.2) # decimal -> float
print(False) # Boolean

print(type("This is my first program")) # Text -> string
print(type(23)) # number -> integer
print(type(14.2)) # decimal -> float
print(type(False)) # Boolean

type("This is my first program")

list
# Collection Data type
l = ["value1", 12,123.5,False,[1,2,3]] # list
["value1", 12,123.5,False,[1,2,3]] = l
t = ("value1", 12,123.5,False,[1,2,3]) # tuple
s = {3,7,2,1,"anothervalue"} # set
d = { # key : value # dictionary
    "name": "tushar",
    "lead":"yogesh",
    'marks':12
     }
print(l)
l = ["value1", 12,123.5,False] 
print(l)

print(type(["value1", 12,123.5,False,[1,2,3]]))

print(type(("value1", 12,123.5,False,[1,2,3])))

print(type({3,7,2,1}))

print(type({ "name": "tushar","lead":"yogesh"}))
# each and every line is nothing but an instruction to python interpretor
# let see the above example
# -> print the message i am giving in () -> paranthesis


# Functionality
# which has some functionality
# types:
# - built-in functions - already defined by python
# - packed functions - already defined but need to import first
# - user-defined functions - need to define the function

# every function has 4 things
# function definition - function calling 
# - function parameter/arguement - function return/non-return