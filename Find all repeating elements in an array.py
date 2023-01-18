arr= [1,1,2,3,4,4,5,2,5]
n=len(arr)

# With the help of hashing-Dictionary
dict={}
for i in arr:
    if not i in dict.keys():
        dict.update({i:1})        
    else: 
        dict.update({i:dict[i]+1})
        

for i in dict.items():
    if i[1]>1:
        print(i)
print(dict)
        
        
# Sorting

arr.sort()
print(arr)
for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        print(arr[i])
        


    