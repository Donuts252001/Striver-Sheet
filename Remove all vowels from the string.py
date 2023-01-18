str='hdgduag'
vowels=['a','e','i','o','u']
for i in str:
    if i in vowels:
        print(i)
        str=str.replace(i,'')

print(str)

