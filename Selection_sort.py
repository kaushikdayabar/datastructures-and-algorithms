def selection_sort(arr):
    n=len(arr)
    
    for i in range(n):
        mn=i
        for j in range(i,n):
            if arr[mn]>arr[j]:
                mn=j
               
        arr[i],arr[mn]=arr[mn],arr[i]
        
    return arr    
    
    
print(selection_sort([12,3,234,56,21,45,6,7]))        
