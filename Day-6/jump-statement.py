       
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