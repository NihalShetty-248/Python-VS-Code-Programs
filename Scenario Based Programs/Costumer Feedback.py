"""Customer Feedback Analyzer
This program accepts feedback from the user and finds the total number of
    consonants
    vowels
    spaces"""

feedback = input("Enter feedback: ")
vowel = consonant = space = 0

for i in feedback:
    if i in "aeiouAEIOU":
        vowel += 1
    elif i.isalpha():
        consonant += 1
    elif i.isspace():
        space += 1

print(f"Total number of Consonants: {consonant}")
print(f"Total number of Vowels: {vowel}")
print(f"Total number of Spaces: {space}")
