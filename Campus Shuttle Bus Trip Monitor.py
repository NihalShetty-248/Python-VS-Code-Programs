"""Campus Shuttle Bus Trip Monitor
The program takes the speed of the bus at regular intervals as input and prints
    The number of Very Slow readings.
    The number of Normal readings.
    The number of Fast readings.
    The number of Overspeed readings.
    The average speed.
    The highest speed recorded.
    The number of times the bus was travelling at 50 km/h or more.
    Whether the journey should be flagged for review."""

checkpoints = int(input("Enter the number of checkpoints: "))

# Speed inputs
speed_list = []
for i in range(1, checkpoints + 1):
    speed = int(input(f"Enter speed at checkpoint {i}: ").upper().replace("K", ""))
    speed_list.append(speed)

very_slow, normal, fast, overspeed = 0, 0, 0, 0

for i in speed_list:
    if i <= 30:
        very_slow += 1
    elif 30 < i <= 49:
        normal += 1
    elif 50 <= i <= 59:
        fast += 1
    else:
        overspeed += 1

average_speed = sum(speed_list) / len(speed_list)
max_speed = max(speed_list)

# speed>=50km/hr
cnt = 0
for i in speed_list:
    if i >= 50:
        cnt += 1

print(f"Very Slow readings: {very_slow}")
print(f"Normal readings: {normal}")
print(f"Fast readings: {fast}")
print(f"Overspeed readings: {overspeed}")
print(f"Average speed: {average_speed}K")
print(f"Highest speed recorded: {max_speed}K")
print(f"Number of times bus was travelling at 50 km/h or more: {cnt}")

if overspeed >= 2 or cnt / len(speed_list) >= 40:
    print("Journey should be flagged for review.")
else:
    print("No need to flag for review.")
