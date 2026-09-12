a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a >= b and a >= c:
    print("a is greater")
elif b >= a and b >= c:
    print("b is greater")
else:
    print("c is greater")
