n=5
arr= [5,4,3,2,1]
i=0
j=n-1

def swap(i,j):
    if i>j:
        print(i,j)
        return arr
    else:
        print(i,j)
        temp=arr[j]
        arr[j]=arr[i]
        arr[i]=temp
        i+=1
        j-=1
        swap(i,j)
    return arr
    
print(swap(i,j))
    

