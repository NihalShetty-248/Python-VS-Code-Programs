"""Problem 2: IoT Environmental Sensor Network Analyzer

Problem Description
An agricultural monitoring station collects hourly temperature readings across multiple farm zones.
Each sensor reading arrives as a raw string "ZONE_ID#TIMESTAMP#TEMP_CELSIUS".
Because sensors occasionally transmit duplicate packets at the exact same timestamp, a set of "(zone_id, timestamp)"
    tuples must be maintained to ignore duplicate transmissions.
Valid temperature readings for each zone must be stored in a compact single-precision floating-point array ("array.array("f")").
The system must flag zones that breach safety thresholds and compute summary statistics.

Modular Design Requirements:
1. "parse_packet(packet_str)": Strips whitespace and splits the string into a tuple "(zone_id, timestamp_int, temp_float)".
2. "ingest_stream(raw_packets)": Filters duplicates using a set of "(zone_id, timestamp)" tuples and returns "(zone_dict, dropped_count)"
    where "zone_dict" maps each "zone_id" to an "array.array("f")" of valid temperatures.
3. "analyze_zone(zone_id, temp_array, /, *, min_safe=15.0, max_safe=35.0)": Uses positional-only parameters for "zone_id" and "temp_array"
    and keyword-only parameters for safety bounds. Returns a tuple "(avg_temp, min_temp, max_temp, breach_count)".
4. "generate_sensor_report(raw_packets, min_safe=15.0, max_safe=35.0)": Coordinates the functions and prints the formatted output.

Output Format
- For each zone (in alphabetical order of "ZONE_ID"), print:
  "<ZONE_ID> -> Count: <Valid_Count> | Avg: <Avg>C | Range: (<Min>C, <Max>C) | Breaches: <Breach_Count>" (All floats formatted to 1 decimal place using ":.1f").
- On the final line, print: 'Duplicate Packets Dropped: <dropped_count>'

This code also contains 2 test cases that need to be executed seperately"""

import array


def parse_packet(packet_str):
    stripped_packet_str = packet_str.strip()
    packet_lst = stripped_packet_str.split("#")
    packet_tpl = (packet_lst[0], eval(packet_lst[1]), eval(packet_lst[2]))
    return packet_tpl


def ingest_stream(raw_packets):
    global unique_tpl, zone_dict, dropped_count
    zone_id, timestamp, temp_float = parse_packet(raw_packets)
    temp_array = array.array("f", [])
    if (zone_id, timestamp) in unique_tpl:
        dropped_count += 1
    else:
        if zone_id not in zone_dict:
            temp_array.append(temp_float)
            zone_dict[zone_id] = temp_array
        else:
            zone_dict[zone_id].append(temp_float)
        unique_tpl += ((zone_id, timestamp),)
    return zone_dict, dropped_count


def analyze_zone(zone_id, temp_array, /, *, min_safe=15.0, max_safe=35.0):
    avg_temp = sum(set(temp_array)) / len(set(temp_array))
    min_temp = min(temp_array)
    max_temp = max(temp_array)
    breach_count = 0
    for temp in temp_array:
        if temp < min_safe or temp > max_safe:
            breach_count += 1
    return avg_temp, min_temp, max_temp, breach_count


def generate_sensor_report(raw_packets, min_safe=15.0, max_safe=35.0):
    for raw in raw_packets:
        zone_dict, drop_count = ingest_stream(raw)
    ordered_zone_dict = {key: zone_dict[key] for key in sorted(zone_dict)}
    for zone in ordered_zone_dict:
        avg_temp, min_temp, max_temp, breach_count = analyze_zone(
            zone, ordered_zone_dict[zone], min_safe=min_safe, max_safe=max_safe
        )
        print(
            f"{zone} -> Count: {len(set(ordered_zone_dict[zone]))} | Avg: {avg_temp:.1f}C | Range: ({min_temp}C, {max_temp}C) | Breaches: {breach_count}"
        )
    print(f"Duplicate Packets Dropped: {dropped_count}")


unique_tpl = ()
zone_dict = {}
dropped_count = 0

"""# --- Problem 2: Test Case 1 ---
import io
from contextlib import redirect_stdout

packets_tc1 = [
    "ZONE_B#1001#25.0",
    "ZONE_A#1001#16.5",
    "ZONE_B#1001#25.0",
    "ZONE_A#1002#20.0",
    "ZONE_B#1002#34.5",
    "ZONE_A#1003#19.0",
    "ZONE_A#1002#20.0",
]

assert parse_packet("ZONE_A#1001#16.5") == ("ZONE_A", 1001, 16.5), "parse_packet failed"

buf = io.StringIO()
with redirect_stdout(buf):
    generate_sensor_report(packets_tc1, min_safe=18.0, max_safe=32.0)
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "ZONE_A -> Count: 3 | Avg: 18.5C | Range: (16.5C, 20.0C) | Breaches: 1\n"
    "ZONE_B -> Count: 2 | Avg: 29.8C | Range: (25.0C, 34.5C) | Breaches: 1\n"
    "Duplicate Packets Dropped: 2"
)
assert (
    actual_out == expected_out
), f"Test Case 1 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 2 - Test Case 1 Passed!")"""


"""# --- Problem 2: Test Case 2 ---
import io
from contextlib import redirect_stdout

packets_tc2 = [
    "GREENHOUSE_1#2001#22.0",
    "GREENHOUSE_1#2002#24.0",
    "GREENHOUSE_1#2001#22.0",
]

buf = io.StringIO()
with redirect_stdout(buf):
    generate_sensor_report(packets_tc2, min_safe=15.0, max_safe=30.0)
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "GREENHOUSE_1 -> Count: 2 | Avg: 23.0C | Range: (22.0C, 24.0C) | Breaches: 0\n"
    "Duplicate Packets Dropped: 1"
)
assert (
    actual_out == expected_out
), f"Test Case 2 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 2 - Test Case 2 Passed!")"""
