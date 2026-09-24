"""Message Censoring System
This program is used to censor a statement. It take a sentence and a word as input
and replaces each occurrence of the word with **** to censor it"""

sentence = input("Enter a sentence: ")
word = input("Enter the Word: ")

if sentence == "" or word == "":
    print("Empty String!!")

else:
    censored_sentence = sentence.replace(word, "****")
    print(f"The censored sentence is:\n {censored_sentence}")
