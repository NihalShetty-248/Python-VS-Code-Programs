"""Hostel WiFi Usage Monitor
The following program prints
    total number of intervals
    total study time in minutes
    total entertainment time
    total gaming time
    total messaging/social-media time
    total offline time
    percentage of online time spent on academic activity
    students dominant online activity
    online usage message"""

wifi_usage = input("Enter wifi usage string: ").upper()

# Time for each activity
no_of_intervals = len(wifi_usage)
study = wifi_usage.count("S") * 30
entertainment = wifi_usage.count("E") * 30
gaming = wifi_usage.count("G") * 30
messaging = wifi_usage.count("M") * 30
offline = wifi_usage.count("O") * 30

# Percentage of time spent on academic use
academic_time_percentage = (study / (no_of_intervals * 30)) * 100

print(f"total number of intervals: {no_of_intervals}")
print(f"total study time: {study}")
print(f"total entertainment time: {entertainment}")
print(f"total gaming time: {gaming}")
print(f"total messaging time: {messaging}")
print(f"total offline time: {offline}")
print(f"total study time percentage : {academic_time_percentage}")

# Dominant Activity
time_dict = {
    "Study": study,
    "Entertainment": entertainment,
    "Gaming": gaming,
    "Messaging": messaging,
    "Offline": offline,
}
max = 0
cnt = 0

for i in time_dict:
    if time_dict[i] >= max:
        if time_dict[i] != max:
            dominant_activity = i
            max = time_dict[i]
        else:
            print("No clear dominant activity")
            break
else:
    print(f"Dominant activity: {dominant_activity}")

# Online Usage Message
if academic_time_percentage >= 50:
    print("Excellent academic usage")
elif 30 <= academic_time_percentage <= 49:
    print("Balanced usage")
else:
    print("Needs attention")
