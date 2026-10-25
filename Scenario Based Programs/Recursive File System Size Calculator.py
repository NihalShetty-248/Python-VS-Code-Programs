"""Recursive File System Size Calculator
Task: Compute total size of all files in 'file_system' recursively."""


def file_size(file_dict):
    if isinstance(file_dict, (int, float)):
        return file_dict
    else:
        total_size = 0
        for i in file_dict.values():
            total_size += file_size(i)
        return total_size


file_system = eval(input("Enter file system: "))
print(f"Total Size: {file_size(file_system)} KB")
