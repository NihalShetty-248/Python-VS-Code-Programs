"""In-Place Inventory Sanitizer vs. Audit Copy
Task: Audit negative stock without mutation, then sanitize in-place."""


def remove_negatives(lst):
    Error_lst = [x for x in lst if x < 0]
    return Error_lst


def sanitize_lst(lst):
    sanitized_list = [x if x > 0 else 0 for x in lst]
    return sanitized_list


lst = eval(input("Enter audit list: "))
print(f"Error list: {remove_negatives(lst)}")
print(f"Sanitized list: {sanitize_lst(lst)}")
