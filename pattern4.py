1
10
101
1010
10101

a= int(input("enter a number:"))
i =0

for i in range(1, a+1):
    for j in range(1, i+1):
        print(j%2, end='')
    print("")    
