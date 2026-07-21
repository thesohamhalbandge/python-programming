## Floating-Point Numbers in Python

A **float**, short for **floating-point number**, represents numbers that may contain a decimal point.

Floats are commonly used for:

* Measurements
* Percentages
* Scientific calculations
* Statistical calculations
* Approximate numerical values

> Floats are not ideal for calculations that require exact decimal precision, such as financial accounting. For those cases, Python’s `decimal` module is usually more appropriate.

---

## Declaring Floats

### 1. Direct Assignment

Include a decimal point when assigning a floating-point value.

```python
pi_value = 3.14
temperature = -12.5
zero_float = 0.0
```

### 2. Using the `float()` Function

The `float()` function can convert integers and compatible strings into floating-point numbers.

```python
converted_integer = float(5)
converted_string = float("3.14")

print(converted_integer)
print(converted_string)
```

**Output:**

```text
5.0
3.14
```

> Writing `10` creates an integer, while writing `10.0` creates a float.

### 3. Verifying the Float Type

Use the `type()` function to confirm that a value is a float.

```python
price = 49.99

print(type(price))
```

**Output:**

```text
<class 'float'>
```

---

## Float Addition and Subtraction

Use the addition operator (`+`) to add floating-point numbers and the subtraction operator (`-`) to subtract them.

```python
num1 = 4.5
num2 = 3.2

addition_result = num1 + num2
subtraction_result = num1 - num2

print(addition_result)
print(subtraction_result)
```

**Output:**

```text
7.7
1.2999999999999998
```

The subtraction result may contain additional decimal digits because floating-point values are stored using binary representation.

### Mixing Integers and Floats

Python automatically converts an integer to a float when both types are used in the same arithmetic expression.

```python
num1 = 5    # Integer
num2 = 2.5  # Float

result = num1 + num2

print(result)
print(type(result))
```

**Output:**

```text
7.5
<class 'float'>
```

---

## Float Multiplication

Use the multiplication operator (`*`) to multiply floating-point numbers.

```python
float_number1 = 2.5
float_number2 = 4.0

result = float_number1 * float_number2

print(result)
```

**Output:**

```text
10.0
```

### Result Type

Multiplying two floats produces a float, even when the result represents a whole number.

```python
result = 2.0 * 5.0

print(result)
print(type(result))
```

**Output:**

```text
10.0
<class 'float'>
```

### Precision Considerations

Some multiplication operations may produce small rounding differences.

```python
result = 1.1 * 3

print(result)
```

**Output:**

```text
3.3000000000000003
```

---

## Float Division

The division operator (`/`) performs standard division and always returns a float.

### Dividing Two Integers

```python
result = 8 / 2

print(result)
```

**Output:**

```text
4.0
```

Even though both operands are integers, the `/` operator returns a float.

### Division with a Decimal Result

```python
result = 5 / 2

print(result)
```

**Output:**

```text
2.5
```

### Float Division Compared with Floor Division

```python
print(5 / 2)
print(5 // 2)
```

**Output:**

```text
2.5
2
```

* `/` performs standard division.
* `//` performs floor division and rounds the result down.

---

## Floating-Point Precision

Python floats are stored using binary floating-point representation. Many decimal fractions cannot be represented exactly in binary.

### Example of Floating-Point Inaccuracy

```python
result = 0.1 + 0.2

print(result)
```

**Output:**

```text
0.30000000000000004
```

Although the expected mathematical result is `0.3`, the stored floating-point approximation contains a very small difference.

---

## Rounding Floats

Rounding is useful when a result should contain a limited number of decimal places.

### Using the `round()` Function

The basic syntax is:

```python
round(number, ndigits)
```

* `number` is the value to round.
* `ndigits` is the number of decimal places to retain.
* `ndigits` is optional.

### 1. Rounding to the Nearest Integer

```python
number = 4.6

result = round(number)

print(result)
```

**Output:**

```text
5
```

When `ndigits` is omitted, `round()` returns the nearest integer.

### 2. Rounding to Decimal Places

```python
number = 4.5678

result = round(number, 2)

print(result)
```

**Output:**

```text
4.57
```

### 3. Rounding Halfway Values

Python uses **round half to even**, sometimes called **banker’s rounding**, for exact halfway values.

```python
print(round(4.5))
print(round(5.5))
```

**Output:**

```text
4
6
```

In each case, Python rounds to the nearest even integer.

> Because many decimal values are not represented exactly as floats, some rounding results may appear unexpected.

---

## Formatting Floats for Display

Formatting controls how a float appears without necessarily changing the original value.

### Displaying a Fixed Number of Decimal Places

```python
pi = 3.1415926535

formatted_pi = f"{pi:.2f}"

print(formatted_pi)
```

**Output:**

```text
3.14
```

The `.2f` format specifier displays the value using two digits after the decimal point.

### Formatting Directly Inside `print()`

```python
price = 19.4567

print(f"{price:.2f}")
```

**Output:**

```text
19.46
```

### Formatting Versus Rounding

```python
value = 3.14159

rounded_value = round(value, 2)
formatted_value = f"{value:.2f}"

print(rounded_value)
print(type(rounded_value))

print(formatted_value)
print(type(formatted_value))
```

**Output:**

```text
3.14
<class 'float'>
3.14
<class 'str'>
```

* `round()` returns a numerical value.
* An f-string with `.2f` returns a formatted string.

---

## Handling Float Precision

### 1. Using `round()`

Use `round()` when a numerical result should be reduced to a specific number of decimal places.

```python
value = 0.1 + 0.2
rounded_value = round(value, 2)

print(rounded_value)
```

**Output:**

```text
0.3
```

### 2. Formatting for Display

Use formatting when only the displayed output needs to be limited.

```python
value = 0.1 + 0.2

print(f"{value:.2f}")
```

**Output:**

```text
0.30
```

The original value remains unchanged.

### 3. Using `Decimal` for Exact Decimal Arithmetic

For calculations requiring exact decimal representation, use the `Decimal` class from Python’s `decimal` module.

```python
from decimal import Decimal

result = Decimal("0.1") + Decimal("0.2")

print(result)
```

**Output:**

```text
0.3
```

Strings are passed to `Decimal` so the decimal values are preserved exactly.

---

## Scientific Notation

Scientific notation provides a compact way to represent very large or very small numbers.

For example:

```text
5 × 10³ = 5000
```

Python uses the letter `e` or `E` to represent powers of ten.

### 1. Declaring Floats with Scientific Notation

```python
big_number = 5e3
small_number = 2.5e-4

print(big_number)
print(small_number)
```

**Output:**

```text
5000.0
0.00025
```

The expressions mean:

```text
5e3 = 5 × 10³
2.5e-4 = 2.5 × 10⁻⁴
```

Values written using scientific notation are floats.

### 2. Performing Arithmetic Operations

```python
result = 2e2 + 3e3

print(result)
```

The expression is equivalent to:

```text
200 + 3000 = 3200
```

**Output:**

```text
3200.0
```

### 3. Rounding Scientific-Notation Values

```python
precise_number = 2.34567e2
rounded_number = round(precise_number, 2)

print(precise_number)
print(rounded_number)
```

**Output:**

```text
234.567
234.57
```

### 4. Formatting Output in Scientific Notation

Use the `e` format specifier to display a value in scientific notation.

```python
large_value = 1234567890

formatted_value = f"{large_value:.3e}"

print(formatted_value)
```

**Output:**

```text
1.235e+09
```

The `.3e` format specifier means:

* Display the value in scientific notation.
* Show three digits after the decimal point.

### 5. Using Uppercase Scientific Notation

Use `E` instead of `e` to display an uppercase exponent indicator.

```python
value = 123456

print(f"{value:.2E}")
```

**Output:**

```text
1.23E+05
```