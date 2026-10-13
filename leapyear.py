n =int(input("Enter a Year:"))

if n%400==0:
    print(f"{n} is Leap Year")
elif n%100==0:
    print(f"{n} is not Leap Year")
elif n%4==0:
    print(f"{n} is Leap Year")
else:
    print(f"{n} is not Leap Year")
