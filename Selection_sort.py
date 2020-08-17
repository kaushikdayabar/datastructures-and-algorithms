def selection_sort(arr):
    n=len(arr)
    
    for i in range(n):
        mn=i
        for j in range(i,n):
            if arr[mn]>arr[j]:
                mn=j
               
        swap(mn,i,arr)
        
    return arr    

def swap(a,b,arr):
    t=arr[a]
    arr[a]=arr[b]
    arr[b]=t
    
    
print(selection_sort([12,3,234,56,21,45,6,7]))        
