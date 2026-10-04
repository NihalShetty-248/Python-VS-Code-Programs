"""This program takes a list containing registered and checked-in students
and find thise students who checked-in but did not register(gatecrashers)
and find those who were registered but did not check-in(absentees)"""

registered = eval(input("Enter list of registered students: "))
checked_in = eval(input("Enter list of checked-in students: "))

print("Gatecrashers:")
for i in checked_in:
    if i not in registered:
        print(i, end=", ")
print()

print("\nAbsentees:")
for i in registered:
    if i not in checked_in:
        print(i, end=", ")
print()

# Alternate method
gatecrashers_list = [name for name in checked_in if name not in registered]
absentees_list = [name for name in registered if name not in checked_in]

print(f"Gatecrashers: {gatecrashers_list}")
print(f"Absentees: {absentees_list}")
