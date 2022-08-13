array= [1,2,3,4,6]
n=4

def avg(array):
    if len(array)==1:
        return array[0]
    else:
        return array[-1]+avg(array[:-1])

print(avg(array)/n)