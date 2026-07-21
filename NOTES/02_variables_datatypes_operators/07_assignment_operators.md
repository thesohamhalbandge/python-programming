<a id="assignment-operators-in-python"></a>

## Assignment Operators in Python

Assignment operators assign values to variables or update values that variables already hold.

<a id="index"></a>

## Index

1. [Simple Assignment (`=`)](#simple-assignment)

   * [Declaring a Variable](#declaring-a-variable)
   * [Reassigning Variables](#reassigning-variables)
   * [Assignment Is Not Equality](#assignment-versus-equality)
2. [Add and Assign (`+=`)](#add-and-assign)
3. [Subtract and Assign (`-=`)](#subtract-and-assign)
4. [Multiply and Assign (`*=`)](#multiply-and-assign)
5. [Divide and Assign (`/=`)](#divide-and-assign)
6. [Floor Divide and Assign (`//=`)](#floor-divide-and-assign)

   * [Floor Division with Negative Numbers](#floor-division-negative-numbers)
   * [Floor Division with Floats](#floor-division-with-floats)
7. [Assignment Operator Summary](#assignment-operator-summary)

---

<a id="simple-assignment"></a>

## Simple Assignment (`=`)

The assignment operator (`=`) assigns a value to a variable.

A variable can be viewed as a name that refers to a value stored in memory. The value on the right side of `=` is evaluated and assigned to the variable on the left side.

### Syntax

```python
variable = value
```

<a id="declaring-a-variable"></a>

### 1. Declaring a Variable

```python
x = 5

print(x)
```

**Output:**

```text
5
```

In this example:

* `x` is the variable name.
* `5` is an integer value.
* `=` assigns the value `5` to `x`.

```python
name = "Alice"
temperature = 28.5
is_active = True

print(name)
print(temperature)
print(is_active)
```

**Output:**

```text
Alice
28.5
True
```

[Back to Index](#index)

---

<a id="reassigning-variables"></a>

### 2. Reassigning Variables

A variable can be assigned a new value after it has been created.

```python
x = 5

print(x)

x = 10

print(x)
```

**Output:**

```text
5
10
```

The second assignment replaces the value previously associated with `x`.

Python is dynamically typed, which means a variable can be reassigned to a value of a different data type.

```python
x = 5
print(x)
print(type(x))

x = 10.5
print(x)
print(type(x))

x = "Hello"
print(x)
print(type(x))
```

**Output:**

```text
5
<class 'int'>
10.5
<class 'float'>
Hello
<class 'str'>
```

The variable `x` first refers to an integer, then a float, and finally a string.

> Although Python allows variables to change data types, repeatedly changing a variable's purpose can make code harder to understand.

[Back to Index](#index)

---

<a id="assignment-versus-equality"></a>

### 3. Assignment Is Not Equality

The assignment operator (`=`) does not check whether two values are equal.

It assigns the value on the right to the variable on the left.

```python
x = 5
```

To compare two values for equality, use the equality operator (`==`).

```python
x = 5

print(x == 5)
print(x == 10)
```

**Output:**

```text
True
False
```

| Operator | Purpose                     |
| -------- | --------------------------- |
| `=`      | Assigns a value             |
| `==`     | Checks whether values match |

[Back to Index](#index)

---

<a id="add-and-assign"></a>

## Add and Assign (`+=`)

The add-and-assign operator (`+=`) adds a value to a variable and assigns the result back to that variable.

### Syntax

```python
variable += value
```

This is generally equivalent to:

```python
variable = variable + value
```

### Example

```python
x = 5
x += 3

print(x)
```

**Output:**

```text
8
```

The operation proceeds as follows:

```text
x = 5
x = x + 3
x = 5 + 3
x = 8
```

The `+=` operator can also be used with compatible data types such as strings.

```python
message = "Hello"
message += " World"

print(message)
```

**Output:**

```text
Hello World
```

For strings, `+=` performs concatenation rather than numerical addition.

[Back to Index](#index)

---

<a id="subtract-and-assign"></a>

## Subtract and Assign (`-=`)

The subtract-and-assign operator (`-=`) subtracts a value from a variable and assigns the result back to that variable.

### Syntax

```python
variable -= value
```

This is generally equivalent to:

```python
variable = variable - value
```

### Example

```python
y = 10
y -= 4

print(y)
```

**Output:**

```text
6
```

The operation proceeds as follows:

```text
y = 10
y = y - 4
y = 10 - 4
y = 6
```

Another example:

```python
balance = 100
balance -= 25

print(balance)
```

**Output:**

```text
75
```

[Back to Index](#index)

---

<a id="multiply-and-assign"></a>

## Multiply and Assign (`*=`)

The multiply-and-assign operator (`*=`) multiplies a variable by a value and assigns the result back to that variable.

### Syntax

```python
variable *= value
```

This is generally equivalent to:

```python
variable = variable * value
```

### Example

```python
z = 3
z *= 2

print(z)
```

**Output:**

```text
6
```

The operation proceeds as follows:

```text
z = 3
z = z * 2
z = 3 * 2
z = 6
```

The `*=` operator can also repeat strings.

```python
text = "Hi "
text *= 3

print(text)
```

**Output:**

```text
Hi Hi Hi 
```

For strings, multiplication repeats the string the specified number of times.

[Back to Index](#index)

---

<a id="divide-and-assign"></a>

## Divide and Assign (`/=`)

The divide-and-assign operator (`/=`) divides a variable by a value and assigns the result back to that variable.

### Syntax

```python
variable /= value
```

This is generally equivalent to:

```python
variable = variable / value
```

### Example

```python
a = 20
a /= 4

print(a)
```

**Output:**

```text
5.0
```

The operation proceeds as follows:

```text
a = 20
a = a / 4
a = 20 / 4
a = 5.0
```

The `/` operator performs standard division and returns a float, even when the division produces a whole-number result.

```python
value = 8
value /= 2

print(value)
print(type(value))
```

**Output:**

```text
4.0
<class 'float'>
```

Division can also produce a fractional result.

```python
value = 5
value /= 2

print(value)
```

**Output:**

```text
2.5
```

### Division by Zero

Dividing by zero raises a `ZeroDivisionError`.

```python
value = 10
value /= 0
```

**Error:**

```text
ZeroDivisionError: division by zero
```

[Back to Index](#index)

---

<a id="floor-divide-and-assign"></a>

## Floor Divide and Assign (`//=`)

The floor-divide-and-assign operator (`//=`) performs floor division and assigns the result back to the variable.

### Syntax

```python
variable //= value
```

This is generally equivalent to:

```python
variable = variable // value
```

Floor division divides two numbers and rounds the result down toward negative infinity.

### Basic Example

```python
x = 10
x //= 3

print(x)
```

**Output:**

```text
3
```

The operation proceeds as follows:

```text
x = 10
x = x // 3
x = 10 // 3
x = 3
```

Normal division produces approximately:

```text
10 / 3 = 3.333...
```

Floor division rounds this result down to `3`.

> Floor division does not simply remove the decimal portion. It rounds the mathematical result down.

<a id="floor-division-negative-numbers"></a>

### 1. Floor Division with Negative Numbers

When the result is negative, floor division rounds toward negative infinity.

```python
x = -10
x //= 3

print(x)
```

**Output:**

```text
-4
```

Normal division produces approximately:

```text
-10 / 3 = -3.333...
```

The nearest lower integer is `-4`, so Python returns `-4`, not `-3`.

[Back to Index](#index)

---

<a id="floor-division-with-floats"></a>

### 2. Floor Division with Floats

Floor division can also be used with floating-point values.

```python
value = 10.0
value //= 3

print(value)
print(type(value))
```

**Output:**

```text
3.0
<class 'float'>
```

The value is rounded down mathematically, but the result remains a float because one of the operands is a float.

Therefore, `//` is more accurately called **floor division**, not integer division.

### Division by Zero

Floor division by zero also raises a `ZeroDivisionError`.

```python
value = 10
value //= 0
```

**Error:**

```text
ZeroDivisionError: integer division or modulo by zero
```

[Back to Index](#index)

---

<a id="assignment-operator-summary"></a>

## Assignment Operator Summary

| Operator | Name                    | Example   | Equivalent operation |
| -------- | ----------------------- | --------- | -------------------- |
| `=`      | Simple assignment       | `x = 5`   | Assigns `5` to `x`   |
| `+=`     | Add and assign          | `x += 3`  | `x = x + 3`          |
| `-=`     | Subtract and assign     | `x -= 3`  | `x = x - 3`          |
| `*=`     | Multiply and assign     | `x *= 3`  | `x = x * 3`          |
| `/=`     | Divide and assign       | `x /= 3`  | `x = x / 3`          |
| `//=`    | Floor divide and assign | `x //= 3` | `x = x // 3`         |

### Combined Example

```python
number = 10

number += 5
print(number)

number -= 3
print(number)

number *= 2
print(number)

number /= 4
print(number)

number //= 2
print(number)
```

**Output:**

```text
15
12
24
6.0
3.0
```

The value becomes a float after `/=`. Therefore, the later `//=` operation also returns a float.

[Back to Index](#index)
