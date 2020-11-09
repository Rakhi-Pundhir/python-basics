def prime(n):
    if(n==2):
        return 'Prime'
    for j in range(2,n):
        if (n%j==0):
            return 'Non Prime'
        else:
            return 'Prime'
l=int(input("Enter the limit"))        
res=[(i,prime(i))for i in range(2,l+1)]
print(res)
        
