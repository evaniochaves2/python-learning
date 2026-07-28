# Python Basics Cheat Sheet

> **Version 1.2**
>
> Updated after completing **Day 2** of the Python Learning Roadmap.

---

# 1. Variables

Variables store information.

Python does not require you to declare the data type.

```python
name = "Evanio"
age = 31
height = 1.68
```

Use descriptive names.

Good:

```python
motor_speed = 1500
temperature = 85.5
```

Avoid:

```python
x = 1500
a = 85.5
```

---

# 2. Data Types

## String (`str`)

Used for text.

```python
name = "Evanio"
equipment = "Motor A"
```

---

## Integer (`int`)

Whole numbers.

```python
age = 31
hours = 1500
```

---

## Float (`float`)

Numbers with decimal places.

```python
height = 1.68
temperature = 85.5
```

---

## Boolean (`bool`)

True or False values.

```python
machine_running = True
alarm_active = False
```

---

# 3. Check Data Type

Use:

```python
type()
```

Example:

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

---

# 4. User Input

`input()` receives information from the user.

**Important:**

`input()` always returns a string.

Example:

```python
name = input("Name: ")

print(name)
```

---

# 5. Type Conversion

Convert between data types.

## Integer

```python
age = int(input("Age: "))
```

## Float

```python
temperature = float(input("Temperature: "))
```

## String

```python
number = str(100)
```

---

# 6. Printing

Display information.

```python
print("Hello World")
```

Print variables.

```python
name = "Evanio"

print(name)
```

---

# 7. f-Strings

Insert variables directly into text.

Syntax:

```python
f"Text {variable}"
```

Example:

```python
name = "Evanio"

print(f"Hello {name}")
```

Output:

```text
Hello Evanio
```

Engineering example:

```python
temperature = 75

print(f"Current temperature: {temperature}°C")
```

---

# 8. String Methods

## Uppercase

```python
name.upper()
```

Example:

```python
"motor".upper()
```

Output:

```text
MOTOR
```

---

## Lowercase

```python
name.lower()
```

Example:

```python
"PYTHON".lower()
```

Output:

```text
python
```

---

# 9. Length

Count characters or items.

```python
len()
```

Example:

```python
len("Python")
```

Output:

```text
6
```

---

# 10. Math Operators

## Addition

```python
+
```

## Subtraction

```python
-
```

## Multiplication

```python
*
```

## Division

```python
/
```

## Power

```python
**
```

Example:

```python
area = length * width
```

---

# 11. Number Formatting

Control decimal places.

Example:

```python
area = 810.55000001

print(f"{area:.2f}")
```

Output:

```text
810.55
```

---

# 12. Conditional Statements

Used to make decisions.

## if

```python
if condition:
    code
```

Example:

```python
if temperature > 80:
    print("Warning")
```

---

## if / elif / else

```python
if temperature < 60:
    status = "Cold"

elif temperature < 80:
    status = "Normal"

else:
    status = "Warning"
```

---

# 13. Indentation

Python uses **indentation** instead of braces (`{}`) to define blocks of code.

Correct:

```python
if temperature > 80:
    print("Warning")
```

Incorrect:

```python
if temperature > 80:
print("Warning")
```

Use **4 spaces** for each indentation level.

---

# 14. Comparison Operators

| Operator | Meaning |
|----------|---------|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `==` | Equal |
| `!=` | Not equal |

Example:

```python
if temperature > 80:
```

---

# 15. Boolean Logic

Used to combine conditions.

| Operator | Meaning |
|----------|---------|
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses a condition |

Example:

```python
temperature = 70
pressure = 100

if temperature < 80 and pressure < 150:
    print("Machine Healthy")
```

---

# 16. Lists (Preview)

Lists store multiple values.

This section is included as a preview because Python lists are conceptually similar to **dynamic arrays in C** and **`std::vector` in C++**.

Lists will be covered in detail later in the learning roadmap.

Example:

```python
machines = [
    "Motor 01",
    "Pump 01",
    "Fan 01"
]
```

## Access List Items

Lists use indexing.

```python
machines[0]
```

Output:

```text
Motor 01
```

---

## Add Items

```python
machines.append("Motor 02")
```

---

## Count Items

```python
len(machines)
```

---

# 17. Comments

Comments explain code.

Python ignores them.

```python
# This is a comment

temperature = 75
```

---

# Common Beginner Commands

| Command | Purpose |
|----------|---------|
| `print()` | Display output |
| `input()` | Get user input |
| `type()` | Check data type |
| `len()` | Count items |
| `.upper()` | Convert to uppercase |
| `.lower()` | Convert to lowercase |
| `int()` | Convert to integer |
| `float()` | Convert to decimal |
| `str()` | Convert to string |
| `round()` | Round numbers |
| `max()` | Largest value |
| `min()` | Smallest value |
| `sum()` | Add values |

---

# Engineering Examples & Applications

## Equipment Data

```python
equipment = "Conveyor Motor"

hours = 1500
temperature = 85.5
running = True
```

---

## Equipment Health Score

```python
score = 100

if temperature > 80:
    score -= 10
```

---

## Equipment Monitor

```python
equipment = "Motor A"
temperature = 75
running = True

if running and temperature < 80:
    print(f"{equipment} operating normally")
else:
    print(f"{equipment} requires inspection")
```

---

# Common Beginner Mistakes

## Forgetting Type Conversion

Wrong:

```python
age = input("Age: ")

print(age + 5)
```

Correct:

```python
age = int(input("Age: "))

print(age + 5)
```

---

## Using `=` Instead of `==`

Wrong:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

## Forgetting the Colon

Wrong:

```python
if temperature > 80
    print("Warning")
```

Correct:

```python
if temperature > 80:
    print("Warning")
```

---

## Incorrect Indentation

Wrong:

```python
if temperature > 80:
print("Warning")
```

Correct:

```python
if temperature > 80:
    print("Warning")
```

---

# Python vs C/C++

Python removes extra syntax but keeps the same programming concepts.

| Concept | C/C++ | Python |
|---------|--------|---------|
| Variable | Declare type | Automatic typing |
| Dynamic Array | `std::vector` | `list` |
| Condition Blocks | `{}` | Indentation |
| Comments | `//` | `#` |
| Function | Function | `def` |

---

# Current Learning Progress

## Completed

- ✅ Variables
- ✅ Data Types
- ✅ User Input
- ✅ Type Conversion
- ✅ Printing
- ✅ Strings
- ✅ String Methods
- ✅ f-Strings
- ✅ Math Operators
- ✅ Conditional Statements
- ✅ Comparison Operators
- ✅ Boolean Logic
- ✅ Comments

## Previewed

- 👀 Lists (Introduction)

## Coming Next

- ⏳ Loops (`for` and `while`)
- ⏳ Lists (Detailed Study)
- ⏳ Functions
- ⏳ Dictionaries
- ⏳ File Handling
- ⏳ CSV Reports
- ⏳ Object-Oriented Programming