1
23
456
78910

a= int(input("enter a number:"))
i= 0
k= 1
for i in range(1, a+1):
    for j in range(1, i+1):
        print(k, end="")
        k+=1
    print('')    