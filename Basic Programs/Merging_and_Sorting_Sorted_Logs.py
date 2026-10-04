"""This program takes 2 log batches as input and does the following
1. combines the 2 log batches
2. sorts this combined list in chronological order"""

log_batch1 = [102, 105, 110]
log_batch2 = [101, 107, 115]
combined_log_batch = sorted(log_batch1 + log_batch2)

print(f"Combined log batch is: {combined_log_batch}")
