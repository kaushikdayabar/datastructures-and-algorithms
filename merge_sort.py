def mergesort(arr):
    if len(arr)>1:
        m=len(arr)//2
        l=arr[:m]
        r=arr[m:]
        
    
        l=mergesort(l)
        r=mergesort(r)

        i,j,re=0,0,[]
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                re.append(l[i])
                i+=1
            else:
                re.append(r[j])
                j+=1
                
        while i<len(l):
            re.append(l[i])
            i+=1
            
        while j<len(r):
            re.append(r[j])
            j+=1
        
        return re
    else:
        return arr
print(mergesort([5,6,12,11,34,4,3,2,1]))            
