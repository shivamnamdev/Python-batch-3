
# Syntax
# for item in collection:
#     action

var = "Mahak"

for char in var:
    print(char)

l = ["value1", 12,123.5,False,[1,2,3]] # list
t = ("value1", 12,123.5,False,[1,2,3]) # tuple
s = {3,7,2,1,"anothervalue"} # set
d = { # key : value # dictionary
    "name": "tushar",
    "lead":"yogesh",
    'marks':12
     }
for e in l:
    print(e)

for p in t:
    print(p)

for q in s:
    print(q)
    
for k,v in d.items():
    print(k,v)
    
    
# age = False

# for i in age:
#     print(i)    
    
# TypeError: 'bool' object is not iterable
# TypeError: 'int' object is not iterable
# TypeError: 'float' object is not iterable


for i in range(1,10):
    print(i)
    
print(*range(1,10)) 
print(type(range(1,10)))

# for i in range(1.0,10.0):
#     print(i)
    
# TypeError: 'float' object cannot be interpreted as an integer  

range(1, 50) # -------> 1 to 49 
range(50) # -------> 0 to 49 
range(1,10,2) # -------> 1 3 5 7 9

range(5, 20, 3) #---------> 5 8 11 14 17

for i in range(5, 20, 3):
    print(i)
    
# reverse loop    
for i in range(10,1,-1):
    print(i)    
    
# 2 ka table print krna h
# hr line me print hoga -> 2 * <change value> - string = 2*<changevalue> -int

# print(f"2 * {1} = {2*1}") #-> professional way
# print("2 *", 1, "=", 2*1) #-> beginner way

table = int(input())
for i in range(1,11):
    print(f"{table} * {i} = {table*i}")
    
for i in range(2,21):
    if i % 2 == 0:
        print(i)     

