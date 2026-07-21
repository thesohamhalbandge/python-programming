<a id="cleaning-and-formatting-user-input"></a>

## Cleaning and Formatting User Input in Python

User-provided input may contain extra whitespace, unwanted symbols, inconsistent capitalization, or incorrectly formatted values.

Cleaning and formatting input helps ensure that data is:

* Consistent
* Easier to validate
* Ready for processing
* Presented clearly

<a id="index"></a>

## Index

1. [Filtering Invalid Characters](#filtering-invalid-characters)

   * [Using `strip()`](#cleaning-with-strip)
   * [Using `replace()`](#cleaning-with-replace)
   * [Combining `strip()` and `replace()`](#combining-strip-and-replace)
   * [Removing All Non-Alphanumeric Characters](#removing-non-alphanumeric)
   * [Preserving Spaces While Filtering](#preserving-spaces)
2. [Formatting User Input](#formatting-user-input)

   * [Formatting Numbers with F-Strings](#formatting-numbers)
   * [Formatting Currency](#formatting-currency)
   * [Aligning and Padding Output](#aligning-and-padding)
   * [Creating a Formatted Table](#formatted-table)
3. [Cleaning and Formatting Together](#cleaning-and-formatting-together)
4. [Summary](#input-cleaning-summary)

---

<a id="filtering-invalid-characters"></a>

## Filtering Invalid Characters

Filtering invalid characters means removing whitespace, symbols, or other characters that should not be included in user input.

The appropriate cleaning method depends on which characters are allowed.

For example:

* A person's name may allow letters, spaces, hyphens, and apostrophes.
* A username may allow only letters and numbers.
* A phone number may allow digits and an optional `+` sign.
* A price may allow digits and one decimal point.

> Input should be cleaned according to its intended purpose. Removing every symbol may accidentally remove valid information.

<a id="cleaning-with-strip"></a>

### 1. Using `strip()`

The `strip()` method removes whitespace from the beginning and end of a string.

```python
user_input = "   Hello, World!   "
cleaned_input = user_input.strip()

print(repr(user_input))
print(repr(cleaned_input))
```

**Output:**

```text
'   Hello, World!   '
'Hello, World!'
```

The spaces inside the string remain unchanged.

```python
user_input = "   Hello   World   "
cleaned_input = user_input.strip()

print(repr(cleaned_input))
```

**Output:**

```text
'Hello   World'
```

The `strip()` method removes only leading and trailing whitespace.

A common pattern with `input()` is:

```python
user_name = input("Enter your name: ").strip()
```

[Back to Index](#index)

---

<a id="cleaning-with-replace"></a>

### 2. Using `replace()`

The `replace()` method replaces every occurrence of a specified substring.

### Syntax

```python
string.replace(old, new)
```

To remove a character, replace it with an empty string:

```python
text = "@Hello!"

cleaned_text = text.replace("@", "")

print(cleaned_text)
```

**Output:**

```text
Hello!
```

Multiple unwanted characters can be removed by chaining `replace()` calls:

```python
text = "@Hello!"

cleaned_text = text.replace("@", "").replace("!", "")

print(cleaned_text)
```

**Output:**

```text
Hello
```

The original string remains unchanged:

```python
print(text)
```

**Output:**

```text
@Hello!
```

> `replace()` removes only the exact characters or substrings you specify. It does not automatically detect every invalid character.

[Back to Index](#index)

---

<a id="combining-strip-and-replace"></a>

### 3. Combining `strip()` and `replace()`

The `strip()` and `replace()` methods can be used together to remove surrounding whitespace and specified unwanted symbols.

```python
user_input = input("Enter text: ")
```

**Example input:**

```text
 @Hello! 
```

Clean the value in separate steps:

```python
stripped_input = user_input.strip()
cleaned_input = stripped_input.replace("@", "").replace("!", "")

print(f"After strip():   {stripped_input!r}")
print(f"After replace(): {cleaned_input!r}")
```

**Output:**

```text
After strip():   '@Hello!'
After replace(): 'Hello'
```

The processing occurs as follows:

```text
" @Hello! "
      ↓ strip()
"@Hello!"
      ↓ replace("@", "")
"Hello!"
      ↓ replace("!", "")
"Hello"
```

The same operation can be written in one statement:

```python
user_input = input("Enter text: ")

cleaned_input = (
    user_input
    .strip()
    .replace("@", "")
    .replace("!", "")
)

print(cleaned_input)
```

[Back to Index](#index)

---

<a id="removing-non-alphanumeric"></a>

### 4. Removing All Non-Alphanumeric Characters

When the input should contain only letters and numbers, use `isalnum()` to filter its characters.

```python
user_input = "@Hello123!"
cleaned_input = "".join(
    character
    for character in user_input
    if character.isalnum()
)

print(cleaned_input)
```

**Output:**

```text
Hello123
```

The expression processes each character:

```text
@ → removed
H → retained
e → retained
l → retained
l → retained
o → retained
1 → retained
2 → retained
3 → retained
! → removed
```

A more concise version is:

```python
user_input = "@Hello123!"

cleaned_input = "".join(
    character for character in user_input if character.isalnum()
)

print(cleaned_input)
```

This approach uses a **whitelist**: only characters that satisfy the condition are retained.

> A whitelist is often more reliable than manually removing individual unwanted symbols because it clearly defines which characters are allowed.

[Back to Index](#index)

---

<a id="preserving-spaces"></a>

### 5. Preserving Spaces While Filtering

A basic `isalnum()` filter removes spaces because spaces are not alphanumeric.

To preserve spaces, include an additional condition:

```python
user_input = "  @Hello World!  "

cleaned_input = "".join(
    character
    for character in user_input.strip()
    if character.isalnum() or character.isspace()
)

print(cleaned_input)
```

**Output:**

```text
Hello World
```

This condition retains characters that are either:

* Alphanumeric: `character.isalnum()`
* Whitespace: `character.isspace()`

To replace repeated whitespace with a single space, use `split()` and `join()`:

```python
user_input = "  @Hello    World!  "

filtered_input = "".join(
    character
    for character in user_input
    if character.isalnum() or character.isspace()
)

cleaned_input = " ".join(filtered_input.split())

print(cleaned_input)
```

**Output:**

```text
Hello World
```

The processing occurs in two stages:

```text
"  @Hello    World!  "
          ↓ character filtering
"  Hello    World  "
          ↓ split() and join()
"Hello World"
```

[Back to Index](#index)

---

<a id="formatting-user-input"></a>

## Formatting User Input

F-strings provide a concise way to insert values into strings and control how those values are displayed.

### Basic Syntax

```python
f"Text {value}"
```

Example:

```python
name = "John"

print(f"Hello, {name}!")
```

**Output:**

```text
Hello, John!
```

F-strings can also format:

* Decimal places
* Currency
* Percentages
* Alignment
* Padding
* Scientific notation

<a id="formatting-numbers"></a>

### 1. Formatting Numbers with F-Strings

Use the `.nf` format specifier to display a floating-point value with a fixed number of decimal places.

```python
value = 25.6789

print(f"{value:.2f}")
```

**Output:**

```text
25.68
```

The format specifier `.2f` means:

* `f`: display the value in fixed-point notation
* `.2`: display two digits after the decimal point

Another example:

```python
temperature = float(input("Enter the temperature: "))

print(f"Temperature: {temperature:.1f}°C")
```

**Example interaction:**

```text
Enter the temperature: 28.456
Temperature: 28.5°C
```

Formatting changes how the value is displayed. It does not modify the original variable.

```python
value = 25.6789

formatted_value = f"{value:.2f}"

print(value)
print(formatted_value)
print(type(formatted_value))
```

**Output:**

```text
25.6789
25.68
<class 'str'>
```

[Back to Index](#index)

---

<a id="formatting-currency"></a>

### 2. Formatting Currency

A numeric price can be displayed with two decimal places:

```python
price = float(input("Enter the price: "))

print(f"The formatted price is: ${price:.2f}")
```

**Example interaction:**

```text
Enter the price: 25.6789
The formatted price is: $25.68
```

Use a comma separator for larger values:

```python
price = 1234567.89

print(f"${price:,.2f}")
```

**Output:**

```text
$1,234,567.89
```

The format specifier `:,.2f` means:

* `,`: add thousands separators
* `.2f`: display two decimal places

> Displaying a float as currency does not make floating-point arithmetic exact. Exact financial calculations usually require the `Decimal` class.

[Back to Index](#index)

---

<a id="aligning-and-padding"></a>

### 3. Aligning and Padding Output

F-strings can align values inside a specified width.

Common alignment symbols include:

| Symbol | Alignment |
| ------ | --------- |
| `<`    | Left      |
| `>`    | Right     |
| `^`    | Center    |

### Left Alignment

```python
name = "John"

print(f"|{name:<10}|")
```

**Output:**

```text
|John      |
```

The value is left-aligned within a width of `10`.

### Right Alignment

```python
score = 96

print(f"|{score:>6}|")
```

**Output:**

```text
|    96|
```

The value is right-aligned within a width of `6`.

### Center Alignment

```python
title = "Score"

print(f"|{title:^10}|")
```

**Output:**

```text
|  Score   |
```

The value is centered within a width of `10`.

[Back to Index](#index)

---

<a id="formatted-table"></a>

### 4. Creating a Formatted Table

Alignment specifiers are useful for tables and reports.

```python
name = input("Enter your name: ").strip()
score = int(input("Enter your score: "))

print("\nFormatted Output:")
print(f"| {'Name':<10} | {'Score':>6} |")
print(f"| {'-' * 10} | {'-' * 6} |")
print(f"| {name:<10} | {score:>6} |")
```

**Example interaction:**

```text
Enter your name: John
Enter your score: 96

Formatted Output:
| Name       |  Score |
| ---------- | ------ |
| John       |     96 |
```

The format specifiers work as follows:

```text
{name:<10}
```

* `<` left-aligns the value.
* `10` reserves ten character positions.

```text
{score:>6}
```

* `>` right-aligns the value.
* `6` reserves six character positions.

Multiple rows can use the same alignment:

```python
student1 = "John"
score1 = 96

student2 = "Alice"
score2 = 89

student3 = "Soham"
score3 = 100

print(f"| {'Name':<10} | {'Score':>6} |")
print(f"| {'-' * 10} | {'-' * 6} |")
print(f"| {student1:<10} | {score1:>6} |")
print(f"| {student2:<10} | {score2:>6} |")
print(f"| {student3:<10} | {score3:>6} |")
```

**Output:**

```text
| Name       |  Score |
| ---------- | ------ |
| John       |     96 |
| Alice      |     89 |
| Soham      |    100 |
```

[Back to Index](#index)

---

<a id="cleaning-and-formatting-together"></a>

## Cleaning and Formatting Together

Input cleaning and output formatting are often used in the same program.

```python
raw_name = input("Enter your name: ")
raw_price = input("Enter the price: ")

cleaned_name = " ".join(raw_name.strip().split())
cleaned_price = float(raw_price.strip())

print("\nFormatted Details:")
print(f"Name:  {cleaned_name.title()}")
print(f"Price: ${cleaned_price:,.2f}")
```

**Example interaction:**

```text
Enter your name:   john   doe
Enter the price:   1234.5

Formatted Details:
Name:  John Doe
Price: $1,234.50
```

The name is processed as follows:

```text
"  john   doe  "
        ↓ strip()
"john   doe"
        ↓ split()
["john", "doe"]
        ↓ " ".join()
"john doe"
        ↓ title()
"John Doe"
```

The price is processed as follows:

```text
"  1234.5  "
      ↓ strip()
"1234.5"
      ↓ float()
1234.5
      ↓ f"{value:,.2f}"
"1,234.50"
```

### Complete Validation Example

```python
raw_name = input("Enter your name: ")

cleaned_name = "".join(
    character
    for character in raw_name
    if character.isalpha() or character.isspace()
)

cleaned_name = " ".join(cleaned_name.split()).title()

raw_score = input("Enter your score: ").strip()

try:
    score = float(raw_score)

    print("\nStudent Record:")
    print(f"| {'Name':<20} | {'Score':>8} |")
    print(f"| {'-' * 20} | {'-' * 8} |")
    print(f"| {cleaned_name:<20} | {score:>8.2f} |")
except ValueError:
    print("The score must be a valid number.")
```

**Example interaction:**

```text
Enter your name:   @john   doe!
Enter your score: 96.456

Student Record:
| Name                 |    Score |
| -------------------- | -------- |
| John Doe             |    96.46 |
```

[Back to Index](#index)

---

<a id="input-cleaning-summary"></a>

## Summary

| Operation                     | Example                  | Purpose                                         |
| ----------------------------- | ------------------------ | ----------------------------------------------- |
| Remove surrounding whitespace | `text.strip()`           | Removes whitespace from both ends               |
| Remove a specific character   | `text.replace("@", "")`  | Removes every `@` character                     |
| Keep letters and numbers      | `char.isalnum()`         | Filters non-alphanumeric characters             |
| Keep letters only             | `char.isalpha()`         | Filters non-letter characters                   |
| Normalize internal spaces     | `" ".join(text.split())` | Replaces repeated whitespace with single spaces |
| Format two decimal places     | `f"{value:.2f}"`         | Displays two digits after the decimal           |
| Add thousands separators      | `f"{value:,.2f}"`        | Formats large numeric values                    |
| Left-align a value            | `f"{value:<10}"`         | Aligns within a fixed width                     |
| Right-align a value           | `f"{value:>10}"`         | Aligns within a fixed width                     |
| Center a value                | `f"{value:^10}"`         | Centers within a fixed width                    |

[Back to Index](#index)