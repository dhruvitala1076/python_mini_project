n=int(input("Enter a Number:"))
R=0
while n>0:
    sum=n%10 #modulus se last digit milta hai
    R=R*10+sum 
    n//=10#floor division se last digit remove hota hai
print(R)

