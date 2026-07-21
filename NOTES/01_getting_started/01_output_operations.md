## Basic `print()` Function

### 1. Printing Text

```python
print("Hello, World!")  # Using double quotes
print('Welcome to Python!')  # Using single quotes
```

### 2. Printing Numbers

```python
print(123)  # Prints a whole number
print(3.14)  # Prints a decimal number
```

### 3. Printing Multiple Items

```python
print("Hello", "world", 2026)
```

**Output:**

```text
Hello world 2026
```

By default, Python inserts a space between each item.

### 4. Printing with a Separator

Use the `sep` parameter to specify the separator between multiple items.

**Syntax:**

```python
print(item1, item2, item3, sep="your_separator")
```

**Example:**

```python
print("apple", "banana", "cherry", sep=", ")
```

**Output:**

```text
apple, banana, cherry
```

### 5. Printing with the `end` Parameter

The `end` parameter specifies what should be printed after the output. By default, its value is `"\n"`, which moves the cursor to a new line.

#### Printing on the Same Line

```python
print("Hello", end=" ")
print("World!")
```

**Output:**

```text
Hello World!
```

#### Using Custom Endings

```python
print("Item 1", end=", ")
print("Item 2", end=", ")
print("Item 3")
```

**Output:**

```text
Item 1, Item 2, Item 3
```

### 6. Using Escape Sequences

Escape sequences represent special characters inside strings.

```python
print("He said, \"Hello!\"")
```

**Output:**

```text
He said, "Hello!"
```

#### Common Escape Sequences

| Escape sequence | Description                     |
| --------------- | ------------------------------- |
| `\'`            | Inserts a single quotation mark |
| `\"`            | Inserts a double quotation mark |
| `\\`            | Inserts a literal backslash     |
| `\n`            | Inserts a newline               |
| `\t`            | Inserts a horizontal tab        |

### 7. Printing Empty Lines

```python
print()
```

Calling `print()` without any arguments inserts one blank line.

Other approaches include:

```python
print(" ")   # Prints a single space
print("\n")  # Prints two newline characters in total
```

> `print()` is the preferred way to print a blank line.

### 8. Formatting Printed Output

#### 8.1 F-Strings

F-strings allow variables and expressions to be inserted directly into a string.

```python
num_apples = 2
num_oranges = 3

print(f"I have {num_apples} apples and {num_oranges} oranges.")
```

**Output:**

```text
I have 2 apples and 3 oranges.
```

#### 8.2 The `format()` Method

```python
print("I have {} apples and {} oranges.".format(2, 3))
```

**Output:**

```text
I have 2 apples and 3 oranges.
```