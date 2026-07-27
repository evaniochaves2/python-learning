print("=== Equipment Health Calculator ===")

equipment = input("Equipment name: ")

hours = int(input("Operating hours: "))

failures = int(input("Failures this month: "))

temperature = float(input("Temperature °C: "))

vibration = float(input("Vibration mm/s: "))


score = 100

# Add your calculations here
if failures > 0:
    score -= failures * 5
if hours > 1000:
    score -= (hours - 1000) * 0.1
if temperature > 80:
    score -= 10
if vibration > 5:
    score -= 15

score = max(score, 0) # Ensure score doesn't go below 0

print("\n--- Equipment Report ---")

print(f"Equipment: {equipment}")

print(f"Reliability Score: {score}%")

if score >= 90:
    recommendation = "Continue normal operation."
elif score >= 70:
    recommendation = "Schedule an inspection."
else:
    recommendation = "Perform maintenance immediately."

print("\nRecommendation:")
print(recommendation)