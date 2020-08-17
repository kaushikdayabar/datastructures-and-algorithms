def count_sort(arr,exp):
    l=[0]*10
    n=len(arr)
    ca=[] 
    for i in range(n):
        rmd=arr[i]//exp
        ca.append(rmd%10) 
      
    for i in range(10):
        if i in ca:
            l[i]+=ca.count(i)         #frequency of each digit       
          
    s=[]        
    for i in range(10):
        s.append(sum(l[:i])+l[i])     #summation of the previous frequencies
    
    re=[]
    for i in ca:
        re.append(0)                   
    j=0
    for i in range(n):
        if ca[i]==0:
            re[j]=arr[i]            #numbers with lesser number of digits are put first
            j+=1
        
    for i in range(n):
        if ca[i]!=0:
            re[s[ca[i]]-1]=arr[i]
            s[ca[i]]-=1
            
    return re


def radix_sort(arr):
    m=max(arr)

    exp=1
    while m//exp>0:
        arr=count_sort(arr,exp)             
        exp*=10                          #to dostinct between one's place,ten's place etc
    return arr        
print(radix_sort([1,7,1,12,5,43,56,2,113]))
