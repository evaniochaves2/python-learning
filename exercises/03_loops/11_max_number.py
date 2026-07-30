numbers = [15, 8, 42, 3, 27, 19]

max_number = numbers[0]
for number  in numbers:
    if number  > max_number:
        max_number = number
print(f"The maximum number is: {max_number}")