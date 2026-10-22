n=input("Enter a Number:")

for i in n:
    if i == n[0:1]:
        print(i)
    elif i==n[-1]:
        print(i)