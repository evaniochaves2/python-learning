temperature = float(input("Enter the temperature in Celsius: "))

if temperature < 60:
    print("Safe")
elif 60 <= temperature <= 80:
    print("Warning")
else:
    print("Critical")