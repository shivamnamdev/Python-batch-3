# Functions
# - Primary goal of a function is - repeat the task
# Resuse the Block of code in any point of time in the program
# - Function has definition and calling

# Built-in Global functions
# print()
# input()
# len()
# int()
# float()
# str()
# dict()
# set()
# list()
# type()

# List Function
# l = []
# l.append()


# print("Functionality of print is printing the stream")


def greet():
    print("Welcome to the python class.")
    
    
greet()
greet()
greet()
greet()


# greet => task
# task 1
# task 2
# 1000 lines of code 
# task 3
# 300 lines of code
# task 4


def new_greet(message): #parameter
    print(message)
    
# new_greet("This is my first message","This won't work")  TypeError: new_greet() takes 1 positional argument but 2 were given
new_greet("This is my second message") # arguement
# new_greet()  TypeError: new_greet() missing 1 required positional argument: 'message'


def welcome(name):
    print("Welcome to the class",name)
    
welcome("Vipul")
welcome("Poornima")    


def add(a,b):
    print(a+b)
    
add(3,5) # 8
add(7,10)   # 17 
add("Vipul", " Sontakke")
# add("vipul",1) #TypeError: can only concatenate str (not "int") to str


# Return Keyword

def multiply(a,b):
    return a*b

val = multiply(3,5)
print(val)

# print(multiply(add(2,5),add(9,5))) TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'


# any data type passing is supported while calling a function
def printlist(l):
    for i in l:
        print(i)
    
printlist([1,2,3,4,5]) 

# What if you want to restrict specific data type

def pythonsession(a: str, b: str) -> int:
    print(type(b))
    print(a, b)  
    return 10 
    
pythonsession("Welcome", 1)    

# Example: Functions for student marks

def print_marks(data):
    for subjects in data:
        print(subjects, ":", data[subjects])


marks = {
    "maths": 80,
    "science": 75
}

marks1 = {
    "maths": 81,
    "science": 90
}

print_marks(marks)
print_marks(marks1)

# Parameters vs Argument
# Arguement -> Actual values that we are passing while calling the function
# Parameter -> Variables inside the function


y = 10 # -> Global Variable
def show(z): # -> Parameter/Local Variable
    global y
    # globals()['y'] = 30
    y = 30 # -> Global variable scope under this function
    x = 20 # -> Local Variable
    print("within functionsum:",x+y+z)
    print("within function y:",y)
    return x
    
# print(x)
p = 30
print("global:",y)    
l = show(p)
print("global:",y)
print("global:",l)
print("global:",p)



def email(name):
    print("Hello", name, " Thanks for subscribing")
    
subscribers = ["Poornima","Vipul", "Harshit", "Tushar"]

for i in subscribers:
    email(i)    