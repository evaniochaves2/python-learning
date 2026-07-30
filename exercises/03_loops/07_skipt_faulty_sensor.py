for sensor in range(1, 11):
    if sensor == 5:
        print(f"Skipping faulty sensor {sensor}")
        continue
    print(f"Inspecting sensor {sensor}")