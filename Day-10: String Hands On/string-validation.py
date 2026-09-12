# 1	Username & Password Validation -> strip(), lower(), len()

# Password@123

# capital
# lower
# symbol
# digit
# lower
# upper

password = "PASSWORD@123"

upper = False
lower = False
digit = False
symbol = False

for i in password:
    if i.isupper():
        upper = True
    elif i.islower():
        lower = True 
    elif i.isdigit():
        digit = True    
    else:
        symbol = True

if 8 <= len(password) <= 15 and digit and lower and upper and symbol:
    print("Password is valid")
else:
    if not digit:   
        print("password doesn't have digit")
    elif not upper:   
        print("password doesn't have at least one upper")
    elif not lower:   
        print("password doesn't have at least one lower")
    else:
        print("Password doesn't have symbol")    
        
        
# 2	Mobile Number Validator	-> isdigit(), len(), indexing
# 3	Full Name Differentiator -> title(), split(), join()
# 4	Email Validator	-> find(), count(), startswith()
# email should have @
# @ shouldn't be multiple times
# no special character
# length 15 before @
# should have .
# " " should not be in it

email = "shivamnamdev@gmail.com"

if email.count("@") == 1 and len(email.split("@")[0]) <= 15 and "." in email and " " not in email:
    print("Valid email")
else:
    print("invalid email")


# 5	Product Search -> in, find(), lower()
# 6	YouTube Title Analyzer -> len(), split(), count()
# 7	Hashtag Generator -> replace(), split(), join()
# 8	PAN/ID Format Checker -> slicing, isalpha(), isdigit()
# 9	Password Strength Checker -> multiple string checks + loops
# 10 Chat Message Analyzer -> combining multiple string functions


numbers = [1, 2, 3]
letters = ["A", "B"]

result = [(num, letter) for num in numbers for letter in letters]
print(result)
