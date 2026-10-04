"""This program takes the name of participant and their scores in seperate list
and combine them into a consolidated format. This consolidated format
is then ordered in decending order and printed in the form of ranks"""

name = eval(input("Enter name of participants in the form of list: "))
scores = eval(input("Enter scores of each participant in the form of a list: "))

combined_list = list(zip(name, scores))
combined_list.sort(reverse=True, key=lambda x: x[1])

for i in range(1, len(combined_list) + 1):
    print(f"{i}. {combined_list[i-1][0]}:{combined_list[i-1][1]}")

# Alternate method
List = [
    f"{rank}. {name}:{score}" for rank, (name, score) in enumerate(combined_list, 1)
]
for i in List:
    print(i)
