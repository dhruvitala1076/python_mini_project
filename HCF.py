n=int(input('Enter first number:'))
m= int(input('Enter  second number:'))


for i in range(1, min(n,m)+1):
    if n%i==0 and m%i==0:
       HCF=i
print(HCF)       