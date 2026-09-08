"""Battery Health Monitor
Takes the battery readings of the laptop as a string and print
    The first battery reading.
    The final battery reading.
    The total battery drop.
    The largest drop between two consecutive readings.
    The intervals are classified as:
        Normal
        Fast Discharge
        Sudden Discharge
    The overall battery behavior should be classified as:
        Healthy
        Needs Observation
        Suspicious"""


def drop_type(x):
    if x <= 10:
        return "Normal"
    elif 11 <= x <= 20:
        return "Fast Discharge"
    else:
        return "Sudden Discharge"


def battery_behaviour(x):
    if max_drop <= 10:
        return "Healthy"
    elif 11 <= max_drop <= 20:
        return "Needs Observation"
    else:
        return "Suspicious"


battery_reading = input("Enter battery readings seperated by spaces: ")
battery_list = battery_reading.split()

first_reading = battery_list[0]
last_reading = battery_list[-1]
total_drop = eval(first_reading + "-" + last_reading)

print(f"First battery reading: {first_reading}")
print(f"Last battery reading: {last_reading}")
print(f"Total battery drop: {total_drop}")

# Finding largest drop
i = 0
max_drop = 0
while i < (len(battery_list) - 1):
    print(
        f"{battery_list[i]}-{battery_list[i+1]}: {drop_type(eval(battery_list[i] +'-'+ battery_list[i+1]))}"
    )
    if eval(battery_list[i] + "-" + battery_list[i + 1]) > max_drop:
        max_drop = eval(battery_list[i] + "-" + battery_list[i + 1])
    i += 1

print(f"Largest drop among intervals: {max_drop}")
print(f"Overall battery health: {battery_behaviour(max_drop)}")
