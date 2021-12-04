l = [5,2,8,6,7]


for i in range(len(l)):
    for  j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]
print(l)            