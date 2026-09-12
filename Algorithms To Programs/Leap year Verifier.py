year = int(input("Enter year: "))
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Non Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Non Leap Year")
