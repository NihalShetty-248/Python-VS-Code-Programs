"""Smart Retry Exponential Backoff Calculator
Task: Compute wait time on retry attempt 5 recursively."""


def wait_time(attempt, base=2):
    if attempt <= 1:
        return base
    else:
        time = base * wait_time(attempt - 1, base)
        return time


attempt = int(input("Enter number of attempts: "))
base = int(input("Enter base: "))

print(f"Wait time: {wait_time(attempt,base)}")
