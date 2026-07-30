# Day 1 - Python Basics

Date: July 27, 2026

---

# Topics Covered

* `print()`
* Variables
* Data Types
* `input()`
* Type conversion
* Math operations
* Strings
* f-strings
* Basic conditional logic (`if`, `elif`, `else`)
* Introduction to lists

---

# Things I Learned

## Variables

Variables store information that can be used or changed throughout a program.

Example:

```python
name = "Evanio"
```

A variable is a named location used to store a value.

---

# Data Types

Python's basic data types:

| Type    | Meaning                     |
| ------- | --------------------------- |
| `str`   | Text                        |
| `int`   | Whole numbers               |
| `float` | Numbers with decimal places |
| `bool`  | True or False               |

Examples:

```python
name = "Motor A"      # str
hours = 1500          # int
temperature = 85.5    # float
running = True        # bool
```

---

# Useful Functions

```python
type()
len()
.upper()
.lower()
```

## Examples

```python
type(hours)

len(name)

name.upper()

name.lower()
```

---

# Keywords Learned

* `print`
* `input`
* `str`
* `int`
* `float`
* `bool`
* `if`
* `elif`
* `else`
* f-string

---

# Input and Conversion

`input()` collects information from the user.

Important:

`input()` always returns a string.

Example:

```python
hours = int(input("Operating hours: "))
```

The value must be converted when performing calculations.

---

# Formatting Numbers

Problem:

Area printed as:

```
810.5500000000001
```

Solution:

Use formatting:

```python
{area:.2f}
```

This displays two decimal places.

Example:

```python
print(f"Area: {area:.2f}")
```

Output:

```
Area: 810.55
```

---

# Mini Project Completed

## Equipment Health Calculator

Created:

```
mini-projects/
└── 01_equipment_health_calculator.py
```

The program:

* Takes equipment information from the user
* Calculates a reliability score
* Evaluates equipment condition
* Provides maintenance recommendations

Concepts practiced:

* Variables
* User input
* Integer and float conversion
* Mathematical calculations
* Conditional statements
* f-strings

---

# New Concept: Conditional Statements

Python uses conditions to make decisions.

Example:

```python
if temperature > 80:
    score -= 10
```

Python uses indentation instead of `{}` like C/C++.

Example comparison:

C:

```c
if (temperature > 80)
{
    score -= 10;
}
```

Python:

```python
if temperature > 80:
    score -= 10
```

---

# New Concept: Lists

A Python list is similar to a C++ `std::vector`.

Example:

Python:

```python
machines = [
    "Motor 01",
    "Pump 01",
    "Fan 01"
]
```

C++ equivalent:

```cpp
std::vector<string> machines;
```

Useful commands:

```python
machines.append("Motor 02")

len(machines)

machines[0]
```

A list stores multiple pieces of data that can be accessed individually.

---

# Programming Comparison

| Concept       | C             | C++           | Python  |
| ------------- | ------------- | ------------- | ------- |
| Variable      | `int x = 5;`  | `int x = 5;`  | `x = 5` |
| Array         | `int a[5]`    | `std::array`  | list    |
| Dynamic Array | Manual memory | `std::vector` | list    |
| Condition     | `if`          | `if`          | `if`    |

---

# Problems I Had

## Adapting to Python's Simplicity

Coming from C, Python feels very different because:

* Less syntax
* No need to declare variable types
* No manual memory management
* No `{}` blocks

The concepts are similar, but the language removes a lot of complexity.

---

# Questions I Answered Today

## What is a variable?

A variable is a named location used to store a value that can be accessed and modified during program execution.

---

## What is the difference between str, int, float, bool?

* `str` → text
* `int` → whole numbers
* `float` → decimal numbers
* `bool` → True or False

---

## What does input() do?

`input()` receives information from the user and returns it as a string.

---

## What does print() do?

`print()` displays text or values on the screen.

---

## What are f-strings?

An f-string allows variables to be inserted directly into text.

Example:

```python
name = "Motor A"

print(f"Equipment: {name}")
```

Output:

```
Equipment: Motor A
```

---

# Reflection

## What new thing surprised you today?

The similarity between C and Python, but also the subtle differences.

Python keeps the same programming concepts but removes much of the complexity.

---

## What was difficult?

Adapting to the simplicity of the language.

---

## What was easy?

Writing my own logic, following steps, and understanding the flow of the program.

---

## What would you like to build with Python?

Definitely! I am falling in love with the language every single moment.

I want to use Python to build engineering tools, automation systems, equipment monitoring software, and practical applications.

---

# Next Steps

Day 2:

* More `if/elif/else`
* Comparison operators
* Logical operators
* Improving the Equipment Health Calculator

Future goals:

* Loops
* Lists
* Functions
* File handling
* CSV reports
* Object-oriented programming
* Engineering automation projects
