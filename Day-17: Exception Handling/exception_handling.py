# Exception: Exception is an event, which terminates the program in between

# Exception -> Error

# Types of Exceptions:
#  - SyntaxError -> Solution: IDE updates the syntax errors
#  - Runtime Error -> Solution: Exceptional Handling
#  - Logical Error -> AI assisted IDEs(VScode, Cursor, Antigravity etc) 


print("This is the frist manager")
print("This is the frist manager")
print("This is the frist manager")


# with open("Testing", "r") as f: FileNotFoundError: [Errno 2] No such file or directory: 'Testing'
#     print("not working")
    
# try:
#   risky code
# except Defined-Exception:
#   raise - act exception
# else:
#   perform only when not exception found
# finally:
# perform everytime


# Example 1: with explicitly mentioning the exception
try:
    with open("Testing", "r") as f: 
        print(f.read())
except FileNotFoundError:
    print("File is not existing, please create file first")  



# Example 2: without explicitly mentioning the exception
try:
    with open("Testing", "r") as f: 
        print(f.read())
    print(f.read())    
except:
    print("File is not existing, please create file first")  



# Example 3: with handling runtime exception
try:
    with open("Testing", "r") as f: 
        print(f.read())
    print(f.read())    
except Exception as e:
    print("My Error is:", e)  
 
 
# Example 4: multiple known exception
try:
    with open("Testing2", "r") as f: 
        print(f.read())
    print(f.read())    
except FileNotFoundError:
    print("File is not existing, please create file first") 
except ValueError:
    print("File is already Closed")   
    
    
    
# Else and Finally
try:
    value = int(input("enter the value for division:"))
    print(10/value)    
except ZeroDivisionError:
    print("you are diving with zero") 
except TypeError:
    print("you have entered this value:", value)   
except ValueError:
    print("you have entered string inplace of integer:")  
except NameError:
    print("Variable not defined:")       
else:
    print("there is no error found") 
# else: -> syntax error: there cannot be multiple else
#     print("this is another else")    
finally:
    print("this piece of line will run everytime")
# finally: -> syntax error: there cannot be multiple finally
#     print("another finally block")        
          
          
 #   Raised an Error
value = 0
if value == 0:       
    pass
    # raise ValueError("the number cannot be zero")
       
print("Printing after risky code")
    
    
# Custom Exception
try:
    age = int(input("Enter your age:"))
    if age > 18:
        print("you can vote")
    else:
        raise Exception("You are not eligible to vote")   
except Exception as e:
    print("UserMadeException:",e)         