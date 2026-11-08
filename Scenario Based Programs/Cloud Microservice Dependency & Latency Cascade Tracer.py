"""Cloud Microservice Dependency & Latency Cascade Tracer

Problem Description
In a cloud architecture, an API request to a gateway microservice triggers downstream calls to other microservices.
Service metadata is stored in a dictionary where each key is a 'service_name' and its value is a tuple
'(local_latency_ms, [list_of_downstream_services])'.

The system must recursively compute the critical path latency
(maximum cumulative latency from the root service to any leaf service),
collect the unique set of all services touched during the call,
and apply dynamic environment overhead modifiers passed via '**env_modifiers'.

Modular Design Requirements:
1. 'parse_topology(raw_lines)': Builds and returns '(topology_dict, latency_array)' where 'topology_dict' is '{service_name: (latency_int, downstream_list)}' and 'latency_array' is an 'array.array("i")' of all base latencies.

2. 'trace_execution(service, topology, visited_set)': A recursive function that adds 'service' to 'visited_set' (call-by-reference mutation) and returns the maximum cumulative latency ('int') starting from 'service'.

3. 'run_diagnostics(root_service, raw_lines, **env_modifiers)': Coordinates parsing, tracing, and modifier summation, then prints the diagnostic report.

Output Format
- Line 1: 'Root Service: <Root> | Base Topology Avg Latency: <Avg> ms' (rounded to 1 decimal place).
- Line 2: 'Services Touched (<Count>): <Sorted_List_of_Visited_Services>'
- Line 3: 'Critical Path Base Latency: <Base_Critical_Ms> ms'
- Line 4: 'Total Adjusted Latency (with modifiers): <Final_Ms> ms'

The code also contains test cases which need to be executed with the code seperately
"""

import array


def parse_topology(raw_lines):
    latency_array = array.array("i", [])
    topology_dict = {}
    for data in raw_lines:
        split_list = data.split("|")
        service, latency, downstream_list = (
            split_list[0].strip(),
            int(split_list[1].strip()),
            [x.strip() for x in split_list[2].split(",")],
        )
        latency_array.append(latency)
        topology_dict[service] = (latency, downstream_list)
    return topology_dict, latency_array


def trace_execution(service, topology, visited_set=[], sub_visited=[]):
    topology_dict, latency_array = parse_topology(topology)
    max_latency = 0
    if service not in visited_set:
        visited_set.append(service)
    max_latency += topology_dict[service][0]
    sub_lst = []
    latency_lst = []
    if topology_dict[service][1] != ["NONE"]:
        sub_lst.extend(topology_dict[service][1])

    visited_set.extend(sub_lst)

    for sub_service in sub_lst:
        pass_lst, latency, pass_array = trace_execution(
            sub_service, topology, visited_set, sub_visited
        )
        latency_lst.append(latency)

    visited_set.extend(sub_visited)
    duplicate_lst = visited_set.copy()
    visited_set = []
    for i in duplicate_lst:
        if i not in visited_set:
            visited_set.append(i)
    visited_set.reverse()
    if latency_lst:
        max_latency += max(latency_lst)

    return visited_set, max_latency, latency_array


def run_diagnostics(root_service, raw_lines, **env_modifiers):
    visited_set, max_latency, latency_array = trace_execution(root_service, raw_lines)
    avg_latency = sum(latency_array) / len(latency_array)
    services_touched = len(visited_set)
    modifier_latency = sum(env_modifiers.values())
    print(
        f"Root Service: {root_service} | Base Topology Avg Latency: {round(avg_latency,1)} ms"
    )
    print(f"Services Touched ({services_touched}): {(visited_set)}")
    print(f"Critical Path Base Latency: {max_latency} ms")
    print(f"Total Adjusted Latency (with modifiers): {max_latency+modifier_latency} ms")


"""# --- Problem 4: Test Case 1 ---
import io
from contextlib import redirect_stdout

topology_lines_tc1 = [
    "API_GW | 20 | AUTH_SVC,ORDER_SVC",
    "AUTH_SVC | 35 | USER_DB",
    "ORDER_SVC | 50 | USER_DB,PAYMENT_GW",
    "USER_DB | 15 | NONE",
    "PAYMENT_GW | 120 | NONE",
]

buf = io.StringIO()
with redirect_stdout(buf):
    run_diagnostics("API_GW", topology_lines_tc1, network_jitter=12, tls_handshake=8)
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "Root Service: API_GW | Base Topology Avg Latency: 48.0 ms\n"
    "Services Touched (5): ['PAYMENT_GW', 'USER_DB', 'ORDER_SVC', 'AUTH_SVC', 'API_GW']\n"
    "Critical Path Base Latency: 190 ms\n"
    "Total Adjusted Latency (with modifiers): 210 ms"
)
assert (
    actual_out == expected_out
), f"Test Case 1 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 4 - Test Case 1 Passed!")"""


"""# --- Problem 4: Test Case 2 ---
import io
from contextlib import redirect_stdout

topology_lines_tc2 = [
    "WEB_APP | 10 | CACHE_SVC",
    "CACHE_SVC | 5 | NONE",
    "BATCH_WORKER | 200 | ANALYTICS_DB",
    "ANALYTICS_DB | 100 | NONE",
]

buf = io.StringIO()
with redirect_stdout(buf):
    run_diagnostics("WEB_APP", topology_lines_tc2, proxy_delay=5)
actual_out = buf.getvalue().strip()
print(actual_out)

expected_out = (
    "Root Service: WEB_APP | Base Topology Avg Latency: 78.8 ms\n"
    "Services Touched (2): ['CACHE_SVC', 'WEB_APP']\n"
    "Critical Path Base Latency: 15 ms\n"
    "Total Adjusted Latency (with modifiers): 20 ms"
)
assert (
    actual_out == expected_out
), f"Test Case 2 Failed!\nExpected:\n{expected_out}\n\nGot:\n{actual_out}"
print("\n✅ Problem 4 - Test Case 2 Passed!")"""
