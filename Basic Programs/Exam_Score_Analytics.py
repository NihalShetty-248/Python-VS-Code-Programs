"""This program takes a score list as input and does the following tasks:
1. Prints the highest score
2. Prints lowest score
3. Prints class average
4. Prints a filtered list of passing scores (>70)"""

scores = eval(input("Enter score list: "))

print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Class average: {sum(scores)/len(scores)}")
print(f"Filtered list of passing scores: {[x for x in scores if x>=70]}")
