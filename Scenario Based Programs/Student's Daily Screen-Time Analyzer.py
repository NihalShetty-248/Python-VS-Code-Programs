"""Student's Daily Screen-Time Analyzer
The program takes Phone activity as a string input and prints
    Total number of activity events.
    Number of academic events.
    Number of social-media events.
    Number of entertainment events.
    Number of gaming events.
    Number of other events.
    Percentage of events spent on academic work.
    The longest continuous stretch of non-academic activity.
    Sums up the students screen time"""

record = input("Enter today's phone activity record: ").upper()
total_activity = len(record)
academic = record.count("A")
social_media = record.count("S")
entertainment = record.count("E")
gaming = record.count("G")
other = record.count("O")
percentage = (academic / total_activity) * 100

# Longest stretch of non-academic activity
max_len = 0
cnt = 0
i = record.find("A") + 1
while i < total_activity:
    if record[i] == "A" and cnt >= max_len:
        max_len = cnt
    else:
        cnt += 1
    i += 1

print(f"Total number of activity events: {total_activity} ")
print(f"Number of academic events: {academic} ")
print(f"Number of social-media events: {social_media} ")
print(f"Number of entertainment events: {entertainment} ")
print(f"Number of gaming events: {gaming} ")
print(f"Number of other events: {other} ")
print(f"Percentage of events spent on academic work: {percentage} ")
print(f"The longest continuous stretch of non-academic activity: {max_len} ")

# Usage comments
if percentage >= 60:
    print("Excellent academic focus")
elif percentage < 60 and max_len <= 4:
    print("Needs improvement")
elif percentage < 60 and max_len >= 5:
    print("High Distraction period")
