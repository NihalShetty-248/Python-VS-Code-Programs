#1. Calculate sum of 2 number
num1=int(input('Enter 1st number: '))
num2=int(input('Enter 2nd number: '))
result=num1+num2
print('The sum is',result)

#2. Find are of rectangle
length=float(input('Enter length of rectangle: '))
breadth=float(input('Enter breadth of rectangle: '))
area=length*breadth
print('Area of rectangle is:',area)

#3. Convert Celcius to Farenheit
celcius=float(input('Enter temperature in celcius: '))
farenheit=(9/5)*celcius+32
print('The temperature in farenheit is:',farenheit)

#4. Calculate simple interest
p=float(input('Enter principal amount: '))
r=float(input('Enter rate of interest: '))
t=int(input('Enter time: '))
si=(p*r*t)/100
print('The simple interest is:',si)

#5. Swap two numbers
x=int(input('Enter num1: '))
y=int(input('Enter num2: '))
print(f'x is {x}\ny is {y}\n')
temp=x
x=y
y=temp
print(f'After swapping:\nx is {x}\ny is {y}')

#6. Average of 3 numbers
A=int(input('Enter 1st number: '))
B=int(input('Enter 2nd number: '))
C=int(input('Enter 3rd number: '))
sum=A+B+C
avg=sum/3
print(f'The average is {avg}')

#7. Calculate circumference of circle
radius=int(input('Enter radius of circle: '))
circumference=2*3.14*radius
print(f'The circumference of the circle is {circumference}')

#8. Calculate volume of cube
side=float(input('Enter side of cube: '))
volume=side**3
print(f'Volume of cube is {volume}')

#9. Converting kilometers to miles
km=float(input('Enter distance in kilomters: '))
miles=km*0.62
print(f'The distance in miles is {miles}')

#10. Calculating Gross salary
basic=float(input('Enter basic: '))
hra=float(input('Enter HRA: '))
da=float(input('Enter DA: '))
gross=basic+hra+da
print(f'The gross salary is {gross}')

#11. Checking whether a number is even or odd
n=int(input('Enter a number: '))
rem=n%2
if rem==0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')

#12. To print largest of two numbers
a=int(input('Enter a: '))
b=int(input('Enter b: '))
if a>b:
    print('a is greater')
elif b>a:
    print('b is greater')
else:
    print('Both are equal')

#13. Checking voting eligibility
age=int(input('Enter age: '))
if age>=18:
    print('Eligible')
else:
    print('Not eligible')

#14. To determine whether a number is zero, positive or negative
n=int(input('Entr a number: '))
if n>0:
    print('Positive')
elif n<0:
    print('Negative')
else:
    print('Zero')

#15. To check whether a year is leap year or not
year=int(input('Enter year: '))
if year%400==0:
    print('Leap Year')
elif year%100==0:
    print('Non Leap Year')
elif year%4==0:
    print('Leap Year')
else:
    print('Non Leap Year')

#16. To check if adent is pass or fail
marks=float(input('Enter marks: '))
if marks>=40:
    print('Pass')
else:
    print('Fail')

#17. To find largest of 3 numbers
a=int(input('Enter a: '))
b=int(input('Enter b: '))
c=int(input('Enter c: '))
if a>=b and a>=c:
    print('a is greater')
elif b>=a and b>=c:
    print('b is greater')
else:
    print('c is greater')

#18. To check whether an alphabet is vowel or constant
char=input('Enter an alphabet: ')
if char in 'aeiouAEIOU':
    print('Vowel')
else:
    print('Constant')

#19. To categorize triangles
x=float(input('Enter side 1: '))
y=float(input('Enter side 2: '))
z=float(input('Enter side 3: '))
if x==y and y==z:
    print('Equilateral')
elif x==y or y==z or z==x:
    print('Isosceles')
else:
    print('scalene')

#20. Ticket price based on age
age=int(input('Enter age: '))
if age<12:
    price=5
else:
    price=10
print(f'The price is {price}')

#21. To print numbers from 1 to n
n=int(input('Enter a number: '))
cnt=1
print(f'Numbers from 1 to {n} are:')
while cnt<=n:
    print(cnt)
    cnt+=1

#22. To calculate n!
n=int(input('Enter a number: '))
factorial=1
i=1
while i<=n:
    factorial*=i
    i+=1
print(f'{n}! is {factorial}')

#23. To print multiplication table of a number n
num=int(input('Enter a number: '))
n=int(input('Enter until which number you need the multiplication table: '))
print(f'The multiplication table of {n} is: ')
i=1
while i<=n:
    print(f'{i}x{num}={i*num}')
    i+=1

#24. Sum of first n natural numbers
n=int(input('Enter a number n: '))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(f'The sum of first {n} natural numbers is {sum}')

#25. To reverse a number
n=int(input('Enter a number: '))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(f'The reversed number is {rev}')

#26. To check whether a number is prime or not
n=int(input('Enter a number: '))
isPrime=True
i=2
while i<=n/2:
    if n%i==0:
        isPrime=False
        break
    i+=1
if isPrime:
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')

#27. To print Fibonacci series upto nth number
n=int(input('Enter number of digits upto which fibonacci series needs to be printed: '))
a=0
b=1
i=1
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1

#28. To count total number of digits in a Number
n=int(input('Enter a number: '))
cnt=0
while n>0:
    cnt+=1
    n=n//10
print(f'The above number has {cnt} digits')

#29. To find sum of digits of a number
n=int(input('Enter a number: '))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(f'The sum of digits is {sum}')

#30. To check whether a number is palindrome
num=int(input('Enter a number: '))
n=num
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if rev==num:
    print('Palindrome')
else:
    print('Not a Palindrome')

#31. Perimeter of square
side=float(input('Enter side of square: '))
print(f'The perimeter of square is {4*side}')

#32. Convert Minutes to Seconds
min=int(input('Enter time in minutes: '))
sec=min*60
print(f'The time in seconds is {sec}')

#33. Area of circle
r=int(input('Enter radius of circle: '))
area=3.14*(r)**2
print(f'The area of the circle is {area}')

#34. Calculate BMI
height=float(input('Enter height in metres: '))
weight=float(input('Enter weight in kg: '))
bmi=weight/(height)**2
print(f'The BMI is {bmi}')

#35. USD to Euros
usd=float(input('Enter amount in usd: '))
euro=usd*0.86
print(f'the amount in euros is {euro}')

#36. Calculate average speed
dist=float(input('Enter total distance: '))
time=float(input('Enter total time: '))
speed=dist/time
print(f'The average speed is {speed}')

#37. To find 3rd angle of triangle
a1=float(input('Enter 1st angle: '))
a2=float(input('Enter 2nd angle: '))
a3=180-(a1+a2)
print(f'The third angle is {a3}')

#38. To calculate net price after discount
price=float(input('Enter price: '))
disc=float(input('Enter discount: '))
net_price=price-(price*(disc/100))
print(f'The net price is {net_price}')

#39. Convert days to hours
day=int(input('Enter number of days: '))
hour =day*24
print(f'The number of hours is {hour}')

#40. To calculate distance between 2 points
x1,y1=eval(input('Enter initial coordinates: '))
x2,y2=eval(input('Enter final coordinates: '))
dist=((x2-x1)**2+(y2-y1)**2)**(1/2)
print(f'The distance is {dist}')

#41. To check if a number is a multiple of 5
n=int(input('Enter a number: '))
if n%5==0:
    print('Multiple of 5')
else:
    print('Not a multiple of 5')

#42. To determine pass/fail based on grade
grade=float(input('Enter grade: '))
if grade>=40:
    print('Pass')
else:
    print('Fail')

#43. To check whether a triangle is valid
a=float(input('Enter side1: '))
b=float(input('Enter side2: '))
c=float(input('Enter side3: '))
if a+b>c and b+c>a and c+a>b:
    print('Valid Triangle')
else:
    print('Invalid Triangle')

#44. To calculate profit or loss
cp=float(input('Enter cost price: '))
sp=float(input('Enter sale price: '))
if sp>cp:
    print(f'Profit of Rs.{sp-cp}')
else:
    print(f'Loss of Rs.{cp-sp}')

#45. To determine if a character is an alphabet
char=input('Enter a chracter: ')
if char.isalpha():
    print(f'{char} is an alphabet')
else:
    print(f'{char} is not an alphabet')

#46. To check eligibility for Senior citizen discount
age=int(input('Enter age: '))
if age>=60:
    discount=50
else:
    discount=10
print(f'The discount is {discount}%')

#47. To find quadrant of a coordinate
x,y=eval(input('Enter coordinates: '))
if x>0 and y>0:
    print('First Quadrant')
elif x<0 and y>0:
    print('Second Quadrant')
elif x<0 and y<0:
    print('Third Quadrant')
else:
    print('Fourth Quadrant')

#48. To categorize temperature as hot or cold
temp=float(input('Enter temperature: '))
if temp>=30:
    print('Hot')
else:
    print('Cold')

#49. To check if a number is divisible by 3 and 7
num=int(input('Enter a number: '))
if num%3==0 and num%7==0:
    print(f'{num} is divisible by 3 and 7')
else:
    print(f'{num} is not divisible by 3 and 7')

#50. To check eligibility for driving license
age=int(input('Enter age: '))
if age>=18:
    print('Eligible')
else:
    print('Not eligible')

#51. Print even numbers from 1 to 20
i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1

#52. Sum of odd numbers upto n
n=int(input('Enter a number: '))
sum=0
i=1
while i<=n:
    sum+=i
    i+=2
print(f'The sum of odd numbers upto {n} is {sum}')

#53. To find power of a number
a=int(input('Enter base number: '))
b=int(input('Enter exponent number: '))
res=1
i=1
while i<=b:
    res*=a
    i+=1
print(f'{a}^{b} is equal to {res}')

#54. To find LCM of 2 numbers
num1=int(input('Enter first number: '))
num2=int(input('Enter second number :'))
i=max(num1,num2)
while True:
    if i%num1==0 and i%num2==0:
        print(f'LCM is {i}')
        break
    i+=1

#55. To find GCD of 2 numbers
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
i=1
while i<=min(num1,num2):
    if num1%i==0 and num2%i==0:
        gcd=i
    i+=1
print(f'The GCD of {num1} and {num2} is {gcd}')

#56. To print prime numbers upto n
n=int(input('Enter number: '))
isprime=True
print(f'The prime numbers upto {n} are:')
i=2
while i<=n:
    j=2
    while j<i:
        if i%j==0:
            isprime=False  
        j+=1
    if isprime:
        print(i)
    isprime=True
    i+=1

#57. To find factors of n
n=int(input('Enter a number: '))
i=1
print(f'The factors of {n} are:')
while i<=n:
    if n%i==0:
        print(i)
    i+=1

#58. To calculate sum of series 1+ 1/2 +1/3 ... + 1/n
n=int(input('Enter a number(>0): '))
i=1
sum=0
while i<=n:
    sum+=(1/i)
    i+=1
print(f'The sum of series is {sum}')

#59. To check whether a number is a perfect number
n=int(input('Enter a number: '))
i=1
sum=0
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')

#60. To check whether a number is an Armstrong number
num=int(input('Enter a number: '))
sum=0
n=num
pow=len(str(num))
while n>0:
    digit=n%10
    sum+=digit**pow
    n=n//10
if sum==num:
    print(f'{num} is an Armstrong number')
else:
    print(f'{num} is not an Armstrong number')