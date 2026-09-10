# TUPLE: collection of data types -> immutable
 
l = [1,2,3,4]
t = (1,2,3,4)
t2 = tuple()

print(type(l), type(t))

# How to access
print(t[1]) # 2
print(t[1:4]) #(2, 3, 4)

# Use case
location = (123.80, 241.80)

# Update won't work

# t[3]=54 TypeError: 'tuple' object does not support item assignment

# Tuple Functions
t = (1,2,2,2,2,1,1,1,5,5,5,5,2,2,2,2)
print(t.count(2))
print(t.index(5))

mytuple = ("banana", "orange","mango","guava","pineapple")

print(mytuple.index("orange"))

# Possible values - immutable

mytuple2 = (1,2,3,4,"first","second","third",True, False, 14.2, 16.8,98.2,[3,2,1],{1,2,3},(1,6,2),{"key":"value"})
print(mytuple2)

mytuple2[12][1] = 5
print(mytuple2)

# mytuple2[13] = {4,1,5}  TypeError: 'tuple' object does not support item assignment

# Parsing the tuple

for t in mytuple:
    print(t)
    
for i in range(len(mytuple)):
    print(i, mytuple[i])    
    

# How to change tuple value - backdoor 
mytuple = ("banana", "orange","mango","guava","pineapple")
updatet = list(mytuple)  

updatet.append("kiwi")
print(updatet)

mytuple = tuple(updatet) 
print(mytuple)


    