"""Cyber-Security Log Forensics & Threat Scoring Engine

Problem Description
A Security Operations Center (SOC) analyzes firewall access logs to detect multi-vector attacks. Each log line is a string: "IP_ADDRESS | ENDPOINT | STATUS_CODE | RESPONSE_BYTES".

The engine groups activity by IP address inside a dictionary where each IP maps to:
- "endpoints": A 'set' of unique endpoints accessed.
- "failures": A 'list' of '(endpoint, status_code)' tuples representing failed requests ('status_code >= 400').
- "bytes": An 'array.array("i")' storing 'RESPONSE_BYTES' for all requests from that IP.

Modular Design Requirements:
1. 'ingest_log_entry(raw_log, ip_registry)': Parses the string and mutates 'ip_registry' (Call by Reference) by updating the IP's endpoint set, failed request tuple list, and byte array.
2. 'compute_threat_score(ip_data, *, restricted_endpoints, **weights)': Keyword-only 'restricted_endpoints' (a 'set') and arbitrary keyword '**weights' ('fail_weight', 'restricted_weight', 'volume_threshold'). Computes score = '(num_failures * fail_weight) + (num_restricted_hits * restricted_weight) + (50 if total_bytes > volume_threshold else 0)' where 'num_restricted_hits' is the size of the intersection between unique endpoints accessed and 'restricted_endpoints'.
3. 'generate_forensic_report(raw_logs, restricted_endpoints, **weights)': Ingests all logs, evaluates all IPs, and prints the leaderboard sorted by 'threat_score' descending.

Output Format
- Print the forensic leaderboard sorted by Threat Score (highest to lowest):
  Rank <R>: <IP_ADDRESS> | Threat Score: <Score> | Unique Endpoints: <Count> | Failed Attempts: <Fail_Count> | Total Bytes: <Bytes>

The program also contains test cases which need to be executed seperately
"""

import array as arr


def ingest_log_entry(raw_log, ip_registry):
    log_lst = raw_log.split("|")
    endpoints = set()
    failures = []
    byte_arr = arr.array("i", [])

    ip_address = log_lst[0].strip()
    end_pt = log_lst[1].strip()
    status_code = int(log_lst[2].strip())
    response_bytes = int(log_lst[3].strip())

    endpoints.add(end_pt)

    if status_code >= 400:
        failures.append(status_code)

    byte_arr.append(response_bytes)

    if ip_address not in ip_registry:
        ip_registry[ip_address] = [endpoints, failures, byte_arr]

    else:
        ip_registry[ip_address][0] |= endpoints
        ip_registry[ip_address][1] += failures
        ip_registry[ip_address][2] += byte_arr

    return ip_registry


def compute_threat_score(ip_data, *, restricted_endpoints, **weights):
    endpoints = ip_data[0]
    failures = ip_data[1]
    byte = ip_data[2]

    fail_score = len(failures) * weights["fail_weight"]
    restricted_score = (
        len(endpoints & restricted_endpoints) * weights["restricted_weight"]
    )

    if sum(byte) > weights["volume_threshold"]:
        threat_score = fail_score + restricted_score + 50

    else:
        threat_score = fail_score + restricted_score

    return threat_score


def generate_forensic_report(raw_logs, restricted_endpoints, **weights):
    ip_registry = {}
    for ip in raw_logs:
        ip_registry = ingest_log_entry(ip, ip_registry)

    score_dict = {}
    for ip_data in ip_registry:
        threat_score = compute_threat_score(
            ip_registry[ip_data], restricted_endpoints=restricted_endpoints, **weights
        )
        score_dict[ip_data] = threat_score

    sorted_ip = sorted(score_dict, reverse=True, key=score_dict.get)

    rank = 1
    for ip in sorted_ip:
        endpoints = ip_registry[ip][0]
        failures = ip_registry[ip][1]
        byte = ip_registry[ip][2]
        print(
            f"Rank {rank}: {ip} | Threat Score: {score_dict[ip]} | Unique Endpoints: {len(endpoints)} | Failed Attempts: {len(failures)} | Total Bytes: {sum(byte)}"
        )
        rank += 1


"""# --- Problem 6: Test Case 1 ---
import io
from contextlib import redirect_stdout

restricted_tc1 = {"/admin", "/env", "/db_dump"}
logs_tc1 = [
    "192.168.1.50 | /login | 401 | 512",
    "10.0.0.12 | /home | 200 | 3200",
    "192.168.1.50 | /admin | 403 | 256",
    "192.168.1.50 | /env | 404 | 128",
    "10.0.0.12 | /products | 200 | 2400",
    "192.168.1.50 | /login | 401 | 512",
]

buf = io.StringIO()
with redirect_stdout(buf):
    generate_forensic_report(
        logs_tc1,
        restricted_tc1,
        fail_weight=10,
        restricted_weight=25,
        volume_threshold=5000,
    )
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "Rank 1: 192.168.1.50 | Threat Score: 90 | Unique Endpoints: 3 | Failed Attempts: 4 | Total Bytes: 1408\n"
    "Rank 2: 10.0.0.12 | Threat Score: 50 | Unique Endpoints: 2 | Failed Attempts: 0 | Total Bytes: 5600"
)
assert (
    actual_out == expected_out
), f"Test Case 1 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 6 - Test Case 1 Passed!")"""


"""# --- Problem 6: Test Case 2 ---
import io
from contextlib import redirect_stdout

restricted_tc2 = {"/config", "/keys"}
logs_tc2 = [
    "172.16.0.9 | /keys | 200 | 8000",
    "172.16.0.9 | /config | 500 | 1200",
    "172.16.0.2 | /index | 200 | 400",
]

buf = io.StringIO()
with redirect_stdout(buf):
    generate_forensic_report(
        logs_tc2,
        restricted_tc2,
        fail_weight=15,
        restricted_weight=30,
        volume_threshold=5000,
    )
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "Rank 1: 172.16.0.9 | Threat Score: 125 | Unique Endpoints: 2 | Failed Attempts: 1 | Total Bytes: 9200\n"
    "Rank 2: 172.16.0.2 | Threat Score: 0 | Unique Endpoints: 1 | Failed Attempts: 0 | Total Bytes: 400"
)
assert (
    actual_out == expected_out
), f"Test Case 2 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 6 - Test Case 2 Passed!")"""
