# Set
# A collection of unique values - no duplicacy
# Unordered 
#  here we use {} to contain set

s = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
print(s)
print(type(s))

emptyset = set()
print(emptyset)

# Unique
multivalueset = {1,2,2,2,5,5,5,1,1,1}
print(multivalueset)

# Unordered
# print(multivalueset[1]) TypeError: 'set' object is not subscriptable

# Set function

# Add
number = {1,2,3,4,5}
number.add(6)
number.add(5)
print(number)

# remove
number = {1,2,3,4,5}
number.remove(5)
# number.remove(5) KeyError: 5
print(number)

# discard
number.discard(4)
number.discard(4)
print(number)

# Set Operations

a = {1,2,3,4,5,6}
b = {5,6,7,8,9}

print(a | b) #union
print(a & b) #intersection
print(a - b) #difference
print(b - a) #difference
c = [3,2,1,7,9]
print("*****************")
print(a.union(c))
print("*****************")


List = "Shopping bag (values are changable)"
Tuple = "Locked Box(Fixed values)"
Set = "Unique Collection (no duplicacy)"

