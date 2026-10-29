Str=input('Enter a String:')
max_count=0

for i in Str:
    if Str.count(i)>max_count:
        max_count=Str.count(i)
        ans= i
print(ans)    
