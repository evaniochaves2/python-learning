print("\nStarting automated inspection...\n")

products_checked = 0
skip_count = 0
emergency_stop = False

for product in range(1, 11):
    print(f"Inspecting product {product}...")
    products_checked += 1

    if product == 4:
        print(f"Minor defect detected.\nSkipping product {product}.\n")
        skip_count += 1
        continue

    elif product == 8:
        print(
            "CRITICAL DEFECT DETECTED!"
            f"\nEmergency stop activated at product {product}.\n"
        )
        emergency_stop = True
        break

    print(f"Product {product} passed inspection.\n")

products_inspected = products_checked - skip_count
stop_status = "Yes" if emergency_stop else "No"

print(
    "Inspection Summary\n"
    "------------------"
    f"\nProducts inspected: {products_inspected}"
    f"\nProducts skipped: {skip_count}"
    f"\nEmergency stop: {stop_status}\n"
)