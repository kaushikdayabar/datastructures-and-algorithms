def quick_sort(arr,low,high):

    if low<high:
        pi=partition(arr,low,high)
        
        quick_sort(arr,low,pi-1)

        quick_sort(arr,pi+1,high)

        return arr


def partition(arr,low,high):

    n=high+1

    i=low-1
    
    for j in range(low,n):
        if arr[j]<=arr[high]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    return i        
     
            

print("list the numbers")
l=list(map(int,input().split()))

print("the sorted array")
print(quick_sort(l,0,len(l)-1))
