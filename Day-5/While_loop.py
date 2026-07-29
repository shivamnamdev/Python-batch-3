# # print("print this statement")
# # print("print this statement")
# # print("print this statement")
# # print("print this statement")
# # print("print this statement")
# # print("print this statement")
# # print("print this statement")
# # print("print this statement")


# # # while <condition>:
# # #     this statement would work
    
# # a = "running"
# # while a:
# #     a = input()
# #     print("print this statement")    
    
    
# # value = 4
# # while value:
# #     value = int(input())
# #     print(f"you've given integer value {value}")
       
       
# # # print "print this statement" 5 times      

# # i = 0 # initialise
# # while i < 5: # check whether the condition met - my counter should be less than the target(5)
# #     print("print this statement")
# #     i = i + 1 # increment the counter
    
    
# # i = 1
# # while i <= 10:
# #     if i != 2:
# #         print(i)
# #     i = i + 1    
    
# # ATM Program
b = 1234
d = 5000
i = 1

while i <= 3:
    pin = int(input("Enter your PIN: "))

    if pin == b:
        print("This is a valid pin")
        c = int(input("enter  the amount:"))  
        if c> 3000:
            print("Exceeded daily limit")
        elif c <= d-300:
            if c%100 == 0:
                print("Transaction is successful")
                print("remaining balance is:", d-c)
                transaction = input("Do you want to continue the transaction (yes/no):")
                if transaction == "yes":
                    continue
                else:
                    break    
            else:
                print("enter in multiple of 100")
        else:
            print("Insufficient balance")
    else :
        print("This is an invalid pin")
        print(f"Attempt left {3-i}")
        i = i + 1   
        
        
        
# Write a program to print 1 to 10 

i = 0

while True:
    i = i + 1
    #agar 5 aata ha to loop ruk jaaye
    if i == 5 or i == 2:
        continue
    if i == 11:
        break
    print(i)  


# 5 students k name lene h
# check karna h ki unke naam me vowel aata h ya nahi
# agar aata h to naam print krdo otherwise jane do
a = 1
while a <=5:
    name = input("give name of the student: ")
    a = a+1
    if "a" in name or "e" in name or "i" in name or "o" in name or "u" in name:
       print(name) 
       
outer = 1

while outer <= 3:
    inner = 4       
    while inner <= 6:
        print(inner)
        inner = inner + 1
    print(outer)    
    outer += 1 
             

stringvalue = "abcde"
i = 0
while i <= len(stringvalue)-1:
    print(stringvalue[i])
    i += 1