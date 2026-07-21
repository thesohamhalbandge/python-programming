## Strings in Python

A **string** is a sequence of characters used to represent text. Python strings can contain letters, numbers, spaces, punctuation marks, and special characters.

---

## Declaring Strings with Single and Double Quotes

Strings can be created using either single quotes (`'`) or double quotes (`"`). Both forms behave identically.

### Using Single Quotes

```python
greeting = 'Hello, World!'

print(greeting)
```

**Output:**

```text
Hello, World!
```

### Using Double Quotes

```python
farewell = "Goodbye, World!"

print(farewell)
```

**Output:**

```text
Goodbye, World!
```

The choice between single and double quotes often depends on readability.

For example, double quotes make it easier to include an apostrophe:

```python
message = "Python isn't difficult."
```

Single quotes make it easier to include double quotation marks:

```python
message = 'He said, "Hello!"'
```

---

## Multiline Strings

A multiline string can span several lines. It is created using triple single quotes (`'''`) or triple double quotes (`"""`).

```python
message = """Hello,
This is a multiline string.
It can span several lines."""

print(message)
```

**Output:**

```text
Hello,
This is a multiline string.
It can span several lines.
```

The line breaks inside the string are preserved when it is printed.

Triple single quotes can also be used:

```python
message = '''First line
Second line
Third line'''
```

---

## String Length

Use the built-in `len()` function to determine the number of characters in a string.

The count includes:

* Letters
* Numbers
* Spaces
* Punctuation marks
* Special characters

```python
greeting = "Hello, world!"
length_of_greeting = len(greeting)

print(length_of_greeting)
```

**Output:**

```text
13
```

The string contains `13` characters, including the comma, space, and exclamation mark.

---

## String Indexing

Each character in a string has an index that identifies its position.

Python supports:

* Positive indexing, which starts from the beginning
* Negative indexing, which starts from the end

---

## Positive Index Access

Positive indexing begins at `0`.

For the string `"Hello"`, the indexes are:

```text
Character: H  e  l  l  o
Index:     0  1  2  3  4
```

```python
my_string = "Hello"

print(my_string[0])
print(my_string[1])
print(my_string[4])
```

**Output:**

```text
H
e
o
```

### Index Errors

Trying to access an index outside the string's valid range raises an `IndexError`.

```python
my_string = "Hello"

print(my_string[5])
```

**Error:**

```text
IndexError: string index out of range
```

Because `"Hello"` contains five characters, its valid positive indexes range from `0` to `4`.

---

## Negative Index Access

Negative indexing starts from the end of a string.

* `-1` represents the last character.
* `-2` represents the second-to-last character.
* `-3` represents the third-to-last character.

For the string `"Hello"`, the indexes are:

```text
Character:       H   e   l   l   o
Positive index:  0   1   2   3   4
Negative index: -5  -4  -3  -2  -1
```

### Example

```python
my_string = "Hello, World!"

print(my_string[-1])
print(my_string[-5])
```

**Output:**

```text
!
o
```

* `my_string[-1]` returns the final character, `!`.
* `my_string[-5]` returns the fifth character from the end, `o`.

Negative indexing is useful when the string's length is unknown.

---

## String Immutability

Strings in Python are **immutable**, meaning their characters cannot be changed after the string is created.

The following code produces an error:

```python
my_string = "Hello"

my_string[0] = "h"
```

**Error:**

```text
TypeError: 'str' object does not support item assignment
```

To modify a string, create a new string instead.

```python
my_string = "Hello"
modified_string = "h" + my_string[1:]

print(modified_string)
```

**Output:**

```text
hello
```

The original string remains unchanged:

```python
print(my_string)
```

**Output:**

```text
Hello
```

---

## String Slicing

Slicing extracts a portion of a string.

### Syntax

```python
string[start:end:step]
```

* `start` is the index where the slice begins. It is included.
* `end` is the index where the slice stops. It is not included.
* `step` determines the interval between selected characters.

The `step` value is optional.

---

## Full String Slice

Omitting both the `start` and `end` values returns the complete string.

```python
my_string = "Hello, World!"
full_slice = my_string[:]

print(full_slice)
```

**Output:**

```text
Hello, World!
```

The expression `my_string[:]` returns the complete string.

> Because strings are immutable, Python may reuse the same string object rather than creating a separate object in memory.

---

## Partial Slicing

Partial slicing extracts a specific section of a string.

```python
my_string = "Hello, World!"

print(my_string[0:5])
print(my_string[7:12])
```

**Output:**

```text
Hello
World
```

The ending index is excluded from the result.

Therefore:

```python
my_string[0:5]
```

includes indexes `0`, `1`, `2`, `3`, and `4`, but not index `5`.

### Omitting the Start Index

When `start` is omitted, Python begins at the start of the string.

```python
my_string = "Hello, World!"

print(my_string[:5])
```

**Output:**

```text
Hello
```

### Omitting the End Index

When `end` is omitted, Python continues to the end of the string.

```python
my_string = "Hello, World!"

print(my_string[7:])
```

**Output:**

```text
World!
```

### Using the Step Value

The `step` value determines how many positions Python moves between characters.

```python
my_string = "Hello, World!"

print(my_string[::2])
```

**Output:**

```text
Hlo ol!
```

A step of `2` selects every second character.

---

## Empty Slice Results

Unlike direct indexing, slicing does not normally raise an `IndexError` when indexes are outside the valid range. Python adjusts out-of-range slice indexes automatically.

### Start and End Are Equal

When the start and end indexes are equal, the result is an empty string.

```python
my_string = "Hello World"
empty_slice = my_string[5:5]

print(empty_slice)
```

**Output:**

```text
```

The value of `empty_slice` is `""`.

You can verify it using `repr()`:

```python
print(repr(empty_slice))
```

**Output:**

```text
''
```

### Start Index Exceeds the String Length

When the start index is beyond the end of the string, the result is also empty.

```python
my_string = "Hello World"
empty_slice = my_string[12:15]

print(repr(empty_slice))
```

**Output:**

```text
''
```

### Start Comes After End

With the default positive step, slicing moves from left to right. If the start index comes after the end index, the result is empty.

```python
my_string = "Hello World"
empty_slice = my_string[8:3]

print(repr(empty_slice))
```

**Output:**

```text
''
```

---

## Negative Slicing

Negative indexes can also be used in slices.

```python
my_string = "Hello World"
substring = my_string[-5:-2]

print(substring)
```

**Output:**

```text
Wor
```

For `"Hello World"`:

```text
Character:       H   e   l   l   o       W   o   r   l   d
Positive index:  0   1   2   3   4   5   6   7   8   9  10
Negative index: -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
```

The slice begins at index `-5`, which contains `W`, and stops before index `-2`, which contains `l`.

Therefore, the result is `"Wor"`.

### Empty Negative Slice

With the default positive step, Python still reads from left to right. If the start position comes after the end position, the result is empty.

```python
my_string = "Hello World"
empty_slice = my_string[-2:-5]

print(repr(empty_slice))
```

**Output:**

```text
''
```

Index `-2` appears later in the string than index `-5`, so Python cannot move from `-2` to `-5` using the default positive step.

### Out-of-Range Negative Indexes

Out-of-range negative slice indexes are adjusted to the beginning of the string.

```python
my_string = "Hello World"
substring = my_string[-20:-1]

print(substring)
```

**Output:**

```text
Hello Worl
```

The start index `-20` is outside the string, so Python adjusts it to the beginning. The end index `-1` excludes the final character.

---

## Reversing a String

A negative step can be used to move through a string from right to left.

```python
my_string = "Hello"

reversed_string = my_string[::-1]

print(reversed_string)
```

**Output:**

```text
olleH
```

The step value `-1` selects the characters in reverse order.

---

## String Concatenation

String concatenation means joining two or more strings to create a new string.

Use the addition operator (`+`) to concatenate strings.

### Concatenating Variables

```python
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name

print(full_name)
```

**Output:**

```text
John Doe
```

The string `" "` inserts a space between the first and last names.

### Concatenating String Literals

```python
greeting = "Hello, " + "World!"

print(greeting)
```

**Output:**

```text
Hello, World!
```

### Strings Cannot Be Concatenated Directly with Numbers

The `+` operator cannot directly concatenate a string and an integer.

```python
age = 25

message = "Age: " + age
```

**Error:**

```text
TypeError: can only concatenate str (not "int") to str
```

Convert the number to a string using `str()`:

```python
age = 25

message = "Age: " + str(age)

print(message)
```

**Output:**

```text
Age: 25
```

An f-string is usually more readable:

```python
age = 25

message = f"Age: {age}"

print(message)
```

**Output:**

```text
Age: 25
```