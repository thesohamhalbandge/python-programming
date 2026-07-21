<a id="string-methods-in-python"></a>

## String Methods in Python

Python provides built-in string methods for changing letter case, removing unwanted characters, and validating string content.

String methods do not modify the original string because strings are immutable. Instead, they return a new string or a Boolean value.

<a id="index"></a>

## Index

1. [Converting String Case](#converting-string-case)

   * [`upper()`](#upper-method)
   * [`lower()`](#lower-method)
   * [`title()`](#title-method)
2. [Checking String Case](#checking-string-case)

   * [`isupper()`](#isupper-method)
   * [`islower()`](#islower-method)
3. [Removing Whitespace and Characters](#removing-whitespace-and-characters)

   * [`strip()`](#strip-method)
   * [`lstrip()`](#lstrip-method)
   * [`rstrip()`](#rstrip-method)
4. [Checking String Content](#checking-string-content)

   * [`isalpha()`](#isalpha-method)
   * [`isdigit()`](#isdigit-method)
   * [`isalnum()`](#isalnum-method)

---

<a id="converting-string-case"></a>

## Converting String Case

Python includes several methods for changing the capitalization of a string.

<a id="upper-method"></a>

### 1. Converting to Uppercase with `upper()`

The `upper()` method converts all lowercase letters in a string to uppercase.

```python
text = "hello world"
uppercase_text = text.upper()

print(uppercase_text)
```

**Output:**

```text
HELLO WORLD
```

The original string remains unchanged:

```python
text = "hello world"
uppercase_text = text.upper()

print(text)
print(uppercase_text)
```

**Output:**

```text
hello world
HELLO WORLD
```

The `upper()` method is useful for normalizing user input and performing case-insensitive comparisons.

```python
answer = "yes"

if answer.upper() == "YES":
    print("The user agreed.")
```

**Output:**

```text
The user agreed.
```

[Back to Index](#index)

---

<a id="lower-method"></a>

### 2. Converting to Lowercase with `lower()`

The `lower()` method converts all uppercase letters in a string to lowercase.

```python
text = "Hello World!"
lowercase_text = text.lower()

print(lowercase_text)
```

**Output:**

```text
hello world!
```

The original string remains unchanged:

```python
text = "Hello World!"
lowercase_text = text.lower()

print(text)
print(lowercase_text)
```

**Output:**

```text
Hello World!
hello world!
```

The `lower()` method is commonly used when comparing text without considering capitalization.

```python
username = "Soham"

if username.lower() == "soham":
    print("Username matched.")
```

**Output:**

```text
Username matched.
```

[Back to Index](#index)

---

<a id="title-method"></a>

### 3. Converting to Title Case with `title()`

The `title()` method returns a new string in which each word begins with an uppercase letter and the remaining letters are lowercase.

```python
my_string = "hello world"
title_case_string = my_string.title()

print(title_case_string)
```

**Output:**

```text
Hello World
```

The original string remains unchanged:

```python
print(my_string)
```

**Output:**

```text
hello world
```

The `title()` method can be useful when formatting headings, names, and titles.

```python
book_title = "the old man and the sea"

print(book_title.title())
```

**Output:**

```text
The Old Man And The Sea
```

> `title()` capitalizes words according to Python's word-boundary rules. Its output may not always follow formal title-writing conventions.

For example:

```python
text = "python's string methods"

print(text.title())
```

**Output:**

```text
Python'S String Methods
```

[Back to Index](#index)

---

<a id="checking-string-case"></a>

## Checking String Case

The `isupper()` and `islower()` methods check the capitalization of the letters in a string.

These methods return Boolean values:

* `True`
* `False`

Numbers, spaces, and punctuation do not affect the result. However, the string must contain at least one letter with a case.

<a id="isupper-method"></a>

### 1. Checking Uppercase with `isupper()`

The `isupper()` method returns `True` when:

* The string contains at least one cased letter.
* Every cased letter is uppercase.

#### Uppercase Letters Only

```python
text = "HELLO"

print(text.isupper())
```

**Output:**

```text
True
```

#### Mixed Uppercase and Lowercase Letters

```python
text = "Hello"

print(text.isupper())
```

**Output:**

```text
False
```

#### Uppercase Letters with Numbers

Numbers do not affect the result.

```python
text = "HELLO123"

print(text.isupper())
```

**Output:**

```text
True
```

#### Numbers Only

A string containing only numbers returns `False` because it does not contain any cased letters.

```python
text = "1234"

print(text.isupper())
```

**Output:**

```text
False
```

#### Uppercase Letters with Symbols

Symbols do not affect the result.

```python
text = "HELLO!"

print(text.isupper())
```

**Output:**

```text
True
```

[Back to Index](#index)

---

<a id="islower-method"></a>

### 2. Checking Lowercase with `islower()`

The `islower()` method returns `True` when:

* The string contains at least one cased letter.
* Every cased letter is lowercase.

#### Lowercase Letters Only

```python
text = "hello"

print(text.islower())
```

**Output:**

```text
True
```

#### Mixed Uppercase and Lowercase Letters

```python
text = "Hello"

print(text.islower())
```

**Output:**

```text
False
```

#### Lowercase Letters with Numbers

Numbers do not affect the result.

```python
text = "hello123"

print(text.islower())
```

**Output:**

```text
True
```

#### Numbers Only

A string containing only numbers returns `False` because it does not contain any cased letters.

```python
text = "1234"

print(text.islower())
```

**Output:**

```text
False
```

#### Lowercase Letters with Symbols

```python
text = "hello!"

print(text.islower())
```

**Output:**

```text
True
```

[Back to Index](#index)

---

<a id="removing-whitespace-and-characters"></a>

## Removing Whitespace and Characters

Python provides the following methods for removing unwanted whitespace or characters:

* `strip()` removes characters from both ends.
* `lstrip()` removes characters from the left side.
* `rstrip()` removes characters from the right side.

When no argument is provided, these methods remove whitespace such as spaces, tabs, and newline characters.

<a id="strip-method"></a>

### 1. Removing Whitespace with `strip()`

The `strip()` method removes leading and trailing whitespace from a string.

```python
my_string = "   Hello, World!   "
stripped_string = my_string.strip()

print(stripped_string)
```

**Output:**

```text
Hello, World!
```

The whitespace inside the string is not removed.

```python
my_string = "   Hello, World!   "

print(my_string.strip())
```

**Output:**

```text
Hello, World!
```

The original string remains unchanged:

```python
print(repr(my_string))
```

**Output:**

```text
'   Hello, World!   '
```

#### Removing Specific Characters

You can pass a collection of characters to `strip()`.

```python
text = "***Hello***"
cleaned_text = text.strip("*")

print(cleaned_text)
```

**Output:**

```text
Hello
```

The argument is treated as a set of individual characters, not as an exact prefix or suffix.

```python
text = "xyxHello Worldxy"
cleaned_text = text.strip("xy")

print(cleaned_text)
```

**Output:**

```text
Hello World
```

Python repeatedly removes any `x` or `y` characters found at either end.

[Back to Index](#index)

---

<a id="lstrip-method"></a>

### 2. Removing Leading Characters with `lstrip()`

The `lstrip()` method removes whitespace or specified characters from the beginning of a string.

#### Removing Leading Whitespace

```python
my_string = "   Hello, World!"
cleaned_string = my_string.lstrip()

print(cleaned_string)
```

**Output:**

```text
Hello, World!
```

Only the whitespace on the left side is removed.

#### Removing Specific Leading Characters

```python
another_string = "***Hello, World!"
result = another_string.lstrip("*")

print(result)
```

**Output:**

```text
Hello, World!
```

#### Removing Multiple Possible Characters

```python
text = "!?!!Hello"
result = text.lstrip("!?")

print(result)
```

**Output:**

```text
Hello
```

The argument `"!?"` means that any leading `!` or `?` characters should be removed.

> `lstrip()` does not remove an exact substring. It removes any combination of the supplied characters from the left side.

[Back to Index](#index)

---

<a id="rstrip-method"></a>

### 3. Removing Trailing Characters with `rstrip()`

The `rstrip()` method removes whitespace or specified characters from the end of a string.

#### Removing Trailing Whitespace

```python
my_string = "Hello, World!   "
cleaned_string = my_string.rstrip()

print(cleaned_string)
```

**Output:**

```text
Hello, World!
```

Only the whitespace on the right side is removed.

#### Removing Specific Trailing Characters

```python
another_string = "Hello, World!!!"
result = another_string.rstrip("!")

print(result)
```

**Output:**

```text
Hello, World
```

#### Removing Multiple Possible Characters

```python
text = "Hello!?!?"
result = text.rstrip("!?")

print(result)
```

**Output:**

```text
Hello
```

The argument `"!?"` means that any trailing `!` or `?` characters should be removed.

> `rstrip()` removes individual matching characters from the right side. It does not remove an exact suffix as a complete unit.

[Back to Index](#index)

---

<a id="checking-string-content"></a>

## Checking String Content

Python provides methods for checking what types of characters a string contains.

These methods return `True` only when:

* The string is not empty.
* Every character satisfies the method's condition.

<a id="isalpha-method"></a>

### 1. Checking Alphabetic Characters with `isalpha()`

The `isalpha()` method returns `True` when every character in a non-empty string is alphabetic.

#### Letters Only

```python
text = "HelloWorld"

print(text.isalpha())
```

**Output:**

```text
True
```

#### Contains a Space

```python
text = "Hello World"

print(text.isalpha())
```

**Output:**

```text
False
```

A space is not an alphabetic character.

#### Contains Digits

```python
text = "Hello123"

print(text.isalpha())
```

**Output:**

```text
False
```

#### Contains Special Characters

```python
text = "Hello@World"

print(text.isalpha())
```

**Output:**

```text
False
```

#### Empty String

```python
text = ""

print(text.isalpha())
```

**Output:**

```text
False
```

An empty string returns `False` because it contains no alphabetic characters.

> `isalpha()` supports alphabetic Unicode characters, not only the English letters `A–Z` and `a–z`.

For example:

```python
print("नमस्ते".isalpha())
print("Python".isalpha())
```

The exact result depends on how the Unicode text is composed, because some writing systems may contain combining marks.

[Back to Index](#index)

---

<a id="isdigit-method"></a>

### 2. Checking Digit Characters with `isdigit()`

The `isdigit()` method returns `True` when every character in a non-empty string is a digit.

#### Digits Only

```python
number_string = "12345"

print(number_string.isdigit())
```

**Output:**

```text
True
```

#### Mixed Letters and Digits

```python
mixed_string = "12345abc"

print(mixed_string.isdigit())
```

**Output:**

```text
False
```

#### Empty String

```python
empty_string = ""

print(empty_string.isdigit())
```

**Output:**

```text
False
```

#### Contains Spaces

```python
spaced_string = " 12345 "

print(spaced_string.isdigit())
```

**Output:**

```text
False
```

#### Contains a Decimal Point

```python
decimal_string = "12.5"

print(decimal_string.isdigit())
```

**Output:**

```text
False
```

The decimal point is not a digit.

#### Contains a Negative Sign

```python
negative_number = "-25"

print(negative_number.isdigit())
```

**Output:**

```text
False
```

The minus sign is not a digit.

> `isdigit()` recognizes certain Unicode digit characters in addition to the ASCII digits `0–9`.

[Back to Index](#index)

---

<a id="isalnum-method"></a>

### 3. Checking Alphanumeric Characters with `isalnum()`

The `isalnum()` method returns `True` when every character in a non-empty string is either:

* Alphabetic
* Numeric

#### Letters and Numbers

```python
text = "Hello123"

print(text.isalnum())
```

**Output:**

```text
True
```

#### Letters Only

```python
text = "Hello"

print(text.isalnum())
```

**Output:**

```text
True
```

#### Numbers Only

```python
text = "12345"

print(text.isalnum())
```

**Output:**

```text
True
```

#### Contains a Space

```python
text = "Hello 123"

print(text.isalnum())
```

**Output:**

```text
False
```

The space is neither alphabetic nor numeric.

#### Contains Punctuation

```python
text = "Hello!"

print(text.isalnum())
```

**Output:**

```text
False
```

The exclamation mark is not alphanumeric.

#### Empty String

```python
text = ""

print(text.isalnum())
```

**Output:**

```text
False
```

An empty string does not contain any alphanumeric characters.

The `isalnum()` method is useful for basic validation, such as checking whether a username contains only letters and numbers.

```python
username = "User123"

if username.isalnum():
    print("The username is valid.")
else:
    print("The username contains invalid characters.")
```

**Output:**

```text
The username is valid.
```

> Like `isalpha()` and `isdigit()`, `isalnum()` supports applicable Unicode characters and is not limited to English letters and ASCII digits.

[Back to Index](#index)