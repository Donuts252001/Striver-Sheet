exp='(a+b)'

# arr=[(1,5),(2,3),(4,2),(5,1),(2,4)] 
# arr = [20, 15, 26, 2, 98, 6]
# temp=arr.copy()
# temp.sort()
# dict={}
# j=1
# for i in temp:
#     if i not in dict:
#         dict[i]=j
#     j+=1
    
# for i in arr:
#     print(dict[i])
# print(dict)
    

str='abcdefghij gooogle micrrrrrosoft'
dict={}
list=[]
counter=0
for i in range(len(str)):
    if str[i]==' ' or i==len(str)-1:
        counter+=1
        list.append([max(dict.values()),counter])
        dict={}
    else:
        if str[i] not in dict:
            dict[str[i]]=1
        else:
           dict[str[i]] +=1

    print(dict)
    
print(list)

    