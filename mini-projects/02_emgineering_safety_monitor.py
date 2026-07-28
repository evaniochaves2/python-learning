temperature = float(input("Enter the temperature in Celsius: "))
pressure = float(input("Enter the pressure in kPa: "))

if temperature > 90 and pressure > 120:
    print("Emergency Shutdown")
elif temperature > 80 or pressure > 100:
    print("Warning")
else:
    print("System Normal")