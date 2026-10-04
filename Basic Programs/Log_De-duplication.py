"""This program takes a server-log as input
and returns a list of server-log with the duplicate items deleted"""

server_log = eval(input("Enter serverlog as list: "))
print(f"The list after De-duplication: {list(set(server_log))}")
print()

# Alternative method
server_log = eval(input("Enter serverlog as list: "))
deduplicated_list = []

for log in server_log:
    if log not in deduplicated_list:
        deduplicated_list.append(log)
print(f"The list after De-duplication: {deduplicated_list}")
