<a id="conditional-statements-in-python"></a>

## Conditional Statements in Python

Conditional statements allow a program to make decisions and execute different blocks of code depending on whether conditions are true or false.

Python provides several tools for decision-making:

* `if`
* `else`
* `elif`
* Logical operators such as `and`, `or`, and `not`
* Membership operators such as `in` and `not in`
* Identity operators such as `is` and `is not`
* Conditional expressions

<a id="index"></a>

## Index

1. [Simple `if` Statement](#simple-if-statement)
2. [`if-else` Statement](#if-else-statement)
3. [Comparison Operators in Conditions](#comparison-operators-in-conditions)

   * [Equal To (`==`)](#equal-to-condition)
   * [Not Equal To (`!=`)](#not-equal-to-condition)
4. [Multiple Conditions](#multiple-conditions)

   * [Using `and`](#conditions-with-and)
   * [Using `or`](#conditions-with-or)
5. [`if-elif` Structure](#if-elif-structure)
6. [`if-elif-else` Structure](#if-elif-else-structure)
7. [Nested `if` Statements](#nested-if-statements)
8. [Conditional Expressions](#conditional-expression)
9. [Truth-Value Testing](#truth-value-testing)

   * [Checking for `None`](#checking-for-none)
10. [Membership Testing](#membership-testing)
11. [Identity Testing](#identity-testing)
12. [Complex Boolean Expressions](#complex-boolean-expressions)
13. [Conditional Statement Summary](#conditional-statement-summary)

---

<a id="simple-if-statement"></a>

## Simple `if` Statement

An `if` statement executes a block of code only when its condition evaluates to `True`.

If the condition evaluates to `False`, Python skips the block.

### Syntax

```python
if condition:
    # Code executed when the condition is true
```

The structure contains:

* The `if` keyword
* A condition that produces a truthy or falsy value
* A colon (`:`)
* An indented block of code

### Example

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

**Output:**

```text
You are an adult.
```

The condition is:

```text
age >= 18
18 >= 18
True
```

Because the condition is `True`, the indented statement runs.

### False Condition

```python
age = 16

if age >= 18:
    print("You are an adult.")

print("Program finished.")
```

**Output:**

```text
Program finished.
```

The message inside the `if` block is skipped because `16 >= 18` is `False`.

### Indentation

Indentation identifies which statements belong to the `if` block.

```python
age = 20

if age >= 18:
    print("You are an adult.")
    print("You may continue.")

print("This statement is outside the if block.")
```

**Output:**

```text
You are an adult.
You may continue.
This statement is outside the if block.
```

Python commonly uses four spaces for each indentation level.

[Back to Index](#index)

---

<a id="if-else-statement"></a>

## `if-else` Statement

An `if-else` statement provides two possible execution paths:

* The `if` block runs when the condition is true.
* The `else` block runs when the condition is false.

Exactly one of the two blocks runs.

### Syntax

```python
if condition:
    # Code executed when the condition is true
else:
    # Code executed when the condition is false
```

### Example

```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

**Output:**

```text
You are an adult.
```

Changing the value produces a different result:

```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

**Output:**

```text
You are a minor.
```

The `else` block does not have its own condition. It runs whenever the preceding `if` condition is false.

[Back to Index](#index)

---

<a id="comparison-operators-in-conditions"></a>

## Comparison Operators in Conditions

Comparison operators compare values and return either `True` or `False`.

Common comparison operators include:

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

<a id="equal-to-condition"></a>

### 1. Equal To (`==`)

The equality operator checks whether two values are equal.

```python
result = 5 == 5

print(result)
```

**Output:**

```text
True
```

It can be used directly inside an `if` statement:

```python
password = "python123"

if password == "python123":
    print("Access granted.")
else:
    print("Incorrect password.")
```

**Output:**

```text
Access granted.
```

> Use `==` to compare values. Use `=` to assign values.

```python
number = 5       # Assignment
result = number == 5  # Comparison
```

#### Comparing Strings

String comparisons are case-sensitive.

```python
print("hello" == "hello")
print("hello" == "Hello")
```

**Output:**

```text
True
False
```

#### Comparing Integers and Floats

Integers and floats with the same numerical value compare as equal.

```python
print(3 == 3.0)
```

**Output:**

```text
True
```

[Back to Index](#index)

---

<a id="not-equal-to-condition"></a>

### 2. Not Equal To (`!=`)

The not-equal operator checks whether two values are different.

```python
print(5 != 3)
print(10 != 10)
```

**Output:**

```text
True
False
```

It can be used in a condition:

```python
status = "inactive"

if status != "active":
    print("The account is not active.")
```

**Output:**

```text
The account is not active.
```

The expression returns `True` because `"inactive"` and `"active"` are different strings.

[Back to Index](#index)

---

<a id="multiple-conditions"></a>

## Multiple Conditions

Logical operators combine several conditions into one expression.

The most common operators are:

* `and`
* `or`
* `not`

<a id="conditions-with-and"></a>

### 1. Using `and`

The `and` operator returns a truthy result only when all combined conditions are truthy.

```python
print(5 > 3 and 8 > 6)
print(5 > 10 and 8 > 6)
```

**Output:**

```text
True
False
```

The first expression checks:

```text
5 > 3 → True
8 > 6 → True

True and True → True
```

The second expression checks:

```text
5 > 10 → False
8 > 6  → True

False and True → False
```

### Using `and` in an `if` Statement

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")
```

**Output:**

```text
You are eligible to drive.
```

Both conditions must be true:

```text
age >= 18  → True
has_license → True
```

Therefore, the entire condition is true.

[Back to Index](#index)

---

<a id="conditions-with-or"></a>

### 2. Using `or`

The `or` operator returns a truthy result when at least one condition is truthy.

It returns `False` only when all conditions are false.

```python
a = 15
b = 5
c = 25

result = a > 10 or b < 10 or c > 20

print(result)
```

**Output:**

```text
True
```

All three conditions happen to be true, but only one true condition is required.

### Example with One True Condition

```python
x = 10
y = 20

result = x < 20 or y <= 10

print(result)
```

**Output:**

```text
True
```

The conditions are:

```text
x < 20  → True
y <= 10 → False

True or False → True
```

### Using `or` in an `if` Statement

```python
number = 5

if number < 10 or number > 50:
    print("The number is outside the range from 10 to 50.")
else:
    print("The number is between 10 and 50.")
```

**Output:**

```text
The number is outside the range from 10 to 50.
```

Because `5 < 10` is true, the complete condition is true.

> In this example, the `else` block includes the boundary values `10` and `50`.

[Back to Index](#index)

---

<a id="if-elif-structure"></a>

## `if-elif` Structure

The `if-elif` structure checks several conditions in order.

Python executes the first block whose condition evaluates to true. All remaining `elif` blocks are skipped.

### Syntax

```python
if condition1:
    # Runs when condition1 is true
elif condition2:
    # Runs when condition1 is false and condition2 is true
elif condition3:
    # Runs when all previous conditions are false
```

You may include as many `elif` blocks as needed.

### Example

```python
temperature = 35

if temperature > 40:
    print("Extremely hot")
elif temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
```

**Output:**

```text
Hot
```

Python evaluates the conditions in order:

```text
temperature > 40 → False
temperature > 30 → True
```

After finding the first true condition, Python runs that block and skips the remaining checks.

### No Matching Condition

An `if-elif` structure does not require an `else` block.

```python
temperature = 10

if temperature > 40:
    print("Extremely hot")
elif temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
```

This program produces no output because none of the conditions are true.

[Back to Index](#index)

---

<a id="if-elif-else-structure"></a>

## `if-elif-else` Structure

An `if-elif-else` structure handles several conditions and provides a final fallback block.

### Syntax

```python
if condition1:
    # Runs when condition1 is true
elif condition2:
    # Runs when condition2 is true
elif condition3:
    # Runs when condition3 is true
else:
    # Runs when none of the conditions are true
```

Only one block runs.

### Example: Grade Classification

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
```

**Output:**

```text
Grade: B
```

Python checks the conditions from top to bottom:

```text
score >= 90 → False
score >= 80 → True
```

The `"B"` block runs, and the remaining conditions are skipped.

### Condition Order Matters

More specific or restrictive conditions should usually appear first.

Incorrect order:

```python
score = 95

if score >= 60:
    print("Passed")
elif score >= 90:
    print("Excellent")
```

**Output:**

```text
Passed
```

The second condition is never reached because `95 >= 60` is already true.

A better structure is:

```python
score = 95

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Passed")
else:
    print("Failed")
```

**Output:**

```text
Excellent
```

[Back to Index](#index)

---

<a id="nested-if-statements"></a>

## Nested `if` Statements

A nested `if` statement is an `if` statement placed inside another conditional block.

The inner condition is checked only when the outer condition is true.

### Structure

```python
if condition1:
    if condition2:
        # Runs when both conditions are true
```

### Example

```python
age = 20
has_ticket = True

if age >= 18:
    print("Age requirement passed.")

    if has_ticket:
        print("Entry allowed.")
```

**Output:**

```text
Age requirement passed.
Entry allowed.
```

The inner condition is checked only because `age >= 18` is true.

### Nested `if-else`

```python
age = 20
has_ticket = False

if age >= 18:
    if has_ticket:
        print("Entry allowed.")
    else:
        print("A ticket is required.")
else:
    print("You must be at least 18.")
```

**Output:**

```text
A ticket is required.
```

### Alternative Using `and`

Simple nested conditions can often be combined:

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed.")
```

**Output:**

```text
Entry allowed.
```

Nested statements are useful when each level requires a separate action or explanation. Combined conditions are often clearer when only the final result matters.

[Back to Index](#index)

---

<a id="conditional-expression"></a>

## Conditional Expression

A conditional expression selects between two values using a single line.

It is sometimes called a **ternary expression**.

### Syntax

```python
value_if_true if condition else value_if_false
```

The condition is evaluated first:

* When true, `value_if_true` is returned.
* When false, `value_if_false` is returned.

### Example

```python
number = 4

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

**Output:**

```text
Even
```

The condition is:

```text
number % 2 == 0
4 % 2 == 0
0 == 0
True
```

Therefore, the expression returns `"Even"`.

### Equivalent `if-else` Statement

```python
number = 4

if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print(result)
```

**Output:**

```text
Even
```

### Another Example

```python
age = 16

status = "Adult" if age >= 18 else "Minor"

print(status)
```

**Output:**

```text
Minor
```

> Conditional expressions are best used for simple value selection. A regular `if-else` statement is usually clearer for complex logic or multiple actions.

[Back to Index](#index)

---

<a id="truth-value-testing"></a>

## Truth-Value Testing

Python can evaluate values directly in conditions.

Values considered false in a Boolean context include:

* `False`
* `None`
* `0`
* `0.0`
* `""`
* `[]`
* `()`
* `{}`
* `set()`

Most other values are considered true.

### Empty String

```python
user_name = ""

if user_name:
    print(f"Hello, {user_name}")
else:
    print("No username was provided.")
```

**Output:**

```text
No username was provided.
```

### Non-Empty String

```python
user_name = "Alice"

if user_name:
    print(f"Hello, {user_name}")
```

**Output:**

```text
Hello, Alice
```

### Using `not`

```python
items = []

if not items:
    print("The collection is empty.")
```

**Output:**

```text
The collection is empty.
```

The condition `not items` is true because an empty list is falsy.

[Back to Index](#index)

---

<a id="checking-for-none"></a>

### Checking for `None`

`None` represents the absence of a value.

Use `is None` when checking specifically for `None`.

```python
value = None

if value is None:
    print("No value is available.")
else:
    print("A value is available.")
```

**Output:**

```text
No value is available.
```

Use `is not None` to check that a value exists:

```python
value = 0

if value is not None:
    print("A value was provided.")
```

**Output:**

```text
A value was provided.
```

Although `0` is falsy, it is not `None`.

### `not value` Is Not a Specific `None` Check

```python
value = 0

if not value:
    print("The value is falsy.")
```

**Output:**

```text
The value is falsy.
```

The condition `not value` is true for many values, including:

* `None`
* `0`
* `False`
* `""`
* Empty collections

Therefore:

```python
if value is None:
```

means:

> Check specifically whether the value is `None`.

Whereas:

```python
if not value:
```

means:

> Check whether the value is falsy.

[Back to Index](#index)

---

<a id="membership-testing"></a>

## Membership Testing

Membership operators check whether a value exists inside a collection.

Python provides:

* `in`
* `not in`

### Syntax

```python
element in collection
element not in collection
```

### Checking a Substring

```python
message = "Welcome to Python programming!"

print("Python" in message)
print("Java" not in message)
```

**Output:**

```text
True
True
```

The tests are case-sensitive:

```python
text = "Hello"

print("H" in text)
print("h" in text)
```

**Output:**

```text
True
False
```

### Using Membership in an `if` Statement

```python
message = "Welcome to Python programming!"

if "Python" in message:
    print("The message mentions Python.")
```

**Output:**

```text
The message mentions Python.
```

### Checking a List

```python
allowed_roles = ["admin", "editor", "viewer"]
user_role = "editor"

if user_role in allowed_roles:
    print("The role is valid.")
else:
    print("Unknown role.")
```

**Output:**

```text
The role is valid.
```

### Using `not in`

```python
blocked_users = ["user1", "user2"]
current_user = "user3"

if current_user not in blocked_users:
    print("Access permitted.")
```

**Output:**

```text
Access permitted.
```

[Back to Index](#index)

---

<a id="identity-testing"></a>

## Identity Testing

Identity operators check whether two variables refer to the same object in memory.

Python provides:

* `is`
* `is not`

Identity comparison is different from value comparison.

* `==` compares values.
* `is` compares object identity.

### Comparing Lists

```python
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(list_a == list_b)
print(list_a is list_b)
print(list_a is list_c)
```

**Output:**

```text
True
False
True
```

Explanation:

* `list_a == list_b` is `True` because their contents are equal.
* `list_a is list_b` is `False` because they are separate list objects.
* `list_a is list_c` is `True` because both variables refer to the same list.

### Checking `None`

The most common identity check is:

```python
value = None

if value is None:
    print("No value")
```

**Output:**

```text
No value
```

### Do Not Use `is` for Ordinary Value Comparisons

Avoid this:

```python
x = 100
y = 100

print(x is y)
```

The result may appear to be `True` in some environments because Python may reuse certain immutable objects. This behavior should not be relied upon for value comparison.

Use:

```python
print(x == y)
```

Use `is` primarily when identity itself matters, especially when checking against `None`.

[Back to Index](#index)

---

<a id="complex-boolean-expressions"></a>

## Complex Boolean Expressions

Complex Boolean expressions combine comparisons and logical operators.

Parentheses can be used to group related conditions and make the intended logic clear.

### Example

A user may proceed when either:

* They are at least 18 years old, or
* They have permission and parental approval

```python
age = 17
has_permission = True
parent_approval = True

if age >= 18 or (has_permission and parent_approval):
    print("Allowed to proceed.")
else:
    print("Access denied.")
```

**Output:**

```text
Allowed to proceed.
```

Python evaluates the grouped expression first:

```text
has_permission and parent_approval
True and True
True
```

It then evaluates:

```text
age >= 18 or True
False or True
True
```

Therefore, the `if` block runs.

### Using `not`

```python
age = 25
has_ticket = True
is_banned = False

if age >= 18 and has_ticket and not is_banned:
    print("Entry allowed.")
else:
    print("Entry denied.")
```

**Output:**

```text
Entry allowed.
```

The conditions are:

```text
age >= 18    → True
has_ticket   → True
not is_banned → not False → True
```

Therefore:

```text
True and True and True → True
```

### Operator Precedence

Logical operators are evaluated in this order:

1. Parentheses: `()`
2. Comparisons: `==`, `!=`, `>`, `<`, `>=`, `<=`, `in`, `is`
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

Python evaluates `and` first:

```text
True or (False and False)
True or False
True
```

Parentheses can change the result:

```python
result = (True or False) and False

print(result)
```

**Output:**

```text
False
```

> Use parentheses in complex expressions to make the intended logic clear, even when Python's precedence rules already produce the correct result.

[Back to Index](#index)

---

<a id="conditional-statement-summary"></a>

## Conditional Statement Summary

| Structure or operator  | Purpose                                                     |
| ---------------------- | ----------------------------------------------------------- |
| `if`                   | Runs code when a condition is true                          |
| `else`                 | Runs code when the preceding condition is false             |
| `elif`                 | Checks another condition when previous conditions are false |
| `and`                  | Requires all combined conditions to be truthy               |
| `or`                   | Requires at least one combined condition to be truthy       |
| `not`                  | Reverses a value's truthiness                               |
| `in`                   | Checks whether a value exists in a collection               |
| `not in`               | Checks whether a value is absent                            |
| `is`                   | Checks whether two references identify the same object      |
| `is not`               | Checks whether two references identify different objects    |
| Conditional expression | Selects between two values in one expression                |

### Combined Example

```python
user_name = "Alice"
age = 22
role = "editor"
allowed_roles = ["admin", "editor"]
is_banned = False

if not user_name:
    print("A username is required.")
elif age < 18:
    print("The user must be at least 18.")
elif role not in allowed_roles:
    print("The user's role is not permitted.")
elif is_banned:
    print("The user is blocked.")
else:
    access_message = "Access granted" if role == "admin" else "Limited access granted"
    print(access_message)
```

**Output:**

```text
Limited access granted
```

[Back to Index](#index)