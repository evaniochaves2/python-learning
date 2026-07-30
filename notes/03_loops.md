# Python - Loops

## What is a Loop?

A loop repeatedly executes a block of code.

Loops are used when a task needs to be repeated without writing the same code multiple times.

Example applications:
- Printing values
- Processing lists
- Repeating calculations
- Embedded systems (reading sensors continuously)

---

# for Loop

A for loop repeats code a known number of times.

Syntax:

for i in range(5):
    print(i)

Output:

0
1
2
3
4

---

# range()

range(stop)

Starts at 0 and stops before stop.

Example:

range(5)

Produces:

0 1 2 3 4

---

range(start, stop)

Example:

range(3,7)

Produces:

3 4 5 6

---

range(start, stop, step)

Example:

range(1,10,3)

Produces:

1 4 7

---

# while Loop

A while loop repeats code while a condition is true.

Example:

count = 0

while count < 5:
    print(count)
    count += 1

Output:

0
1
2
3
4

---

Important:

Always update the condition variable.

Otherwise an accidental infinite loop occurs.

---

# Infinite Loops

Python:

while True:
    print("Running")

Embedded C:

while(1)
{
    // Application
}

Embedded systems intentionally use infinite loops so the microcontroller continuously monitors and controls hardware.

---

# break

break immediately exits the loop.

Example:

for i in range(6):
    if i == 4:
        break
    print(i)

Output:

0
1
2
3

---

# continue

continue skips the current iteration and continues with the next one.

Example:

for i in range(6):
    if i == 2:
        continue
    print(i)

Output:

0
1
3
4
5

---

Difference

break
- Exits the entire loop.

continue
- Skips one iteration and continues the loop.

---

# Nested Loops

A nested loop is a loop inside another loop.

Example:

for row in range(3):
    for col in range(2):
        print(row, col)

Output:

0 0
0 1
1 0
1 1
2 0
2 1

Applications:

- Matrix operations
- Keypad scanning
- Image processing
- 2D arrays
- Reading rows and columns of sensors

---

# Engineering Connection

Blink LED five times

for i in range(5):
    LED_ON()
    LED_OFF()

Continuous firmware

while True:
    read_sensor()
    control_motor()
    update_display()

The logic is identical to embedded C.
Only the syntax changes.