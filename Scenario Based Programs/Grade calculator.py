"""Grade Calculator
This programs take 5 subject marks as input, calculate the average and returns the grade
    90-100: A
    75-89: B
    60-74: C
    40-59: D
    Below 40: Fail"""

mark_sum = 0
for i in range(5):
    mark = float(input(f"Enter marks of subject {i+1}: "))
    mark_sum += mark

avg = mark_sum / 5

print(f"Total Marks: {mark_sum}")
print(f"Average Marks: {avg}")
print("Grade: ", end="")

if avg < 40:
    print("Fail")
elif 40 <= avg <= 59:
    print("D")
elif 60 <= avg <= 74:
    print("C")
elif 75 <= avg <= 89:
    print("B")
elif 90 <= avg <= 100:
    print("A")
