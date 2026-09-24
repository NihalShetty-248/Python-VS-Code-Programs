"""Password Strength Verifier
This program takes a password as an input and
checks whether it satisfies the security requirement
    At least 8 characters.
    Contains at least one uppercase letter.
    Contains at least one lowercase letter.
    Contains at least one digit."""

password = input("Enter password: ")
len_check = upper_check = lower_check = digit_check = False

if len(password) >= 8:
    print("Length requirement: Satisfied")
    len_check = True
else:
    print("Length requirement: Not Satisfied")

for i in password:
    if i.isupper():
        upper_check = True
    if i.islower():
        lower_check = True
    if i.isdigit():
        digit_check = True

if upper_check:
    print("Uppercase requirement: Satisfied")
else:
    print("Uppercase requirement: Not Satisfied")

if lower_check:
    print("Lowercase requirement: Satisfied")
else:
    print("Lowercase requirement: Not Satisfied")

if digit_check:
    print("Digit requirement: Satisfied")
else:
    print("Digit requirement: Not Satisfied")

if len_check and upper_check and lower_check and digit_check:
    print("Password is Valid")
else:
    print("Password is Invalid")
