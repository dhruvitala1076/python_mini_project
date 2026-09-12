1
32
654
10987
a= int(input("enter a number:"))
i=0
k= 1
for i in range(1, a+1):
    k=i*(i+1)//2
    for j in range(i, 0, -1):
        print(k, end=" ")
        k-=1
    print('')    