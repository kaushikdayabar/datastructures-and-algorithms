def bubble_Sort(arr):
    n=len(arr)
    for i in range(n):
        f=0
        for j in range(1,n):
            if arr[j-1]>arr[j]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                f=1
          
        if f==0:
            break
    return arr

print(bubble_Sort([5,54,3,5,345,45,54]))
        
        
