arr=[10,5,10,15,10,20]
n=6

visited=[False]*n
count=[0]*n

for i in range(0,n):
 if visited[i]==True:
        continue
 else:      
    visited[i]=True
    count[i]+=1

    for j in range(i+1,n):
        if(arr[i]==arr[j] and visited[j]==False):
            visited[j]=True
            count[i]+=1
print(visited,count)
            
            
        
    
    

