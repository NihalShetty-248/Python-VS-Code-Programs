"""Username Validator
The following program asks the user for his/her username and
checks if it is valid based on the following criteria:
    The username must contain at least 5 characters.
    It must not contain any spaces.
    It must begin with a letter"""

user_name = input("Enter username: ")
length = len(user_name)
valid1 = valid2 = valid3 = False

# Checking if username contains atleast 5 characters
if length >= 5:
    valid1 = True
else:
    print("INVALID!!", "The username is less than 5 characters", sep="\n")

# Checking if it contains spaces
if " " not in user_name:
    valid2 = True
else:
    print("INVALID!!", "The username contains a space", sep="\n")

# Checking if it starts with a letter
if length > 0 and user_name[0].isalpha():
    valid3 = True
else:
    print("INVALID!!", "The username does not start with a letter", sep="\n")

if valid1 and valid2 and valid3:
    print("Username is Valid")
