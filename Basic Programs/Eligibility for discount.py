age = int(input("Enter age: "))
ques = int(input("Are you a student[1-Yes 0-No]? "))
print(f"Are you eligible for discount: {age>=65 or ques==1}")
