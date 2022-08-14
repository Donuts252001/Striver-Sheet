from array import array


arr=[1,2,3,4,5,6,7]
k=2
n=7

def swap(arr,a,b,k):
    for i in range(k):
        temp=arr[a+i]
        arr[a+i]=arr[b+i]
        arr[b+i]=temp
        
def rotate(arr,n,k):
 if k==0 or k==n:
        return arr
 if k==n-k:
  swap(arr,0,n-k,k)      
  return
 elif k<n-k:
     swap(arr,0,n-k,k)
     rotate(arr,k,n-k)
 else:
     swap(arr,0,k,n-k)
     rotate(arr+n-k,2*k-n,k)
 print(arr)

rotate(arr,n,k)
        
    