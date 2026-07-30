motor_speed = float(input("Enter the motor speed in RPM: "))

if motor_speed == 0:
    print("Motor is stopped")
elif 1 <= motor_speed <= 999:
    print("Low speed")
elif 1000 <= motor_speed <= 3000:
    print("Operating normally")
else:
    print("Overspeed.")