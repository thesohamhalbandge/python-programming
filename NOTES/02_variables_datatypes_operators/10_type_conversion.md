<a id="type-conversion-in-python"></a>

## Type Conversion in Python

Type conversion means changing a value from one data type to another.

Python supports two main forms of type conversion:

1. **Implicit type conversion** — Python performs the conversion automatically.
2. **Explicit type conversion** — You manually convert a value using functions such as `int()`, `float()`, `str()`, and `bool()`.

<a id="index"></a>

## Index

1. [Implicit Type Conversion](#implicit-type-conversion)

   * [Integer and Float](#integer-and-float)
   * [Boolean and Integer](#boolean-and-integer)
   * [Limitations of Implicit Conversion](#implicit-conversion-limitations)
2. [Explicit Type Conversion](#explicit-type-conversion)
3. [Converting Values with `int()`](#int-conversion)

   * [String to Integer](#string-to-integer)
   * [Float to Integer](#float-to-integer)
   * [Boolean to Integer](#boolean-to-integer)
   * [Invalid Integer Conversions](#invalid-integer-conversions)
4. [Converting Values with `float()`](#float-conversion)

   * [String to Float](#string-to-float)
   * [Integer to Float](#integer-to-float)
   * [Boolean to Float](#boolean-to-float)
5. [Converting Values with `str()`](#str-conversion)

   * [Integer to String](#integer-to-string)
   * [Other Values to Strings](#other-values-to-strings)
6. [Converting Values with `bool()`](#bool-conversion)

   * [Truthy Values](#truthy-values)
   * [Falsy Values](#falsy-values)
   * [String Conversion Caution](#boolean-string-caution)
7. [Type Conversion Summary](#type-conversion-summary)

---

<a id="implicit-type-conversion"></a>

## Implicit Type Conversion

Implicit type conversion occurs when Python automatically converts one data type into another during an operation.

This most commonly happens in numeric expressions involving compatible types.

For example, when an integer and a float are used together, Python converts the integer to a float so the operation can be completed.

<a id="integer-and-float"></a>

### 1. Integer and Float

```python
num_int = 10
num_float = 3.5

result = num_int + num_float

print(result)
print(type(result))
```

**Output:**

```text
13.5
<class 'float'>
```

Python treats the integer `10` as the floating-point value `10.0` during the calculation.

The expression is effectively evaluated as:

```text
10.0 + 3.5 = 13.5
```

The resulting value is a float.

```python
print(type(num_int))
print(type(num_float))
```

**Output:**

```text
<class 'int'>
<class 'float'>
```

The original variables are not permanently converted. Only the operation produces a float result.

[Back to Index](#index)

---

<a id="boolean-and-integer"></a>

### 2. Boolean and Integer

In numeric operations:

* `True` behaves like `1`.
* `False` behaves like `0`.

```python
bool_value = True
num_int = 5

total = bool_value + num_int

print(total)
print(type(total))
```

**Output:**

```text
6
<class 'int'>
```

The expression is evaluated as:

```text
True + 5
1 + 5
6
```

Another example:

```python
print(False + 10)
print(True * 4)
```

**Output:**

```text
10
4
```

Although Boolean values can be used numerically, they are generally intended to represent logical states.

[Back to Index](#index)

---

<a id="implicit-conversion-limitations"></a>

### 3. Limitations of Implicit Conversion

Python does not automatically convert all data types.

For example, Python cannot directly add a string and an integer.

```python
age = 25

message = "Age: " + age
```

**Error:**

```text
TypeError: can only concatenate str (not "int") to str
```

The integer must be explicitly converted to a string:

```python
age = 25

message = "Age: " + str(age)

print(message)
```

**Output:**

```text
Age: 25
```

Similarly, Python does not automatically convert numeric strings during arithmetic.

```python
number = "10"

result = number + 5
```

**Error:**

```text
TypeError: can only concatenate str (not "int") to str
```

Convert the string explicitly:

```python
number = "10"

result = int(number) + 5

print(result)
```

**Output:**

```text
15
```

[Back to Index](#index)

---

<a id="explicit-type-conversion"></a>

## Explicit Type Conversion

Explicit type conversion requires you to manually convert a value using a built-in conversion function.

Common conversion functions include:

| Function  | Purpose                                   |
| --------- | ----------------------------------------- |
| `int()`   | Converts a compatible value to an integer |
| `float()` | Converts a compatible value to a float    |
| `str()`   | Converts a value to a string              |
| `bool()`  | Converts a value to a Boolean             |

Explicit conversion is also called **type casting**, although conversion is the more general term.

[Back to Index](#index)

---

<a id="int-conversion"></a>

## Converting Values with `int()`

The `int()` function converts a compatible value into an integer.

### Syntax

```python
int(value)
```

<a id="string-to-integer"></a>

### 1. String to Integer

A string containing a valid whole number can be converted to an integer.

```python
num_string = "100"
num_integer = int(num_string)

print(num_integer)
print(type(num_integer))
```

**Output:**

```text
100
<class 'int'>
```

The original string remains unchanged:

```python
print(num_string)
print(type(num_string))
```

**Output:**

```text
100
<class 'str'>
```

Negative integer strings are also supported.

```python
value = "-25"

print(int(value))
```

**Output:**

```text
-25
```

[Back to Index](#index)

---

<a id="float-to-integer"></a>

### 2. Float to Integer

The `int()` function converts a float to an integer by removing its fractional portion.

```python
num_float = 3.99
num_integer = int(num_float)

print(num_integer)
print(type(num_integer))
```

**Output:**

```text
3
<class 'int'>
```

The conversion truncates toward zero. It does not round to the nearest integer.

```python
print(int(4.9))
print(int(-4.9))
```

**Output:**

```text
4
-4
```

Therefore:

```text
int(4.9)  → 4
int(-4.9) → -4
```

> Use `round()` when rounding is required. Use `int()` when truncation toward zero is required.

[Back to Index](#index)

---

<a id="boolean-to-integer"></a>

### 3. Boolean to Integer

Boolean values can be converted to integers.

```python
print(int(True))
print(int(False))
```

**Output:**

```text
1
0
```

The conversions are:

```text
True  → 1
False → 0
```

[Back to Index](#index)

---

<a id="invalid-integer-conversions"></a>

### 4. Invalid Integer Conversions

A string must contain a valid integer representation.

```python
value = "hello"

print(int(value))
```

**Error:**

```text
ValueError: invalid literal for int() with base 10: 'hello'
```

A decimal string also cannot be passed directly to `int()`.

```python
value = "3.99"

print(int(value))
```

**Error:**

```text
ValueError: invalid literal for int() with base 10: '3.99'
```

Convert it to a float first, then to an integer:

```python
value = "3.99"

result = int(float(value))

print(result)
```

**Output:**

```text
3
```

The conversions occur in two steps:

```text
"3.99" → 3.99 → 3
```

[Back to Index](#index)

---

<a id="float-conversion"></a>

## Converting Values with `float()`

The `float()` function converts a compatible value into a floating-point number.

### Syntax

```python
float(value)
```

<a id="string-to-float"></a>

### 1. String to Float

A string containing a valid numeric value can be converted to a float.

```python
data_string = "45.67"
data_float = float(data_string)

print(data_float)
print(type(data_float))
```

**Output:**

```text
45.67
<class 'float'>
```

A string containing a whole number can also be converted:

```python
value = "10"

print(float(value))
```

**Output:**

```text
10.0
```

Scientific notation is supported:

```python
value = "5e3"

print(float(value))
```

**Output:**

```text
5000.0
```

[Back to Index](#index)

---

<a id="integer-to-float"></a>

### 2. Integer to Float

```python
num_integer = 5
num_float = float(num_integer)

print(num_float)
print(type(num_float))
```

**Output:**

```text
5.0
<class 'float'>
```

The numerical value remains equivalent, but the resulting type is `float`.

[Back to Index](#index)

---

<a id="boolean-to-float"></a>

### 3. Boolean to Float

```python
print(float(True))
print(float(False))
```

**Output:**

```text
1.0
0.0
```

The conversions are:

```text
True  → 1.0
False → 0.0
```

[Back to Index](#index)

---

<a id="str-conversion"></a>

## Converting Values with `str()`

The `str()` function converts a value into its string representation.

### Syntax

```python
str(value)
```

<a id="integer-to-string"></a>

### 1. Integer to String

```python
age = 30
age_string = str(age)

print(age_string)
print(type(age_string))
```

**Output:**

```text
30
<class 'str'>
```

The quotation marks are not displayed by `print()`. They indicate that the value is stored as a string.

Use `repr()` to display the representation more clearly:

```python
print(repr(age_string))
```

**Output:**

```text
'30'
```

The converted value can now be concatenated with another string.

```python
age = 30

message = "Age: " + str(age)

print(message)
```

**Output:**

```text
Age: 30
```

[Back to Index](#index)

---

<a id="other-values-to-strings"></a>

### 2. Other Values to Strings

Floats and Boolean values can also be converted to strings.

```python
price = 19.99
is_available = True

price_string = str(price)
availability_string = str(is_available)

print(price_string)
print(availability_string)

print(type(price_string))
print(type(availability_string))
```

**Output:**

```text
19.99
True
<class 'str'>
<class 'str'>
```

Lists and other objects can also be converted to string representations.

```python
numbers = [1, 2, 3]
numbers_string = str(numbers)

print(numbers_string)
print(type(numbers_string))
```

**Output:**

```text
[1, 2, 3]
<class 'str'>
```

[Back to Index](#index)

---

<a id="bool-conversion"></a>

## Converting Values with `bool()`

The `bool()` function converts a value into either `True` or `False`.

### Syntax

```python
bool(value)
```

Python determines the result based on whether the value is considered **truthy** or **falsy**.

<a id="truthy-values"></a>

### 1. Truthy Values

Most non-empty and non-zero values are truthy.

```python
print(bool(1))
print(bool(-10))
print(bool(3.14))
print(bool("Python"))
print(bool([1, 2]))
```

**Output:**

```text
True
True
True
True
True
```

Examples of truthy values include:

* Non-zero integers
* Non-zero floats
* Non-empty strings
* Non-empty lists
* Non-empty tuples
* Non-empty dictionaries
* Most objects

[Back to Index](#index)

---

<a id="falsy-values"></a>

### 2. Falsy Values

Common falsy values include:

* `False`
* `None`
* `0`
* `0.0`
* `""`
* `[]`
* `()`
* `{}`
* `set()`

```python
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
```

**Output:**

```text
False
False
False
False
False
False
```

An empty value is generally considered false in a Boolean context.

[Back to Index](#index)

---

<a id="boolean-string-caution"></a>

### 3. String Conversion Caution

Any non-empty string is truthy, even when the string contains the word `"False"` or the character `"0"`.

```python
print(bool("False"))
print(bool("0"))
print(bool(" "))
```

**Output:**

```text
True
True
True
```

These strings are truthy because they contain characters.

Only an empty string converts to `False`:

```python
print(bool(""))
```

**Output:**

```text
False
```

To convert text such as `"true"` or `"false"` into a meaningful Boolean value, compare the normalized string explicitly.

```python
user_input = "false"

result = user_input.strip().lower() == "true"

print(result)
```

**Output:**

```text
False
```

Another example:

```python
user_input = " YES "

result = user_input.strip().lower() in ("yes", "true", "1")

print(result)
```

**Output:**

```text
True
```

[Back to Index](#index)

---

<a id="type-conversion-summary"></a>

## Type Conversion Summary

| Conversion                  | Example          | Result  |
| --------------------------- | ---------------- | ------- |
| Integer to float            | `float(5)`       | `5.0`   |
| Float to integer            | `int(3.99)`      | `3`     |
| String to integer           | `int("100")`     | `100`   |
| String to float             | `float("45.67")` | `45.67` |
| Integer to string           | `str(30)`        | `"30"`  |
| Boolean to integer          | `int(True)`      | `1`     |
| Integer to Boolean          | `bool(1)`        | `True`  |
| Zero to Boolean             | `bool(0)`        | `False` |
| Empty string to Boolean     | `bool("")`       | `False` |
| Non-empty string to Boolean | `bool("False")`  | `True`  |

### Combined Example

```python
user_input = "25"

age = int(user_input)
age_as_float = float(age)
age_as_string = str(age_as_float)
is_non_zero = bool(age)

print(age)
print(type(age))

print(age_as_float)
print(type(age_as_float))

print(age_as_string)
print(type(age_as_string))

print(is_non_zero)
print(type(is_non_zero))
```

**Output:**

```text
25
<class 'int'>
25.0
<class 'float'>
25.0
<class 'str'>
True
<class 'bool'>
```

[Back to Index](#index)