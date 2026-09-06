# List is mutable collection of data-types separated by commas
#  In python we use [] square brackets to define a list
l = [1,2,3,4,"first","second","third",True, False, 14.2, 16.8,98.2,[3,2,1],{1,2,3},(1,6,2),{"key":"value"}]
print(l)
print(type(l))


# How to initialise a list
mylist1 = [10,20,30]
mylist2 = list()
mylist3 = []

print(mylist2)


# How to access items in list
mylist4 = [10,20,30,"abc",[1,2,3,"xyz"]]
print(mylist4[1])
print(mylist4[-1])

print(mylist4[3][1])
print(mylist4[4][3][1])

# Range of indexes

print(mylist4[:3])
print(mylist4[-2:])


# item data type

print(type(mylist4[0]))
print(type(mylist4[3]))
print(type(mylist4[4]))


# Concept 3: Mutable(Changable) vs Immutable(not changable)
# List is mutable

fruits = ["banana","orange", "mango","guava","pineapple",10]
print(fruits)
fruits[1] = "Cherry"
print(fruits)
# fruits[4][3] = "a" TypeError: 'str' object does not support item assignment
# fruits[5][1] = 35 TypeError: 'int' object does not support item assignment

# Item iteration

fruits = ["banana", "orange", "mango","guava","pineapple"]

for f in fruits:
    print(f)
    
for f in fruits:
    for i in f:
        print(i,end="")
    print()        
        
# Membership Operator

for f in fruits:
    if "o" in f:
        print("a is present")
    else:
        print("no there is no a") 
        
        
# How to check the length of a list

print(len(fruits))  

# Adding an element

# append
mylist = ["banana", "orange","mango","guava","pineapple"]
mylist.append("melon")
print(mylist)

# insert
mylist.insert(2,"cherry")
print(mylist)

# extend
mylist2 = [1,2,3]
mylist.extend(mylist2)
print("Extend example")
print(mylist)

# Remove element
mylist = ["banana", "orange","mango","guava","pineapple"]

# using pop
lastindex = mylist.pop() # ["banana", "orange","mango","guava"]
print(mylist)
print(lastindex)

mylist.pop(1) # ["banana","mango","guava"]
print(mylist)

mylist2 = ["cherry", "apple","mango", "dragon fruit"]
del mylist2[2]
print(mylist2)

# del mylist2[6] # IndexError: list assignment index out of range

# using clear function

mylist2.clear()
print(mylist2)

# Copying the list
# using list()
mylist = ["banana", "orange","mango","guava","pineapple"]

mylist4 = list(mylist)
print(mylist4)

mylist4.append("Dragon fruit")
print(mylist)
# ---------------------
# using assignment operator
mylist5 = mylist
mylist.append("Dragon fruit")

print(mylist5)
# ---------------------
# using copy
mylist6 = mylist.copy()
print(mylist6)
mylist6.append("Kiwi")
print(mylist)


# Operators
# + for concatenation
# * for repeatation

list1 = ["a","b","c"]
list1_a = [1,2,3]
list2 = [1,2,3]

# + operation
list3 = list1 + list2
print(list3)
list_3_a = list1_a + list2
print(list_3_a)
# [["a","b","c"],[1,2,3]]
# ["a","b","c",1,2,3]
# * operation
list4 = list1 * 2
print(list4)

# list5 = list1 * list2 TypeError: can't multiply sequence by non-int of type 'list'
# print(list5)


marks = [75,72,88,71,51]
out_of = len(marks)*100
total = 0
for mark in marks:
    total +=mark
    
percentage = total/out_of * 100
print(round(percentage,6),"%" )   