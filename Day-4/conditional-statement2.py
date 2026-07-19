print("Print this")
print("Print not this")
print("Print not this again")
print("this should work")
print("this shouldn't work")
print("this shouldn't work too")

# syntax
# if condition is true here:
#     this should run
# elif condition is true here:
#     this should run
# elif condition is true here:
#     this should run
# elif condition is true here:
#     this should run
#     ...
# else:     
#     this should run      


marks = int(input("Give me your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B") 
elif marks >= 50:
    print("Grade C")  
else: 
    print("Fail")  
    
    
num1 = float(input("Enter your first number:"))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter your second number:"))

print(type(operator))


if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)    
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error division by zero")    
else:
    print("invalid operator ")
           
