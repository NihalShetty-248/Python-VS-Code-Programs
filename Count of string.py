'''This program prints takes a string as input and print
 the number of vowels, consonants, alphabets and digits
 If the string is not in title case it converts into title case
 If there are repeating characters then it displays 'There are repeating characters'''

string=input('Enter string: ')
alphabet=0
digit=0
vowels=0
consonants=0

#Counts the number of alphabets, digits, vowels and consonants
for i in string:
    if i.isalpha():
        alphabet+=1
    elif i.isdigit():
        digit+=1
    if i in 'aeiouAEIOU':
        vowels+=1
    else:
        consonants+=1

print(f'Number of alphabets {alphabet}')
print(f'Number of digits {digit}')
print(f'Number of vowels {vowels}')
print(f'Number of consonants {consonants}')

#Checking if text in title case
if string.istitle():
    print('String in title case')
else:
    print(f'String not in title case. converting to title case... \n{string.title()} \n')

#Checking if any characters are repeating
for i in string:
    if string.count(i)>1:
        print('Repeating Chracters are there in the string')
        break
else:
    print('No repeating Characters are there in the string')
