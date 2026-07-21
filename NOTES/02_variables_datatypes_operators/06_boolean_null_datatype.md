<a id="booleans-and-none-in-python"></a>

## Booleans and `None` in Python

Python provides the Boolean values `True` and `False` for representing logical states.

Python also provides `None`, which represents the absence of a value.

<a id="index"></a>

## Index

1. [Booleans in Python](#booleans-in-python)

   * [Declaring Boolean Variables](#declaring-boolean-variables)
   * [Verifying the Boolean Type](#verifying-boolean-type)
   * [Booleans in Numeric Operations](#booleans-in-numeric-operations)
   * [Boolean Comparisons](#boolean-comparisons)
   * [Boolean Values in Conditions](#boolean-values-in-conditions)
2. [`None` in Python](#none-in-python)

   * [Declaring a Variable as `None`](#declaring-none)
   * [Verifying the `None` Type](#verifying-none-type)
   * [Comparing Values with `None`](#comparing-with-none)
   * [Placeholder Values](#placeholder-values)
   * [Clearing a Value](#clearing-a-value)

---

<a id="booleans-in-python"></a>

## Booleans in Python

A Boolean represents one of two logical values:

* `True`
* `False`

Boolean values are commonly used in comparisons, conditions, validation, and decision-making.

Python's `bool` type is a subclass of `int`. Therefore, Boolean values can also be used in numeric operations:

* `True` behaves like `1`.
* `False` behaves like `0`.

> Boolean values should usually be used for logical operations, even though Python allows them in arithmetic expressions.

<a id="declaring-boolean-variables"></a>

### 1. Declaring Boolean Variables

Boolean values must begin with uppercase letters.

```python
is_active = True
is_logged_in = False

print(is_active)
print(is_logged_in)
```

**Output:**

```text
True
False
```

The lowercase values `true` and `false` are not valid Boolean constants in Python.

```python
is_active = true
```

**Error:**

```text
NameError: name 'true' is not defined
```

[Back to Index](#index)

---

<a id="verifying-boolean-type"></a>

### 2. Verifying the Boolean Type

Use the `type()` function to confirm that a value is Boolean.

```python
is_active = True

print(type(is_active))
```

**Output:**

```text
<class 'bool'>
```

Both `True` and `False` belong to the `bool` type.

```python
print(type(True))
print(type(False))
```

**Output:**

```text
<class 'bool'>
<class 'bool'>
```

[Back to Index](#index)

---

<a id="booleans-in-numeric-operations"></a>

### 3. Booleans in Numeric Operations

Because Boolean values behave like `1` and `0` in arithmetic expressions, they can be added, subtracted, or multiplied.

```python
print(True + True)
print(False + True)
print(False * 5)
```

**Output:**

```text
2
1
0
```

The calculations are equivalent to:

```text
True + True  = 1 + 1 = 2
False + True = 0 + 1 = 1
False * 5    = 0 * 5 = 0
```

Another example:

```python
print(True * 10)
print(True - False)
```

**Output:**

```text
10
1
```

Boolean arithmetic can be useful when counting how many conditions are true.

```python
condition1 = True
condition2 = False
condition3 = True

true_count = condition1 + condition2 + condition3

print(true_count)
```

**Output:**

```text
2
```

Two of the three conditions are `True`.

[Back to Index](#index)

---

<a id="boolean-comparisons"></a>

### 4. Boolean Comparisons

Comparison operations return Boolean values.

```python
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)
```

**Output:**

```text
True
False
True
False
```

Common comparison operators include:

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

[Back to Index](#index)

---

<a id="boolean-values-in-conditions"></a>

### 5. Boolean Values in Conditions

Boolean values are commonly used with `if` statements.

```python
is_logged_in = True

if is_logged_in:
    print("Welcome back!")
```

**Output:**

```text
Welcome back!
```

When the condition is `False`, the indented block is skipped.

```python
is_logged_in = False

if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.")
```

**Output:**

```text
Please log in.
```

[Back to Index](#index)

---

<a id="none-in-python"></a>

## `None` in Python

`None` is a special constant that represents the absence of a value.

It is commonly used when:

* A value has not been assigned yet.
* A function has no meaningful result to return.
* A variable needs to be reset.
* An optional value is missing.

`None` is different from:

* `False`
* `0`
* `""`
* `[]`

These values may be considered false in conditions, but they are not the same as `None`.

<a id="declaring-none"></a>

### 1. Declaring a Variable as `None`

Assign `None` directly to a variable.

```python
value = None

print(value)
```

**Output:**

```text
None
```

Like `True` and `False`, `None` must begin with an uppercase letter.

```python
value = none
```

**Error:**

```text
NameError: name 'none' is not defined
```

[Back to Index](#index)

---

<a id="verifying-none-type"></a>

### 2. Verifying the `None` Type

Use `type()` to check the type of `None`.

```python
value = None

print(type(value))
```

**Output:**

```text
<class 'NoneType'>
```

`None` is the only instance of `NoneType`.

[Back to Index](#index)

---

<a id="comparing-with-none"></a>

### 3. Comparing Values with `None`

Use the identity operator `is` to check whether a value is `None`.

```python
value = None

print(value is None)
```

**Output:**

```text
True
```

Use `is not` to check that a value is not `None`.

```python
value = "Python"

print(value is not None)
```

**Output:**

```text
True
```

The recommended form is:

```python
if value is None:
    print("No value is available.")
```

Avoid using `==` when checking for `None`.

```python
if value == None:
    print("No value is available.")
```

Although this may work in simple cases, `is None` is the standard and safer approach because it checks object identity.

### `None` Compared with Other Values

```python
print(None == False)
print(None == 0)
print(None == "")
print(None == None)
```

**Output:**

```text
False
False
False
True
```

`None` is not equal to `False`, zero, or an empty string. It is equal only to itself.

[Back to Index](#index)

---

<a id="placeholder-values"></a>

### 4. Placeholder Values

A variable can be assigned `None` when its actual value will be provided later.

```python
user_name = None

print(user_name)
```

**Output:**

```text
None
```

The variable can later be assigned a meaningful value.

```python
user_name = None

# A value is assigned later
user_name = "Alice"

print(user_name)
```

**Output:**

```text
Alice
```

This makes it clear that the variable exists but does not yet contain meaningful data.

[Back to Index](#index)

---

<a id="clearing-a-value"></a>

### 5. Clearing a Value

Assigning `None` can indicate that a variable no longer contains usable data.

```python
data = "Important information"

print(data)

data = None

print(data)
```

**Output:**

```text
Important information
None
```

Assigning `None` does not delete the variable. The variable still exists, but its current value is `None`.

To completely remove a variable name, use `del`.

```python
data = "Important information"

del data
```

Trying to access it afterward raises an error:

```python
print(data)
```

**Error:**

```text
NameError: name 'data' is not defined
```

[Back to Index](#index)