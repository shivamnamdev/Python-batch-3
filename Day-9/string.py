# String: stream of data enclosed within "" or ''

# Concept 1: Creation of string
var = "123"
var2 = '123'

print(type(var))
print(type(var2))

var3 = "123"
print(var3)
var4 = "ergsdhytyreyhrtsysrtedy#$%^%@$&$#^2463564d. sdgfg. sfdg sdrg "

var3 = "new value"
print(var3)

# Concept 2: Accessing the character/item in the string 
print(var3[2]) #w
print(var3[5]) #a

# Negative indexing
print(var3[-7]) #w
print(var3[-4]) #a

# print(var3[-10]) IndexError: string index out of range

# Concept 3: Mutable(Changable) vs Immutable(not changable)
# String is immutable datatype

# var3[2] = "l" TypeError: 'str' object does not support item assignment

var = "Working"
print(ord(var[0]))
print(chr(87))

var = "Not Working"
print(ord(var[0]))
print(chr(87))
print(chr(78))


# Concept 5: Operators + *
# + -> Concatenation
# * -> Repeatation

# Concept 6: String Slicing
# string[start: stop(excluding): step]
var = "This is my string variable"

print(var[9]) #y
print(var[0:4]) # This
print(var[5:9]) # is m
print(var[11:17]) #string
print(var[8:26]) # my string variable
print(var[8:]) # my string variable
print(var[0:7]) # This is
print(var[:7]) # This is

# Negative Indexing
print(var[-3:]) #ble

# Steppings
print(var[::2]) #Ti sm tigvral
print(var[::3]) #Tssytnvil
print(var[::-1]) #elbairav gnirts ym si sihT

# Practice
print(var[-20:-22:-1]) #si
print(var[6:4:-1]) #si
print(var[9:7:-1])

# Concept: String Functions

var = "making"
p = var.capitalize()
print(var) #making
print(p) #Making

var = "Tushar is a good candidate"
print(var.capitalize()) #Tushar is a good candidate
print(var.count("a")) # 4
print(var.replace('a','o')) #Tushor is o good condidote
print(var) # Tushar is a good candidate
print(var.upper())
print(var.lower())
print(var.index("a",0))


Final_var = "Hakuna Matata"
Final_var = Final_var[0] + "o" + Final_var[2:5] + "o" + Final_var[6:8]+ "o"
print(Final_var)

# Concept 7: Parsing a string
var = "This is my string"
for i in var:
    print(i)