arr=[1,2,3,4,5]
n=5

def findsum(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return arr[0]+findsum(arr[1:])

print(findsum(arr))