from datetime import datetime

# Get the current date and time
current_time = datetime.now()

# Define another date and time (you can customize this)
other_time = datetime(2025, 4, 1, 12, 30, 0)  # Example: April 1, 2025, 12:30 PM

# Calculate the time difference
time_difference = other_time - current_time

# Display the result
print(f"Time difference: {time_difference}")