from datetime import datetime, timedelta
print(".                            THE HERMAN CORP. LTD")
print(".                  72V BATTERY TIME CHARGING PREDICTOR")

percent = float(input("Current Battery %: "))

# Constants
full_time = 240  # minutes for full charge

# Calculate remaining percentage
remaining_percent = 100 - percent

# Minutes left
minutes_left = (remaining_percent / 100) * full_time

# Get current time
now = datetime.now()

# Add remaining time
full_charge_time = now + timedelta(minutes=minutes_left)

# Output
print(f"\n {minutes_left:.2f} minutes left")
print(" Battery will be full at:", full_charge_time.strftime("%H:%M:%S"))