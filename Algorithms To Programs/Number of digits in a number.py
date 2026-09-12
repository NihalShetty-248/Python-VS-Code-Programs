n = int(input("Enter a number: "))
cnt = 0
while n > 0:
    cnt += 1
    n = n // 10
print(f"The above number has {cnt} digits")
