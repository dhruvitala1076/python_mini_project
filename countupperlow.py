n= input("Enter a Name:")
upper=0
lower=0

for i in n:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1

print("Capital:",upper)     
print("Small:",lower)   