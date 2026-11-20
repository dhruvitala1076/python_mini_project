n1=int(input("enter a number:"))
n2=int(input("Enter a Second Number:"))
m= input("enter a operator(+,/,-,*):")
if m=='+':
    print("addition",n1+n2)
elif m=='-':
    print("subtraction",n1-n2)
elif m=='/':
    if n2==0:
        print("cannot divisible by zero")   
    else:
         print("division",n1/n2) 
else:
    print("multiplaction",n1*n2)
