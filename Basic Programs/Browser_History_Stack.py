"""This program implements Last-In-First-Out stack to execute the following tasks:
1. Add new web-page 'Profile'
2. Go to previous web-page twice and print each step
3. Print the current web-page"""

history = ["home_page", "dashboard", "settings"]

print("Went to new web-page 'Profile'")
history.append("Profile")
print(f"New history is: {history}")

print(f"Went back from: {history.pop()}")
print(f"Went back from: {history.pop()}")

print(f"Current web-page is : {history[-1]}")
