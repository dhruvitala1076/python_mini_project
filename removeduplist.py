list=[2,4,2,5,7,2,45,56]
result=[]

for i in list:
    if i not in result:
        result.append(i)
print(result)        