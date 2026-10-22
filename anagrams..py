n1=input("Enter a First String:")
n2=input("Enter a Second String:")

if sorted(n1)==sorted(n2):
    print("String is anagram")
else:
    print("String is not anagram")