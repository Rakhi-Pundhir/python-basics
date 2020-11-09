def listu(l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2
print(listu([3,3,6,8,8,9]))
