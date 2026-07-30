# 🐍 Python Loops Cheat Sheet

## `for` Loop

Use a `for` loop when you know **how many times** you want to repeat something.

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

---

## `range()`

### `range(stop)`

Starts at **0** and stops **before** `stop`.

```python
range(5)
```

Produces:

```
0 1 2 3 4
```

---

### `range(start, stop)`

Starts at `start` and stops **before** `stop`.

```python
range(3, 7)
```

Produces:

```
3 4 5 6
```

---

### `range(start, stop, step)`

Starts at `start`, stops before `stop`, and increases by `step`.

```python
range(1, 10, 3)
```

Produces:

```
1 4 7
```

---

## `while` Loop

Use a `while` loop when you **don't know exactly how many times** something will repeat.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Output:

```
0
1
2
3
4
```

**Remember:** Always update the condition variable (`count += 1`) or you'll create an infinite loop.

---

## Infinite Loop

Python:

```python
while True:
    print("Running")
```

Embedded C:

```c
while(1)
{
    // Application code
}
```

Embedded systems intentionally run forever because the microcontroller continuously monitors and controls hardware.

---

## `break`

Stops the loop immediately.

```python
for i in range(6):
    if i == 4:
        break
    print(i)
```

Output:

```
0
1
2
3
```

---

## `continue`

Skips the current iteration and continues with the next one.

```python
for i in range(6):
    if i == 2:
        continue
    print(i)
```

Output:

```
0
1
3
4
5
```

---

## Nested Loops

A nested loop is a loop inside another loop.

```python
for row in range(2):
    for col in range(3):
        print(row, col)
```

Output:

```
0 0
0 1
0 2
1 0
1 1
1 2
```

Common applications:

- Matrices
- 2D arrays
- Keypad scanning
- Image processing
- Row/column operations

---

# Quick Reference

| Statement | Purpose |
|-----------|---------|
| `for` | Repeat a known number of times |
| `while` | Repeat while a condition is true |
| `break` | Exit the loop immediately |
| `continue` | Skip the current iteration |
| `range(stop)` | 0 to stop-1 |
| `range(start, stop)` | start to stop-1 |
| `range(start, stop, step)` | Count by the specified step |

---

# Common Mistakes

### `range()` excludes the stop value

```python
range(5)
```

Produces:

```
0 1 2 3 4
```

Not:

```
0 1 2 3 4 5
```

---

### Forgetting to update a `while` loop

```python
count = 0

while count < 5:
    print(count)
```

This creates an **infinite loop** because `count` never changes.

---

# Embedded Systems Connection

Blink an LED five times:

```python
for i in range(5):
    LED_ON()
    LED_OFF()
```

Continuous firmware:

```python
while True:
    read_sensor()
    control_motor()
    update_display()
```

Equivalent Embedded C:

```c
while(1)
{
    read_sensor();
    control_motor();
    update_display();
}
```

---

# Key Takeaways

- `for` → Use when the number of iterations is known.
- `while` → Use when repeating until a condition changes.
- `range()` → **Start is inclusive, stop is exclusive.**
- `break` → Ends the loop immediately.
- `continue` → Skips the current iteration.
- Nested loops → Useful for rows, columns, matrices, and keypad scanning.
- Embedded systems commonly use an infinite `while(1)` loop because firmware runs continuously.