"""Word Guessing Game
This game give sthe user 5 chances to guess the secret word. If the user guessess it
then the game ends. Else it shows the number of turns left and gives another chance.
If the user fails to guess it then it shows the secret word"""

secret_word = "python"

for i in range(1, 6):
    guess = input("Enter your guess: ")
    if guess == secret_word:
        print("CORRECT!! You won")
        break
    else:
        print("INCORRECT!! Try Again")
        print(f"You have {5-i} chances left")
        print()

else:
    print(f"The secret word is {secret_word}")
