n=int(input("Enter a Number:"))
N=n
R=0
while n>0:
    sum=n%10
    R=R*10+sum
    n//=10
print(R)
if R==N:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")