n=int(input("Enter a Number:"))
R=0
while n>0:
    sum=n%10
    R=R*10+sum
    n//=10
if R==R:
    print("Number is Palindrome Number")
else:
    print("Number is Not Palidrome Number")    