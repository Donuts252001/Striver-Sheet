arr=[10,5,10,15,10,20]
n=6

visited=[False]*n
count=[1]*n

for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j] and visited[j]==False:
            count[i]+=1
            visited[j]=True
            count[j]=0
                   
        
print(count,visited)


# #######################################
# dict={}
# for i in range(n):
#     if arr[i] not in dict:
#         dict[arr[i]]=1
#     else:
#         dict[arr[i]]+=1
# print(dict)

# ans=[0]*n
# for i in range(n):
#     if arr[i] in dict:
#         ans[i]=dict[arr[i]]
#         dict[arr[i]]=0
# print(ans)
        
    
    
        