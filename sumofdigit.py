a = int(input("A ="))
sum = 0
while a > 0:
    sum += a % 10
    a //= 10
print("Sum of digits:", sum)