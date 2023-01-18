arr=[1,1,2,3,3]
n=len(arr)
# def swap(i,j):
#     temp=i
#     i=j
#     j=temp
#     return (i,j)
i=0
for j in range(1,n):
        if(arr[i]!=arr[j]):
            i+=1
            arr[i]=arr[j] 
                
print(arr)
        
        
        
        