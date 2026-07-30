for station in range(1, 11):
    print(f"Inspecting station {station}")
    if station == 7:
        print(f"Emergency stop activated at station {station}! Stopping inspection.")
        break
    print(f"Station {station} is clear.")

