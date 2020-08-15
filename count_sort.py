def count_sort(arr):
    l=[0,0,0,0,0,0,0,0,0,0]
     
    for i in range(10):
        if i in arr:
            l[i]+=arr.count(i)
            
    s=[]        
    for i in range(10):
        s.append(sum(l[:i])+l[i])

    re=[]
    for i in arr:
        re.append(0)
        
    for i in arr:
        re[s[i]-1]=i
        s[i]-=1
    return re        
print(count_sort([1,4,1,2,7,5,2]))
