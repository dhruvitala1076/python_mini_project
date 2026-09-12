1
21
321
4321
54321

a = int(input("enter a number:"))
i=0
for i in range(1 , a+1):
    for j in range(i, 0, -1):
        print(j, end="")
    print("")    