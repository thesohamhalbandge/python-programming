<a id="comparison-operators-in-python"></a>

## Comparison Operators in Python

Comparison operators compare two or more values and return a Boolean result:

* `True`
* `False`

They are commonly used in conditions, validation, filtering, sorting, and decision-making.

<a id="index"></a>

## Index

1. [Equal To (`==`)](#equal-to)
2. [Not Equal To (`!=`)](#not-equal-to)
3. [Greater Than (`>`)](#greater-than)
4. [Less Than (`<`)](#less-than)
5. [Greater Than or Equal To (`>=`)](#greater-than-or-equal-to)
6. [Less Than or Equal To (`<=`)](#less-than-or-equal-to)
7. [Comparing Different Data Types](#comparing-different-data-types)
8. [Chained Comparisons](#chained-comparisons)

   * [Ascending Range Check](#ascending-range-check)
   * [Descending Comparison](#descending-comparison)
   * [Mixed Comparison Operators](#mixed-comparison-operators)
9. [Comparison Operator Summary](#comparison-operator-summary)

---

<a id="equal-to"></a>

## Equal To (`==`)

The equality operator (`==`) checks whether two values are equal.

It returns:

* `True` when the values are equal.
* `False` when the values are different.

### Syntax

```python
left_value == right_value
```

### Example

```python
a = 5
b = 5
c = 10

print(a == b)
print(a == c)
```

**Output:**

```text
True
False
```

The comparisons are evaluated as follows:

```text
5 == 5  → True
5 == 10 → False
```

### Comparing Strings

String comparisons are case-sensitive.

```python
word1 = "Python"
word2 = "Python"
word3 = "python"

print(word1 == word2)
print(word1 == word3)
```

**Output:**

```text
True
False
```

`"Python"` and `"python"` are different because their capitalization does not match.

> The equality operator (`==`) compares values. The assignment operator (`=`) assigns a value to a variable.

```python
x = 5       # Assignment
print(x == 5)  # Comparison
```

**Output:**

```text
True
```

[Back to Index](#index)

---

<a id="not-equal-to"></a>

## Not Equal To (`!=`)

The not-equal operator (`!=`) checks whether two values are different.

It returns:

* `True` when the values are different.
* `False` when the values are equal.

### Syntax

```python
left_value != right_value
```

### Example

```python
x = 8
y = 12

print(x != y)
print(x != 8)
```

**Output:**

```text
True
False
```

The comparisons are evaluated as follows:

```text
8 != 12 → True
8 != 8  → False
```

### Comparing Strings

```python
username = "Alice"

print(username != "Bob")
print(username != "Alice")
```

**Output:**

```text
True
False
```

[Back to Index](#index)

---

<a id="greater-than"></a>

## Greater Than (`>`)

The greater-than operator (`>`) checks whether the value on the left is greater than the value on the right.

It returns:

* `True` when the left value is greater.
* `False` when the left value is smaller or equal.

### Syntax

```python
left_value > right_value
```

### Example

```python
a = 10
b = 5
c = 10

print(a > b)
print(b > a)
print(a > c)
```

**Output:**

```text
True
False
False
```

The comparisons are evaluated as follows:

```text
10 > 5  → True
5 > 10  → False
10 > 10 → False
```

The final comparison returns `False` because the values are equal. The `>` operator checks only whether the left value is strictly greater.

[Back to Index](#index)

---

<a id="less-than"></a>

## Less Than (`<`)

The less-than operator (`<`) checks whether the value on the left is smaller than the value on the right.

It returns:

* `True` when the left value is smaller.
* `False` when the left value is greater or equal.

### Syntax

```python
left_value < right_value
```

### Example

```python
x = 3
y = 8
z = 3

print(x < y)
print(y < x)
print(x < z)
```

**Output:**

```text
True
False
False
```

The comparisons are evaluated as follows:

```text
3 < 8 → True
8 < 3 → False
3 < 3 → False
```

The final comparison returns `False` because the values are equal.

[Back to Index](#index)

---

<a id="greater-than-or-equal-to"></a>

## Greater Than or Equal To (`>=`)

The greater-than-or-equal-to operator (`>=`) checks whether the value on the left is either:

* Greater than the value on the right
* Equal to the value on the right

### Syntax

```python
left_value >= right_value
```

### Example

```python
a = 10
b = 5
c = 10

print(a >= b)
print(a >= c)
print(b >= a)
```

**Output:**

```text
True
True
False
```

The comparisons are evaluated as follows:

```text
10 >= 5  → True
10 >= 10 → True
5 >= 10  → False
```

Unlike `>`, the `>=` operator returns `True` when both values are equal.

[Back to Index](#index)

---

<a id="less-than-or-equal-to"></a>

## Less Than or Equal To (`<=`)

The less-than-or-equal-to operator (`<=`) checks whether the value on the left is either:

* Less than the value on the right
* Equal to the value on the right

### Syntax

```python
left_value <= right_value
```

### Example

```python
x = 3
y = 8
z = 3

print(x <= y)
print(x <= z)
print(y <= x)
```

**Output:**

```text
True
True
False
```

The comparisons are evaluated as follows:

```text
3 <= 8 → True
3 <= 3 → True
8 <= 3 → False
```

Unlike `<`, the `<=` operator returns `True` when both values are equal.

[Back to Index](#index)

---

<a id="comparing-different-data-types"></a>

## Comparing Different Data Types

Some values of different data types can be compared, while others cannot.

### Integers and Floats

Python can compare integers and floats numerically.

```python
integer_value = 5
float_value = 5.0

print(integer_value == float_value)
print(integer_value < 5.5)
```

**Output:**

```text
True
True
```

Although `5` is an integer and `5.0` is a float, they represent the same numerical value.

### Booleans and Integers

Because `True` behaves like `1` and `False` behaves like `0`, they can compare as equal.

```python
print(True == 1)
print(False == 0)
```

**Output:**

```text
True
True
```

### Incompatible Types

Ordering comparisons between incompatible types usually raise a `TypeError`.

```python
print(5 > "3")
```

**Error:**

```text
TypeError: '>' not supported between instances of 'int' and 'str'
```

Convert the values to compatible types before comparing them.

```python
number = 5
text_number = "3"

print(number > int(text_number))
```

**Output:**

```text
True
```

Equality comparisons between unrelated types normally return `False` instead of raising an error.

```python
print(5 == "5")
```

**Output:**

```text
False
```

The integer `5` and the string `"5"` are different values with different data types.

[Back to Index](#index)

---

<a id="chained-comparisons"></a>

## Chained Comparisons

Python allows multiple comparison operators to be combined in one expression.

### General Form

```python
first_value < second_value < third_value
```

A chained comparison is equivalent to combining individual comparisons with `and`.

```python
a < b < c
```

is equivalent to:

```python
a < b and b < c
```

The middle expression is evaluated only once in a chained comparison.

<a id="ascending-range-check"></a>

### 1. Ascending Range Check

```python
age = 25

print(18 <= age <= 60)
```

**Output:**

```text
True
```

This expression checks both conditions:

```text
18 <= age → True
age <= 60 → True
```

It is equivalent to:

```python
print(18 <= age and age <= 60)
```

**Output:**

```text
True
```

Chained comparisons are particularly useful for checking whether a value lies within a range.

```python
temperature = 28

if 20 <= temperature <= 30:
    print("The temperature is within the expected range.")
```

**Output:**

```text
The temperature is within the expected range.
```

[Back to Index](#index)

---

<a id="descending-comparison"></a>

### 2. Descending Comparison

```python
a = 10
b = 7
c = 3

print(a > b > c)
```

**Output:**

```text
True
```

The expression checks:

```text
10 > 7 → True
7 > 3  → True
```

It is equivalent to:

```python
print(a > b and b > c)
```

**Output:**

```text
True
```

[Back to Index](#index)

---

<a id="mixed-comparison-operators"></a>

### 3. Mixed Comparison Operators

Different comparison operators can appear in the same chain.

```python
a = 5
b = 3
c = 2

print(b < a > c)
```

**Output:**

```text
True
```

The expression checks:

```text
b < a → 3 < 5 → True
a > c → 5 > 2 → True
```

Therefore:

```text
3 < 5 > 2 → True
```

This is equivalent to:

```python
print(b < a and a > c)
```

Another example combines equality and inequality:

```python
a = 5
b = 5
c = 10

print(a == b != c)
```

**Output:**

```text
True
```

The expression checks:

```text
a == b → 5 == 5  → True
b != c → 5 != 10 → True
```

It is equivalent to:

```python
print(a == b and b != c)
```

> `a == b != c` does not directly compare `a` with `c`. It checks `a == b` and `b != c`.

### Failed Chained Comparison

```python
a = 2
b = 5
c = 4

print(a < b < c)
```

**Output:**

```text
False
```

The comparisons are:

```text
2 < 5 → True
5 < 4 → False
```

Because one comparison is `False`, the entire chained comparison returns `False`.

[Back to Index](#index)

---

<a id="comparison-operator-summary"></a>

## Comparison Operator Summary

| Operator | Name                     | Example  | Result condition                    |
| -------- | ------------------------ | -------- | ----------------------------------- |
| `==`     | Equal to                 | `a == b` | `True` when both values are equal   |
| `!=`     | Not equal to             | `a != b` | `True` when the values differ       |
| `>`      | Greater than             | `a > b`  | `True` when `a` is greater          |
| `<`      | Less than                | `a < b`  | `True` when `a` is smaller          |
| `>=`     | Greater than or equal to | `a >= b` | `True` when `a` is greater or equal |
| `<=`     | Less than or equal to    | `a <= b` | `True` when `a` is smaller or equal |

### Combined Example

```python
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

**Output:**

```text
False
True
True
False
True
False
```

[Back to Index](#index)