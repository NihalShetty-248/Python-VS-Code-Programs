"""College Email Id Analyzer
The program accepts an Email Id as an input and
checks whether it is valid or not based on the given criteria
    It should contain @
    It should ends with .edu
    It should not contain spaces
It also counts the number of characters before @"""

email = input("Enter Email Id: ")
symbol_check = domain_check = space_check = False

if "@" in email:
    symbol_check = True
    print("Contains @: Yes")
    pos = email.find("@")
    length = len(email[:pos])
else:
    print("Contains @: No")
    length = 0

if email.endswith(".edu"):
    domain_check = True
    print("Ends with .edu: Yes")
else:
    print("Ends with .edu: No")

if " " not in email:
    space_check = True
    print("Contains space: No")
else:
    print("Contains space: Yes")

print(f"The number of characters before @: {length}")

if symbol_check and domain_check and space_check:
    print("Email ID is valid")
else:
    print("Email ID is invalid")
