#Q1
name=input('Enter Name: ')
print("Hello",name+'!')

#Q2
colour=input('Enter Favourite colour: ')
print('Your favourite colour is',colour)

#Q3
hometown=input('Enter hometown: ')
city=input('Enter current city: ')
print('Your hometown is',hometown)
print('Your current city is',city)

#Q4
animal1=input('Enter first animal: ')
animal2=input('Enter second animal: ')
animal3=input('Enter third animal: ')
print('The three animnals are:',animal1,',',animal2,',',animal3)

#Q5
noun=input('Enter a noun: ')
verb=input('Enter a verb: ')
print('The sentence is:')
print('The',noun,'loves to',verb)

#Q6
f_name=input('Enter first name: ')
l_name=input('Enter last name: ')
print('Your full name is:',f_name,l_name)

#Q7
print('Twinkle Twinkle little star\nHow I wonder what you are')

#Q8
name=input('Enter name of pet: ')
species=input('Enter its species name: ')
print(f'Your {species} is named {name}')

#Q9
job=input('Enter your job title: ')
company=input('Enter company name: ')
print(f'You work as a {job} at {company}')

#Q10
quote=input('Enter your favourite quote: ')
author=input("Enter the quote's author: ")
print(f"{quote}-{author}")

#Q11
n1=int(input('Enter number 1: '))
n2=int(input('Enter number 2: '))
print(f'The sum is {n1+n2}')

#Q12
length=float(input('Enter length of the room in metres: '))
breadth=float(input('Enter breadth of the room in metres: '))
print(f'Area of the room is {length*breadth} sq.m')

#Q13
length=float(input('Enter length of the garden: '))
breadth=float(input('Enter breadth of the garden: '))
print(f'The perimeter of the garden is {2*(length+breadth)} m')

#Q14
c_temp=float(input('Enter temperature in celcius: '))
f_temp=(c_temp*9/5)+32
print(f'The temperature in farenheit is {f_temp} °F')

#Q15
radius=float(input('Enter radius: '))
print(f'Area of the circle is {3.14159*radius*radius}')

#Q16
amt=float(input('Enter total bill amount: '))
no=int(input('Enter number of friends: '))
print(f'Amount each person should pay is {amt/no}')

#Q17
amt=float(input('Enter total bill amount: '))
tip=int(input('Enter tip percentage: '))
print(f'The total amount to be paid is Rs. {amt+amt*(tip)/100}')

#Q18
p=float(input('Enter principal amount: '))
r=float(input('Enter rate of interest:'))
t=float(input('Enter time in years: '))
print(f'The simple interest is {(p*r*t)/100} ')

#Q19
wt=float(input('Enter weight in kg: '))
ht=float(input('Enter height in m: '))
print(f'The body mass index is {wt/(ht**2)}')

#Q20
days=int(input('Enter number of days: '))
hr=days*24
min=hr*60
sec=min*60
print(f'{days} days={hr} hours={min} minutes={sec} seconds')

#Q21
dollars=float(input('Enter amt in dollars: '))
conv=float(input('Enter current conversion rate: '))
euro=dollars*conv
print(f'${dollars}={euro} euros')

#Q22
mile=float(input('Enter distance in miles: '))
effi=float(input('Enter efficiency in terms of MPG: '))
print(f'The total gallons of gas needed is {mile/effi}')

#Q23
mile=float(input('Enter distance in miles: '))
effi=float(input('Enter efficiency in terms of MPG: '))
print(f'The total gallons of gas needed is {mile/effi}')
price=float(input('Enter price of 1 gallon of gas: '))
print(f'Total cos of gas is {(mile/effi)*price}')

#Q24
no=int(input('Enter a 2 digit number: '))
print(f'The tens place is {no//10}',f'The ones place is {no%10}',sep='\n')

#Q25
cupcakes=int(input('Enter number of cupcakes: '))
print(f'The no of boxes you will get is {cupcakes//6}',f'The no of leftover cupcakes is {cupcakes%6}',sep='\n')

#Q26
m1=float(input('Enter marks of first subject: '))
m2=float(input('Enter marks of second subject: '))
m3=float(input('Enter marks of third subject: '))
print(f"The student's average is {(m1+m2+m3)/3}")

#Q27
amt=float(input('Enter price without tax: '))
tax=float(input('Enter tax as percentage:'))
print(f'The final price including taxes is {amt+(amt*tax/100)}')

#Q28
b_year=int(input('Enter birth year: '))
c_year=int(input('Enter current year: '))
print(f'Your approximate age is {c_year-b_year}')

#Q29
r=float(input('Enter radius of cylinder in cm: '))
h=float(input('Enter height of cylinder in cm: '))
print(f'The volume of cylinder is {3.14159*(r**2)*h} cu.cm')

#Q30
sec=int(input('Enter no of seconds: '))
print(f'The no of minutes is {sec//60}',f'The no of remaining seconds is {sec%60}')

#Q31
word=input('Enter a word: ')
print(f'The word printed 5 times is: {5*word}')

#Q32
word1=input('Enter word 1: ')
word2=input('Enter word 2: ')
print(word1+word2)
print(word1+''+word2)

#Q33
chr=input('Enter a character: ')+' '
print(f'The 5x5 square made from {chr} is:\n')
print(f'{5*chr}\n{5*chr}\n{5*chr}\n{5*chr}\n{5*chr}')

#Q34
f_name=input('Enter first name: ')
m_name=input('Enter middle name: ')
l_name=input('Enter last name: ')
print('Your full name is')
print(f_name,m_name,l_name,sep='\t')

#Q35
str=input('Enter a string: ')
int=int(input('Enter a number: '))
print(f'The string {str} repeated {int} times is {str*int}')

#36
name=input('Enter store name: ')
print('Decorative reciept is:\n')
print(20*'=',name,20*'=',sep='\n')

#Q37
word1=input('Enter word 1: ')
word2=input('Enter word 2: ')
word3=input('Enter word 3: ')
print('The fake website is:','www.'+word1+word2+word3+'.com')

#Q38
sym=input('Enter a symbol: ')
n=int(input('Enter a number: '))
print(f'The border is {sym*n}')

#Q39
s_name=input('Enter street name: ')
city=input("Enter city's name: ")
pin_code=input('Enter pincode: ')
var=s_name+'\n'+city+'\n'+pin_code
print(var)

#Q40
prefix=input('Enter a prefix: ')
word=input('Enter a root word: ')
suffix=input('Enter a suffix: ')
print(f'The new word is {prefix+word+suffix}')

#Q41
Float=float(input('Enter a float: '))
print('The float with its decimal part truncated is:',int(Float))

#Q42
Int=int(input('Enter an integer: '))
print('The int converted to float is:',float(Int))

#Q43
int=int(input('Enter a number: '))
str=str(int)
print('Your number is '+str)

#Q44
int_str=input('Enter a number: ')
print(f'Multiplication by 3 as a string is {3*int_str}')
print(f'Multiplication by 3 as an integer is {int(int_str)*3}')

#Q45
num=int(input('Enter a number: '))
print(f'The number in terms of boolean is {bool(num)}')

#Q46
n1=int(input('Enter 1st number: '))
n2=int(input('Enter 2nd number: '))
print(n1>n2)

#Q47
age=int(input('Enter your age: '))
print('You are eligible to vote:',age>=18)

#Q48
password=input('Enter password: ')
print('Password Verification:',password=='secret123')

#Q49
num=int(input('Enter a positive integer: '))
print('Even: True\tOdd:False')
print(num%2==0)

#Q50
num1=int(input('Enter 1st number: '))
num2=int(input('Enter 2nd number: '))
print(f'1st number not equal to 2nd number: {num1!=num2}')

#Q51
height=float(input('Enter height in cm: '))
print('Your height is between 150cm and 200cm:',150<=height<=200)

#Q52
Bool=int(input('Enter 0/1: '))
print(f'Bool value of {Bool} is {bool(Bool)}')
print(f'Not of {Bool} is {not(Bool)}')

#Q53
age=int(input('Enter age: '))
ques=int(input('Are you a student[1-Yes 0-No]? '))
print(f'Are you eligible for discount: {age>=65 or ques==1}')

#Q54
s_range=int(input('Enter starting range number: '))
e_range=int(input('Enter ending range number: '))
t_number=int(input('Enter test number: '))
print(f'Is test number strictly between the given range: {s_range<t_number<e_range}')

#Q55
food1=input('Enter first favourite food: ')
food2=input('Enter second favourite food: ')
print(f'Are the 2 foods the same: {food1==food2}')