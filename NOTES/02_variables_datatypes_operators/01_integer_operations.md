## Integers in Python

### 1. Declaring Integers

An integer is a whole number without a decimal point. To declare an integer, assign a whole-number value to a variable.

```python
positive_temperature = 25   # Holds a positive integer
negative_temperature = -50  # Holds a negative integer
zero_temperature = 0        # Holds zero
```

### 2. Large Integers

Python supports integers that can grow beyond the fixed-size limits used by many other programming languages.

```python
large_number = 123456789012345678901234567890
```

Python allocates additional memory as the integer grows. The practical limit depends on the available system memory.

### 3. Verifying the Integer Type

Use the `type()` function to check the data type of a variable.

```python
age = 30

print(type(age))
```

**Output:**

```text
<class 'int'>
```

---

## Addition

The addition operator (`+`) adds two or more numbers.

### 1. Adding Multiple Numbers

```python
a = 2
b = 4
c = 6

result = a + b + c

print(result)
```

**Output:**

```text
12
```

### 2. Mixing Variables and Literals

A **literal** is a fixed value written directly in the code.

```python
a = 2

result = 10 + a

print(result)
```

**Output:**

```text
12
```

In this example, `10` is an integer literal, while `a` is a variable.

---

## Subtraction

The subtraction operator (`-`) calculates the difference between two numbers.

### 1. Basic Subtraction

```python
result = 10 - 4

print(result)
```

**Output:**

```text
6
```

### 2. Subtracting Variables

```python
a = 15
b = 5

difference = a - b

print(difference)
```

**Output:**

```text
10
```

The value stored in `b` is subtracted from the value stored in `a`.

---

## Multiplication

The multiplication operator (`*`) multiplies two numbers.

### 1. Simple Multiplication

```python
result = 5 * 6

print(result)
```

**Output:**

```text
30
```

Here, `5` multiplied by `6` equals `30`.

### 2. Multiplying Variables

```python
a = 10
b = 2

product = a * b

print(product)
```

**Output:**

```text
20
```

The variable `a` holds `10`, and `b` holds `2`, so `a * b` evaluates to `20`.

---

## Floor Division

The floor division operator (`//`) divides two numbers and rounds the result down to the nearest whole number.

### 1. Basic Floor Division

```python
result = 7 // 2

print(result)
```

**Output:**

```text
3
```

Normal division gives:

```text
7 ÷ 2 = 3.5
```

Floor division rounds `3.5` down to `3`.

### 2. Floor Division with Negative Numbers

```python
result = -10 // 3

print(result)
```

**Output:**

```text
-4
```

Normal division gives approximately:

```text
-10 ÷ 3 = -3.333...
```

Python rounds the result down toward negative infinity. Therefore, the result is `-4`, not `-3`.

> Floor division does not simply remove the decimal portion. It always rounds the result down.

---

## Modulus Operation

The modulus operator (`%`) returns the remainder after division.

For example:

```text
7 ÷ 2 = quotient 3, remainder 1
```

### 1. Basic Modulus Operation

```python
result = 7 % 2

print(result)
```

**Output:**

```text
1
```

### 2. Negative Dividend

When the divisor is positive, the remainder is non-negative.

```python
result = -10 % 3

print(result)
```

**Output:**

```text
2
```

Python follows this relationship:

```text
dividend = divisor × quotient + remainder
```

For this example:

```text
-10 = 3 × (-4) + 2
```

Therefore, the remainder is `2`.

### 3. Negative Divisor

The remainder has the same sign as the divisor.

```python
result = 10 % -3

print(result)
```

**Output:**

```text
-2
```

The calculation follows this relationship:

```text
10 = (-3) × (-4) + (-2)
```

Therefore, the remainder is `-2`.

### 4. Checking Even and Odd Numbers

The modulus operator is commonly used to determine whether a number is even or odd.

```python
number = 8

print(number % 2)
```

**Output:**

```text
0
```

A number is even when dividing it by `2` produces a remainder of `0`.

---

## Exponentiation

The exponentiation operator (`**`) raises one number, called the **base**, to the power of another number, called the **exponent**.

### 1. Positive Exponent

```python
result = 2 ** 3

print(result)
```

This calculation is equivalent to:

```text
2 × 2 × 2 = 8
```

**Output:**

```text
8
```

### 2. Negative Exponent

A negative exponent returns the reciprocal of the corresponding positive exponent.

```python
result = 2 ** -3

print(result)
```

This calculation is equivalent to:

```text
1 ÷ (2 × 2 × 2) = 1 ÷ 8 = 0.125
```

**Output:**

```text
0.125
```

### 3. Special Cases

* **Zero exponent:** `x ** 0` returns `1` for any non-zero value of `x`.
* **Exponent of one:** `x ** 1` returns `x`.

```python
print(5 ** 0)
print(5 ** 1)
```

**Output:**

```text
1
5
```

---

## Operator Precedence

Operator precedence determines the order in which Python evaluates operations in an expression.

When several operators appear in the same expression, Python follows a defined order.

### Precedence Rules

From highest to lowest:

1. Parentheses: `()`
2. Exponentiation: `**`
3. Multiplication, division, floor division, and modulus: `*`, `/`, `//`, `%`
4. Addition and subtraction: `+`, `-`

### Example 1: Without Parentheses

```python
result_without_parentheses = 2 + 3 * 4

print(result_without_parentheses)
```

**Output:**

```text
14
```

Python evaluates the multiplication first:

```text
2 + 3 × 4
2 + 12
14
```

### Example 2: With Parentheses

```python
result_with_parentheses = (2 + 3) * 4

print(result_with_parentheses)
```

**Output:**

```text
20
```

The parentheses force Python to perform the addition first:

```text
(2 + 3) × 4
5 × 4
20
```

> Use parentheses when you want to make the intended order of operations explicit.