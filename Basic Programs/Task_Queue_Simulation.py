"""This program implements First-In-First-Out (FIFO) Queue to perform the following tasks
1. Add a new task 'Task-4' at the end of the list
2. Process the first two tasks one-by-one
3. print the processed task and the remaining queue"""

queue = ["Task_1", "Task_2", "Task_3"]

print('Adding "Task_4" to queue...')
queue.append("Task_4")

print(f"Processed: {queue.pop(0)}")
print(f"Processed: {queue.pop(0)}")

print(f"Remaining Tasks: {queue}")
