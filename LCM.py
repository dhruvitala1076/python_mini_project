n=int(input('Enter first number:'))
m= int(input('Enter  second number'))
d=[]
c=[]
for i in range(1,11):
    a=n*i
    b=m*i
    d.append(a)
    c.append(b)

for num in d:
    if num in c:
        print('LCM',num)
        break    
