arr=[4,5,1,4,1]
n=5

# If element is already visited- means it has duplicates
visited=[False]*n
counter=[0]*n

for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j] and visited[j]==False:
            visited[j]=True
            counter[i]+=1

print(counter)
ans=[]
for i in range(len(counter)):
    if counter[i]==0:
        # print(arr[i])
        ans.append(arr[i])
print(ans)
    

# for i in range(n-1):
#  visited[i]=1
#  for j in range(i+1,n):
#     if arr[i]==arr[j] and visited[j]==0:
#         visited[i]+=1
#         visited[j]+=1
#     else:
#         j+=1
#     # print(visited)
         
        

# for i in range(len(visited)):
#     if visited[i]==1:
#         print(arr[i])

# # print(arr)
        
    