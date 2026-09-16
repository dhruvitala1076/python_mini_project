n=int(input("Enter a Number:"))
R=0
while n>0:
    sum=n%10
    R=R*10+sum
    n//=10
    print(R)

