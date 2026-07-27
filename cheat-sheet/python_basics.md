# Python Basics Cheat Sheet

## 1. Variables

Variables store information.

Python does not require you to declare the data type.

```python
name = "Evanio"
age = 31
height = 1.68
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
is_student = False
machine_running = True
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

`input()` gets information from the user.

Important:

`input()` always returns a string.

Example:

```python
name = input("Name: ")

print(name)
```

---

# 5. Type Conversion

Convert strings into numbers.

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

Display information:

```python
print("Hello World")
```

Print variables:

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

Count characters/items:

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
if score >= 90:
    status = "Healthy"

elif score >= 70:
    status = "Monitor"

else:
    status = "Maintenance Required"
```

---

# 13. Comparison Operators

| Operator | Meaning          |
| -------- | ---------------- |
| `>`      | Greater than     |
| `<`      | Less than        |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |
| `==`     | Equal            |
| `!=`     | Not equal        |

Example:

```python
if temperature > 80:
```

---

# 14. Lists

A list stores multiple values.

Similar to:

* C++ → `std::vector`
* C → dynamic array concept

Example:

```python
machines = [
    "Motor 01",
    "Pump 01",
    "Fan 01"
]
```

---

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

# 15. Comments

Comments explain code.

Python ignores them.

```python
# This is a comment

score = 100
```

---

# Common Beginner Commands

| Command    | Purpose            |
| ---------- | ------------------ |
| `print()`  | Display output     |
| `input()`  | Get user input     |
| `type()`   | Check data type    |
| `len()`    | Count items        |
| `.upper()` | Uppercase text     |
| `.lower()` | Lowercase text     |
| `int()`    | Convert to integer |
| `float()`  | Convert to decimal |
| `str()`    | Convert to string  |

---

# Engineering Examples

## Equipment Data

```python
equipment = "Conveyor Motor"

hours = 1500

temperature = 85.5

running = True
```

## Health Score

```python
score = 100

if temperature > 80:
    score -= 10
```

---

# Python vs C/C++

Python removes a lot of syntax but keeps the same programming concepts.

| Concept          | C/C++        | Python      |
| ---------------- | ------------ | ----------- |
| Variable         | Declare type | Automatic   |
| Dynamic array    | vector       | list        |
| Condition blocks | `{}`         | indentation |
| Function         | function     | `def`       |

---

# Current Learning Level

Completed:

✅ Variables
✅ Data types
✅ Input
✅ Output
✅ Strings
✅ f-strings
✅ Basic calculations
✅ Conditions
✅ Lists introduction

Next:

➡️ Loops
➡️ Functions
➡️ File handling
➡️ CSV reports
➡️ Object-oriented programming