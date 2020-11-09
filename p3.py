s=input("Enter string")
c1=0
c2=0
for i in s:
    if(i.isupper()):
        c1=c1+1
    elif(i.islower()):
        c2=c2+1
print("Upper case letters are :",c1)
print("Lower case letters are :",c2)
