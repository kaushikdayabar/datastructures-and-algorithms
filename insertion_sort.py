def insertion_sort(arr):
    n=len(arr)

    for i in range(n):
        mn=i
        for j in range(i-1,-1,-1):
            if arr[j]>arr[i]:
                mn-=1
        if mn!=i:
            arr=arr[:mn]+[arr.pop(i)]+arr[mn:]   
    return arr

print(insertion_sort([3,5,6,67,45,342,4]))
