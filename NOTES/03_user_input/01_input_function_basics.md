<a id="user-input-in-python"></a>

## User Input in Python

The built-in `input()` function allows a Python program to receive information from the user.

When Python reaches an `input()` call, the program pauses until the user enters a value and presses **Enter**.

> The `input()` function always returns the entered value as a string.

<a id="index"></a>

## Index

1. [Basic `input()` Function](#basic-input-function)

   * [Input as a String](#input-as-string)
   * [Using a Prompt](#using-an-input-prompt)
   * [Input as an Integer](#input-as-integer)
   * [Input as a Float](#input-as-float)
2. [Multiple Inputs on the Same Line](#multiple-inputs-same-line)

   * [Splitting Input with `split()`](#splitting-input)
   * [Collecting Two Names](#collecting-two-names)
   * [Using a Custom Separator](#custom-input-separator)
   * [Unpacking Requirements](#input-unpacking-requirements)
3. [Multiple Inputs on Different Lines](#multiple-inputs-different-lines)

   * [Using Separate `input()` Calls](#separate-input-calls)
   * [Using `map()` for Numeric Input](#map-numeric-input)
   * [Structured Input Example](#structured-input-example)
4. [Input Whitespace Handling](#input-whitespace-handling)

   * [Removing Whitespace with `strip()`](#input-strip)
   * [Removing Leading Whitespace with `lstrip()`](#input-lstrip)
   * [Removing Trailing Whitespace with `rstrip()`](#input-rstrip)
   * [Comparing Whitespace Methods](#comparing-whitespace-methods)
5. [Handling Invalid Numeric Input](#handling-invalid-input)
6. [Input Function Summary](#input-summary)

---

<a id="basic-input-function"></a>

## Basic `input()` Function

The `input()` function reads one line of text entered by the user.

### Syntax

```python
input(prompt)
```

The `prompt` argument is optional. It displays a message before waiting for input.

<a id="input-as-string"></a>

### 1. Input as a String

By default, `input()` returns the user's entry as a string.

```python
user_name = input()

print("Hello, " + user_name + "!")
```

**Example input:**

```text
Tony
```

**Output:**

```text
Hello, Tony!
```

The `+` operator performs string concatenation. Therefore, every value being joined must be a string.

You can verify the returned data type using `type()`:

```python
user_name = input()

print(type(user_name))
```

**Example input:**

```text
Tony
```

**Output:**

```text
<class 'str'>
```

Even when the user enters digits, `input()` returns a string:

```python
value = input()

print(value)
print(type(value))
```

**Example input:**

```text
25
```

**Output:**

```text
25
<class 'str'>
```

[Back to Index](#index)

---

<a id="using-an-input-prompt"></a>

### 2. Using a Prompt

A prompt tells the user what information to enter.

```python
user_name = input("Enter your name: ")

print(f"Hello, {user_name}!")
```

**Example interaction:**

```text
Enter your name: Tony
Hello, Tony!
```

The prompt is displayed before the program waits for input.

An f-string is often more readable than concatenation:

```python
city = input("Enter your city: ")

print(f"You live in {city}.")
```

**Example interaction:**

```text
Enter your city: Mumbai
You live in Mumbai.
```

[Back to Index](#index)

---

<a id="input-as-integer"></a>

### 3. Input as an Integer

Because `input()` returns a string, integer input must be converted using `int()`.

```python
age = int(input("Enter your age: "))

print("You are", age, "years old!")
```

**Example interaction:**

```text
Enter your age: 25
You are 25 years old!
```

The conversion occurs in two steps:

```text
"25" → 25
string → integer
```

You can verify the converted type:

```python
age = int(input("Enter your age: "))

print(type(age))
```

**Example interaction:**

```text
Enter your age: 25
<class 'int'>
```

Because `age` is an integer, it cannot be concatenated directly with strings:

```python
age = 25

message = "You are " + age + " years old."
```

**Error:**

```text
TypeError: can only concatenate str (not "int") to str
```

Use one of these approaches instead:

```python
age = 25

print("You are", age, "years old.")
print("You are " + str(age) + " years old.")
print(f"You are {age} years old.")
```

**Output:**

```text
You are 25 years old.
You are 25 years old.
You are 25 years old.
```

[Back to Index](#index)

---

<a id="input-as-float"></a>

### 4. Input as a Float

Use `float()` when the input may contain a decimal value.

```python
temperature = float(input("Enter the temperature: "))

print(f"The temperature is {temperature}°C.")
```

**Example interaction:**

```text
Enter the temperature: 28.5
The temperature is 28.5°C.
```

The conversion is:

```text
"28.5" → 28.5
string → float
```

[Back to Index](#index)

---

<a id="multiple-inputs-same-line"></a>

## Multiple Inputs on the Same Line

Multiple values can be entered on one line and separated using spaces, commas, or another delimiter.

The `split()` method separates the input string into multiple pieces.

<a id="splitting-input"></a>

### 1. Splitting Input with `split()`

```python
user_input = input("Enter some words: ")
words = user_input.split()

print(words)
```

**Example interaction:**

```text
Enter some words: Python is easy
['Python', 'is', 'easy']
```

When no separator is supplied, `split()` separates the text using whitespace.

It also handles repeated spaces:

```python
user_input = "Python   is    readable"
words = user_input.split()

print(words)
```

**Output:**

```text
['Python', 'is', 'readable']
```

[Back to Index](#index)

---

<a id="collecting-two-names"></a>

### 2. Collecting First and Last Names

The resulting values can be assigned directly to multiple variables.

```python
first_name, last_name = input(
    "Enter your first and last name: "
).split()

print(f"First name: {first_name}")
print(f"Last name: {last_name}")
```

**Example interaction:**

```text
Enter your first and last name: John Doe
First name: John
Last name: Doe
```

The input is processed as follows:

```text
"John Doe"
    ↓ split()
["John", "Doe"]
    ↓ unpacking
first_name = "John"
last_name = "Doe"
```

This approach works when the user enters exactly two values.

[Back to Index](#index)

---

<a id="custom-input-separator"></a>

### 3. Using a Custom Separator

Pass a separator to `split()` when the values are separated by commas or other characters.

```python
city, state = input(
    "Enter your city and state separated by a comma: "
).split(",")

city = city.strip()
state = state.strip()

print(f"City: {city}")
print(f"State: {state}")
```

**Example interaction:**

```text
Enter your city and state separated by a comma: Mumbai, Maharashtra
City: Mumbai
State: Maharashtra
```

The comma is used as the separator:

```python
.split(",")
```

The `strip()` method removes spaces around each extracted value.

[Back to Index](#index)

---

<a id="input-unpacking-requirements"></a>

### 4. Unpacking Requirements

The number of extracted values must match the number of variables.

This example expects exactly two values:

```python
first_name, last_name = input().split()
```

Entering only one value causes an error:

```text
John
```

**Error:**

```text
ValueError: not enough values to unpack (expected 2, got 1)
```

Entering more than two values also causes an error:

```text
John Michael Doe
```

**Error:**

```text
ValueError: too many values to unpack (expected 2)
```

Use `maxsplit` when the final value may contain spaces:

```python
first_name, remaining_name = input(
    "Enter your name: "
).split(maxsplit=1)

print(first_name)
print(remaining_name)
```

**Example interaction:**

```text
Enter your name: John Michael Doe
John
Michael Doe
```

Only one split is performed, producing two values.

[Back to Index](#index)

---

<a id="multiple-inputs-different-lines"></a>

## Multiple Inputs on Different Lines

Use separate `input()` calls when values should be entered on different lines.

<a id="separate-input-calls"></a>

### 1. Using Separate `input()` Calls

```python
name = input("Enter your name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))

print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
```

**Example interaction:**

```text
Enter your name: Alice
Enter your city: Pune
Enter your age: 24
Name: Alice
City: Pune
Age: 24
```

Each call reads one line of input.

[Back to Index](#index)

---

<a id="map-numeric-input"></a>

### 2. Using `map()` for Numeric Input

The `map()` function applies a conversion function to every item in an iterable.

Combined with `input().split()`, it can convert multiple entered values in one statement.

```python
first_number, second_number = map(
    int,
    input("Enter two integers: ").split()
)

print(first_number)
print(second_number)
```

**Example interaction:**

```text
Enter two integers: 7 21
7
21
```

The expression works in stages:

```text
Input:               "7 21"
After split():       ["7", "21"]
After map(int, ...): 7, 21
```

The equivalent longer version is:

```python
values = input("Enter two integers: ").split()

first_number = int(values[0])
second_number = int(values[1])
```

### Converting to a List

`map()` returns a map object rather than a list.

Convert it to a list when you need to store or index all values:

```python
numbers = list(
    map(int, input("Enter integers: ").split())
)

print(numbers)
print(type(numbers))
```

**Example interaction:**

```text
Enter integers: 10 20 30 40
[10, 20, 30, 40]
<class 'list'>
```

[Back to Index](#index)

---

<a id="structured-input-example"></a>

### 3. Structured Input Example

The following program reads string values on one line and numeric values on another line.

```python
favorite_color, favorite_fruit = input(
    "Enter your favorite color and fruit: "
).split()

favorite_number, lucky_number = map(
    int,
    input("Enter your favorite and lucky numbers: ").split()
)

print(
    f"Your favorite color is {favorite_color} "
    f"and your favorite fruit is {favorite_fruit}."
)

print(
    f"Your favorite number is {favorite_number} "
    f"and your lucky number is {lucky_number}."
)
```

**Example interaction:**

```text
Enter your favorite color and fruit: Blue Mango
Enter your favorite and lucky numbers: 7 21
Your favorite color is Blue and your favorite fruit is Mango.
Your favorite number is 7 and your lucky number is 21.
```

The first line produces two strings:

```text
"Blue Mango" → ["Blue", "Mango"]
```

The second line produces two integers:

```text
"7 21" → ["7", "21"] → 7, 21
```

[Back to Index](#index)

---

<a id="input-whitespace-handling"></a>

## Input Whitespace Handling

Whitespace includes:

* Spaces
* Tabs
* Newline characters

The `input()` function removes the newline produced when the user presses **Enter**, but it preserves other leading and trailing whitespace entered on the line.

For example, when a user enters spaces around a name, those spaces become part of the returned string.

<a id="input-strip"></a>

### 1. Removing Whitespace with `strip()`

The `strip()` method removes whitespace from both the beginning and end of a string.

```python
user_input = input("Enter your name: ")
cleaned_input = user_input.strip()

print(f"Hello, '{cleaned_input}'!")
```

**Example input:**

```text
   Alice   
```

**Output:**

```text
Hello, 'Alice'!
```

The original and cleaned values can be inspected using `repr()`:

```python
user_input = "   Alice   "
cleaned_input = user_input.strip()

print(repr(user_input))
print(repr(cleaned_input))
```

**Output:**

```text
'   Alice   '
'Alice'
```

A common concise pattern is:

```python
user_name = input("Enter your name: ").strip()
```

[Back to Index](#index)

---

<a id="input-lstrip"></a>

### 2. Removing Leading Whitespace with `lstrip()`

The `lstrip()` method removes whitespace only from the left side.

```python
user_input = "   Alice   "
cleaned_input = user_input.lstrip()

print(repr(cleaned_input))
```

**Output:**

```text
'Alice   '
```

The leading spaces are removed, but the trailing spaces remain.

[Back to Index](#index)

---

<a id="input-rstrip"></a>

### 3. Removing Trailing Whitespace with `rstrip()`

The `rstrip()` method removes whitespace only from the right side.

```python
user_input = "   Alice   "
cleaned_input = user_input.rstrip()

print(repr(cleaned_input))
```

**Output:**

```text
'   Alice'
```

The trailing spaces are removed, but the leading spaces remain.

[Back to Index](#index)

---

<a id="comparing-whitespace-methods"></a>

### 4. Comparing Whitespace Methods

```python
text = "   Python   "

print(repr(text.strip()))
print(repr(text.lstrip()))
print(repr(text.rstrip()))
```

**Output:**

```text
'Python'
'Python   '
'   Python'
```

| Method     | Removes from the left | Removes from the right |
| ---------- | --------------------- | ---------------------- |
| `strip()`  | Yes                   | Yes                    |
| `lstrip()` | Yes                   | No                     |
| `rstrip()` | No                    | Yes                    |

Whitespace removal is useful when comparing user input:

```python
answer = input("Continue? ").strip().lower()

if answer == "yes":
    print("Continuing...")
```

**Example interaction:**

```text
Continue?   YES
Continuing...
```

The input is processed as follows:

```text
"  YES  "
    ↓ strip()
"YES"
    ↓ lower()
"yes"
```

[Back to Index](#index)

---

<a id="handling-invalid-input"></a>

## Handling Invalid Numeric Input

Using `int()` or `float()` with incompatible input raises a `ValueError`.

```python
age = int(input("Enter your age: "))
```

If the user enters:

```text
twenty-five
```

Python raises:

```text
ValueError: invalid literal for int() with base 10: 'twenty-five'
```

Use `try` and `except` to handle invalid input safely:

```python
user_input = input("Enter your age: ").strip()

try:
    age = int(user_input)
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid whole number.")
```

**Example with valid input:**

```text
Enter your age: 25
You are 25 years old.
```

**Example with invalid input:**

```text
Enter your age: twenty-five
Please enter a valid whole number.
```

A loop can repeatedly request input until the user enters a valid value:

```python
while True:
    user_input = input("Enter your age: ").strip()

    try:
        age = int(user_input)
        break
    except ValueError:
        print("Invalid input. Enter a whole number.")

print(f"You are {age} years old.")
```

**Example interaction:**

```text
Enter your age: twenty
Invalid input. Enter a whole number.
Enter your age: 25
You are 25 years old.
```

[Back to Index](#index)

---

<a id="input-summary"></a>

## Input Function Summary

| Operation                     | Example                     | Result                            |
| ----------------------------- | --------------------------- | --------------------------------- |
| Read a string                 | `name = input()`            | Returns a string                  |
| Display a prompt              | `input("Enter name: ")`     | Shows instructions before reading |
| Read an integer               | `int(input())`              | Converts input to `int`           |
| Read a float                  | `float(input())`            | Converts input to `float`         |
| Split several values          | `input().split()`           | Returns a list of strings         |
| Convert several integers      | `map(int, input().split())` | Converts each item to `int`       |
| Remove surrounding whitespace | `input().strip()`           | Removes whitespace from both ends |
| Remove leading whitespace     | `input().lstrip()`          | Removes whitespace from the left  |
| Remove trailing whitespace    | `input().rstrip()`          | Removes whitespace from the right |

### Combined Example

```python
name = input("Enter your name: ").strip()

age = int(input("Enter your age: "))

height, weight = map(
    float,
    input("Enter your height and weight: ").split()
)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Weight: {weight}")
```

**Example interaction:**

```text
Enter your name:   Alice
Enter your age: 25
Enter your height and weight: 165.5 60.2
Name: Alice
Age: 25
Height: 165.5
Weight: 60.2
```

[Back to Index](#index)