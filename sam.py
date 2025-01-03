from datetime import datetime

# Get current date and time
current_time = datetime.now()

# Format the date and time as "DD/MM/YYYY , HH/MM/SS"
formatted_time = str(current_time.strftime("%d/%m/%Y , %H/%M/%S"))

# Print the formatted time
print(formatted_time)
