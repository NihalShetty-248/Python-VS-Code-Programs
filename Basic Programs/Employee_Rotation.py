"""The following program shifts the team schedule to the left by 1 position
that is the first person moves to the end of the line"""

shift_team = ["Alice", "Bob", "Charlie", "Diana"]
print(f"Old shift: {shift_team}")
shift_team.append(shift_team.pop(0))
print(f"New shift: {shift_team}")
