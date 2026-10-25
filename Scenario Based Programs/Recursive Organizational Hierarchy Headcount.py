"""Recursive Organizational Hierarchy Headcount
Task: Count total team members in 'org_chart' recursively."""


def member_count(team_dict):
    if isinstance(team_dict, str):
        return 1
    else:
        total = 0
        for i in team_dict.values():
            if isinstance(i, list):
                for j in i:
                    total += member_count(j)
            else:
                total += member_count(i)
        return total


team_dict = eval(input("Enter team dictionary: "))
print(f"Total number of members: {member_count(team_dict)}")
