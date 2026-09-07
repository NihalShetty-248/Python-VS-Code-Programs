'''Prints the longest word in sentence'''

sentence=input('Enter a sentence: ')
size=0
word=''

#Creating a list of words present in the sentence
sentence_list=sentence.split()

#Finding the longest word
for i in sentence_list:
    if len(i)>=size:
        if len(i)==size:
            word=word+', '+i
        else:
            size=len(i)
            word=i

print(f'The longest words in the above sentence is/are: {word}')