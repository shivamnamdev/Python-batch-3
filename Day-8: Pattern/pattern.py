#  *
#  **
#  ***
#  ****
#  *****

# for i in range(1,6):
#     print("*"* i)


#  *****
#  ****
#  ***
#  **
#  *

# for i in range(5,0,-1):
#     print("8"* i)
    
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5    

# for j in range (2,7):    
#     for i in range(1,j):
#         print(i, end=" ")
#     print()      
    
# j = 1, i = 1 -> 1

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
# 16 17 18 19 20 21

# count = 1
# for i in range(1,11):
#     for j in range(1,i+1):
#        print(count, end = " ")
#        count += 1 
#     print()
    
    
    
# Program to print:

#         *
#       * *
#     * * *
#   * * * *
# * * * * *    

# for i in range(1,6):
#     for j in range(4,0,-1):
#         print(" ",end=' ')
#     for k in range(1,i+1):
#         print("*",end=' ')    
#     print()
    
# max = 5
# count = 1
# for i in range(1,max):
#     for j in range(1,max-i):
#         print(" ",end='')
#     for k in range(1,i+1):
#         print(count,end='')
#         count+=1    
#     print()    
    
# max = 6
# for i in range(1,max):
#     print(" "*(max-i),"*"*i)
 
#  Program to print:
#     *
#    * *
#   * * *
#  * * * *
 
 
# max = 5
# for i in range(1,max):
#     for j in range(max-i,0,-1):
#         print(" ",end='')
#     for k in range(1,i+1):
#         print("*",end=' ')  
#     print()    
 
 
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# row wise increment ho rha h
# jitni baar outer loop chl rha h utni baar ek increment hojata h  

# puri row k liye ek hi number print hona h

for i in range(1,6):
    for j in range(1,i+1):
       print(i, end=" ") 
    print()  
  
  

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 

# column wise increment ho rha h
# hr ek line me increment hota jayega
# puri row me increment hote jana h or print hona h

for i in range(1,6):
    for j in range(1,i+1):
       print(j, end=" ")     
    print()


#     *
#    **
#   ***
#  ****
# *****       
outer_max=6
for i in range(1,outer_max):
    for k in range(1,outer_max-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print("*", end=" ")
    print()       
    
# outer loop -> 1 to number of lines + 1
# inner loop(pattern) -> 1 to current_outer_loop + 1 -> i + 1
# inner loop(spacing) -> 1 to outer_loop_max_value - i -> max - i











def greet():
    print("working")

def greet1(callback):
    print("another")
    callback()


greet1(greet)


def outer():
    def inner():
        print("Inside")

    return inner


a = outer()
a()