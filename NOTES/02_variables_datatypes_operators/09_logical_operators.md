<a id="logical-operators-in-python"></a>

## Logical Operators in Python

Logical operators combine, modify, or evaluate conditions.

Python provides three main logical operators:

* `and`
* `or`
* `not`

These operators are commonly used with Boolean expressions in conditional statements, validation rules, filtering, and decision-making.

<a id="index"></a>

## Index

1. [The `and` Operator](#and-operator)

   * [`and` Truth Table](#and-truth-table)
   * [Example with Conditions](#and-example)
   * [`and` Short-Circuit Evaluation](#and-short-circuit)
2. [The `or` Operator](#or-operator)

   * [`or` Truth Table](#or-truth-table)
   * [Example with Conditions](#or-example)
   * [`or` Short-Circuit Evaluation](#or-short-circuit)
3. [The `not` Operator](#not-operator)

   * [`not` Truth Table](#not-truth-table)
   * [Basic Usage](#not-basic-usage)
   * [Using `not` with a Condition](#not-with-condition)
4. [Combining Logical Operators](#combining-logical-operators)
5. [Logical Operator Precedence](#logical-operator-precedence)
6. [Logical Operators with Non-Boolean Values](#logical-operators-non-boolean-values)
7. [Logical Operator Summary](#logical-operator-summary)

---

<a id="and-operator"></a>

## The `and` Operator

The `and` operator combines two conditions.

It evaluates to `True` only when both conditions are true. If either condition is false, the combined condition evaluates to `False`.

### Syntax

```python
condition1 and condition2
```

Python evaluates `condition1` first.

* If `condition1` is false, Python skips `condition2`.
* If `condition1` is true, Python evaluates `condition2`.

This behavior is called **short-circuit evaluation**.

<a id="and-truth-table"></a>

### `and` Truth Table

| First condition | Second condition | Result  |
| --------------- | ---------------- | ------- |
| `True`          | `True`           | `True`  |
| `True`          | `False`          | `False` |
| `False`         | `True`           | `False` |
| `False`         | `False`          | `False` |

<a id="and-example"></a>

### Example with Conditions

```python
number = 12

is_even = number % 2 == 0
is_large = number > 10

result = is_even and is_large

print(is_even)
print(is_large)
print(result)
```

**Output:**

```text
True
True
True
```

The conditions are evaluated as follows:

```text
number % 2 == 0 → 12 % 2 == 0 → True
number > 10     → 12 > 10     → True
```

Because both conditions are `True`, the complete expression returns `True`.

```text
True and True → True
```

Another example:

```python
number = 7

is_even = number % 2 == 0
is_positive = number > 0

print(is_even and is_positive)
```

**Output:**

```text
False
```

The conditions are:

```text
is_even     → False
is_positive → True
```

Therefore:

```text
False and True → False
```

[Back to Index](#index)

---

<a id="and-short-circuit"></a>

### `and` Short-Circuit Evaluation

When the first operand of `and` is false, Python does not evaluate the second operand.

```python
number = 0

result = number != 0 and 10 / number > 2

print(result)
```

**Output:**

```text
False
```

The first condition is:

```text
number != 0 → False
```

Because the first condition is false, Python skips:

```python
10 / number > 2
```

This prevents a division-by-zero error.

The expression works like this:

```text
False and <skipped expression> → False
```

> For `and`, Python evaluates the second operand only when the first operand is truthy.

[Back to Index](#index)

---

<a id="or-operator"></a>

## The `or` Operator

The `or` operator combines two conditions and evaluates to `True` when at least one condition is true.

It evaluates to `False` only when both conditions are false.

### Syntax

```python
condition1 or condition2
```

Python evaluates `condition1` first.

* If `condition1` is true, Python skips `condition2`.
* If `condition1` is false, Python evaluates `condition2`.

<a id="or-truth-table"></a>

### `or` Truth Table

| First condition | Second condition | Result  |
| --------------- | ---------------- | ------- |
| `True`          | `True`           | `True`  |
| `True`          | `False`          | `True`  |
| `False`         | `True`           | `True`  |
| `False`         | `False`          | `False` |

<a id="or-example"></a>

### Example with Conditions

```python
number = 15

result = number < 10 or number > 20

print(result)
```

**Output:**

```text
False
```

The conditions are evaluated as follows:

```text
number < 10 → 15 < 10 → False
number > 20 → 15 > 20 → False
```

Because both conditions are `False`, the complete expression returns `False`.

```text
False or False → False
```

Another example:

```python
number = 25

result = number < 10 or number > 20

print(result)
```

**Output:**

```text
True
```

The conditions are:

```text
number < 10 → False
number > 20 → True
```

Therefore:

```text
False or True → True
```

[Back to Index](#index)

---

<a id="or-short-circuit"></a>

### `or` Short-Circuit Evaluation

When the first operand of `or` is true, Python does not evaluate the second operand.

```python
is_admin = True

result = is_admin or print("Checking additional permissions")

print(result)
```

**Output:**

```text
True
```

The `print()` call is skipped because `is_admin` is already `True`.

The expression works like this:

```text
True or <skipped expression> → True
```

A practical example is providing a fallback value:

```python
user_name = ""

display_name = user_name or "Guest"

print(display_name)
```

**Output:**

```text
Guest
```

The empty string is false in a Boolean context, so Python evaluates and returns `"Guest"`.

> For `or`, Python evaluates the second operand only when the first operand is falsy.

[Back to Index](#index)

---

<a id="not-operator"></a>

## The `not` Operator

The `not` operator reverses the Boolean meaning of a value or condition.

* `True` becomes `False`.
* `False` becomes `True`.

### Syntax

```python
not condition
```

<a id="not-truth-table"></a>

### `not` Truth Table

| Condition | Result of `not` |
| --------- | --------------- |
| `True`    | `False`         |
| `False`   | `True`          |

<a id="not-basic-usage"></a>

### Basic Usage

```python
flag = True

print(not flag)
```

**Output:**

```text
False
```

The expression is evaluated as follows:

```text
not True → False
```

Another example:

```python
flag = False

print(not flag)
```

**Output:**

```text
True
```

The expression is:

```text
not False → True
```

[Back to Index](#index)

---

<a id="not-with-condition"></a>

### Using `not` with a Condition

```python
x = 5
y = 10

condition = x < y

print(condition)
print(not condition)
```

**Output:**

```text
True
False
```

The comparison evaluates first:

```text
x < y → 5 < 10 → True
```

The `not` operator then reverses the result:

```text
not True → False
```

A practical example:

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in.")
```

**Output:**

```text
Please log in.
```

The condition `not is_logged_in` becomes `True`, so the `if` block runs.

[Back to Index](#index)

---

<a id="combining-logical-operators"></a>

## Combining Logical Operators

Multiple logical operators can be used in the same expression.

```python
age = 25
has_id = True
is_banned = False

can_enter = age >= 18 and has_id and not is_banned

print(can_enter)
```

**Output:**

```text
True
```

The expression checks:

```text
age >= 18     → True
has_id        → True
not is_banned → not False → True
```

Therefore:

```text
True and True and True → True
```

Another example:

```python
temperature = 35
is_raining = False

should_stay_inside = temperature > 40 or is_raining

print(should_stay_inside)
```

**Output:**

```text
False
```

Both conditions are false:

```text
temperature > 40 → False
is_raining       → False
```

Therefore:

```text
False or False → False
```

### Using Parentheses

Parentheses make complex logical expressions easier to understand.

```python
age = 17
has_parent_permission = True
has_ticket = True

can_enter = (age >= 18 or has_parent_permission) and has_ticket

print(can_enter)
```

**Output:**

```text
True
```

Python evaluates the expression inside the parentheses first:

```text
age >= 18 or has_parent_permission
False or True
True
```

It then evaluates:

```text
True and has_ticket
True and True
True
```

[Back to Index](#index)

---

<a id="logical-operator-precedence"></a>

## Logical Operator Precedence

When multiple logical operators appear in one expression, Python evaluates them in this order:

1. Parentheses: `()`
2. Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
3. `not`
4. `and`
5. `or`

For example:

```python
result = True or False and False

print(result)
```

**Output:**

```text
True
```

Python evaluates `and` before `or`:

```text
True or (False and False)
True or False
True
```

Using parentheses can change the result:

```python
result = (True or False) and False

print(result)
```

**Output:**

```text
False
```

The expression becomes:

```text
(True or False) and False
True and False
False
```

> Use parentheses to make the intended evaluation order clear, even when they are not strictly required.

[Back to Index](#index)

---

<a id="logical-operators-non-boolean-values"></a>

## Logical Operators with Non-Boolean Values

Python's `and` and `or` operators do not always return `True` or `False`.

They return one of their operands based on whether each operand is considered truthy or falsy.

Common falsy values include:

* `False`
* `None`
* `0`
* `0.0`
* `""`
* `[]`
* `{}`
* `set()`

Most other values are truthy.

### `and` with Non-Boolean Values

The `and` operator returns:

* The first falsy operand, if one exists
* Otherwise, the final operand

```python
print(0 and 10)
print(5 and 10)
```

**Output:**

```text
0
10
```

Explanation:

```text
0 and 10 → 0
```

Because `0` is falsy, Python returns it immediately.

```text
5 and 10 → 10
```

Because `5` is truthy, Python evaluates and returns the second operand.

### `or` with Non-Boolean Values

The `or` operator returns:

* The first truthy operand
* Otherwise, the final operand

```python
print("" or "Default")
print("Python" or "Default")
```

**Output:**

```text
Default
Python
```

Explanation:

```text
"" or "Default"       → "Default"
"Python" or "Default" → "Python"
```

### `not` Always Returns a Boolean

Unlike `and` and `or`, the `not` operator always returns `True` or `False`.

```python
print(not "")
print(not "Python")
print(not 0)
print(not 10)
```

**Output:**

```text
True
False
True
False
```

[Back to Index](#index)

---

<a id="logical-operator-summary"></a>

## Logical Operator Summary

| Operator | Purpose                                    | Boolean result                                 |
| -------- | ------------------------------------------ | ---------------------------------------------- |
| `and`    | Requires both conditions to be true        | `True` only when both conditions are true      |
| `or`     | Requires at least one condition to be true | `False` only when both conditions are false    |
| `not`    | Reverses the truth value                   | Converts truthy to `False` and falsy to `True` |

### Combined Example

```python
number = 12

is_positive = number > 0
is_even = number % 2 == 0
is_too_large = number > 100

print(is_positive and is_even)
print(is_positive or is_too_large)
print(not is_too_large)
```

**Output:**

```text
True
True
True
```

The expressions are evaluated as follows:

```text
True and True  → True
True or False  → True
not False      → True
```

[Back to Index](#index)