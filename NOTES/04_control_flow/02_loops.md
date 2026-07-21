<a id="loops-in-python"></a>

## Loops in Python

Loops repeatedly execute a block of code.

Python provides two main loop structures:

* `while` loops repeat while a condition remains true.
* `for` loops iterate over the elements of an iterable.

Loops are commonly used for:

* Counting
* Processing collections
* Validating input
* Searching for values
* Calculating totals
* Generating patterns
* Repeating tasks

<a id="index"></a>

## Index

### While Loops

1. [Basic `while` Loop](#basic-while-loop)
2. [Forward Counter Loop](#forward-counter-loop)
3. [Backward Counter Loop](#backward-counter-loop)
4. [`while` Loop with Multiple Conditions](#while-multiple-conditions)
5. [Infinite Loops](#infinite-loops)
6. [`break` in a `while` Loop](#while-break)
7. [`continue` in a `while` Loop](#while-continue)
8. [`while-else` Statement](#while-else)
9. [Input-Validation Loops](#input-validation-loops)
10. [Accumulator Pattern](#accumulator-pattern)
11. [Flag-Controlled Loop](#flag-controlled-loop)
12. [Nested `while` Loops](#nested-while-loops)
13. [Pattern Printing with `while`](#while-pattern-printing)
14. [Number-Series Generation](#while-number-series)
15. [String Processing with `while`](#while-string-processing)

### For Loops

16. [`for` Loop with `range()`](#for-loop-with-range)
17. [`range()` with Start and Stop](#range-start-stop)
18. [`range()` with a Step](#range-with-step)
19. [`range()` with a Negative Step](#negative-step-range)
20. [Nested `for` Loops](#nested-for-loops)
21. [`break` in a `for` Loop](#for-break)
22. [`continue` in a `for` Loop](#for-continue)
23. [`for-else` Statement](#for-else)
24. [Loop-Variable Scope](#loop-variable-scope)
25. [Iterating Over Strings](#iterating-over-strings)
26. [Pattern Printing with `for`](#for-pattern-printing)

### Loop-Based Programs

27. [Multiplication Tables](#multiplication-tables)
28. [Series Summation](#series-summation)
29. [Factorial Calculation](#factorial-calculation)
30. [Factor Finding](#factor-finding)
31. [Prime-Number Checking](#prime-number-checking)
32. [Character Counting](#character-counting)
33. [Loop Summary](#loop-summary)

---

<a id="basic-while-loop"></a>

## Basic `while` Loop

A `while` loop repeatedly executes a block of code while its condition remains true.

It is useful when the number of iterations is not known in advance.

### Syntax

```python
while condition:
    # Code executed while the condition is true
```

Python checks the condition before every iteration.

* If the condition is true, the loop body runs.
* If the condition is false, the loop ends.
* If the condition is initially false, the loop body never runs.

### Example

```python
i = 1

while i < 6:
    print(i)
    i += 1
```

**Output:**

```text
1
2
3
4
5
```

The loop proceeds as follows:

```text
i = 1 → 1 < 6 → True  → print 1
i = 2 → 2 < 6 → True  → print 2
i = 3 → 3 < 6 → True  → print 3
i = 4 → 4 < 6 → True  → print 4
i = 5 → 5 < 6 → True  → print 5
i = 6 → 6 < 6 → False → stop
```

The statement `i += 1` is essential because it eventually makes the condition false.

[Back to Index](#index)

---

<a id="forward-counter-loop"></a>

## Forward Counter Loop

A forward counter loop increases a counter during each iteration.

### General Structure

```python
counter = start_value

while counter <= end_value:
    # Code executed during each iteration
    counter += step
```

### Counting from 1 to 5

```python
counter = 1

while counter <= 5:
    print(counter)
    counter += 1
```

**Output:**

```text
1
2
3
4
5
```

### Counting with a Larger Step

```python
counter = 0

while counter <= 10:
    print(counter)
    counter += 2
```

**Output:**

```text
0
2
4
6
8
10
```

The counter increases by `2` during each iteration.

[Back to Index](#index)

---

<a id="backward-counter-loop"></a>

## Backward Counter Loop

A backward counter loop decreases a counter during each iteration.

It can be used for:

* Countdowns
* Reverse processing
* Traversing indexes backward
* Decreasing values until a limit is reached

### General Structure

```python
counter = start_value

while counter >= end_value:
    # Code executed during each iteration
    counter -= step
```

### Counting from 5 to 1

```python
counter = 5

while counter >= 1:
    print(counter)
    counter -= 1
```

**Output:**

```text
5
4
3
2
1
```

### Countdown Example

```python
seconds = 3

while seconds > 0:
    print(seconds)
    seconds -= 1

print("Go!")
```

**Output:**

```text
3
2
1
Go!
```

[Back to Index](#index)

---

<a id="while-multiple-conditions"></a>

## `while` Loop with Multiple Conditions

Logical operators can combine multiple conditions in a `while` loop.

When using `and`, every condition must remain true for the loop to continue.

```python
a = 2
b = 3

while a < 10 and b < 15:
    print(f"a: {a}, b: {b}")
    a += 2
    b += 3

print("Loop finished!")
```

**Output:**

```text
a: 2, b: 3
a: 4, b: 6
a: 6, b: 9
a: 8, b: 12
Loop finished!
```

The loop stops when the condition becomes:

```text
a < 10 and b < 15
10 < 10 and 15 < 15
False and False
False
```

### Using `or`

A loop using `or` continues while at least one condition remains true.

```python
a = 1
b = 5

while a < 3 or b < 7:
    print(a, b)
    a += 1
    b += 1
```

**Output:**

```text
1 5
2 6
```

When `a` becomes `3` and `b` becomes `7`, both conditions are false.

[Back to Index](#index)

---

<a id="infinite-loops"></a>

## Infinite Loops

An infinite loop continues indefinitely because its condition never becomes false.

This often happens when:

* A counter is not updated.
* A counter is updated in the wrong direction.
* The condition is always true.
* A `continue` statement skips the required update.

### Accidental Infinite Loop

```python
i = 1

while i > 0:
    print("Infinite loop!")
```

The value of `i` never changes, so `i > 0` always remains true.

> Do not run this example without adding an exit condition. It will continue until the program is manually stopped.

### Intentional Infinite Loop

An intentional infinite loop can be written using `while True`.

```python
while True:
    command = input("Enter 'quit' to stop: ").strip().lower()

    if command == "quit":
        break

    print(f"You entered: {command}")
```

The condition is always true, but the `break` statement provides a controlled exit.

### Preventing Infinite Loops

Verify that:

1. The condition can eventually become false.
2. Variables used in the condition are updated.
3. Updates move values toward the stopping condition.
4. Every possible path can eventually terminate.

[Back to Index](#index)

---

<a id="while-break"></a>

## `break` in a `while` Loop

The `break` statement immediately terminates the nearest enclosing loop.

Execution continues with the first statement after the loop.

### Structure

```python
while condition:
    if exit_condition:
        break

    # Remaining loop code
```

### Stop When the Counter Reaches 4

```python
i = 1

while i <= 10:
    print(i)

    if i == 4:
        break

    i += 1
```

**Output:**

```text
1
2
3
4
```

When `i` becomes `4`, `break` terminates the loop before `i += 1` runs.

### Searching Until a Match Is Found

```python
number = 1

while number <= 10:
    if number == 6:
        print("Found the number.")
        break

    number += 1
```

**Output:**

```text
Found the number.
```

[Back to Index](#index)

---

<a id="while-continue"></a>

## `continue` in a `while` Loop

The `continue` statement skips the remaining code in the current iteration and begins the next iteration.

### Skip the Number 3

```python
i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)
```

**Output:**

```text
1
2
4
5
```

The counter is incremented before `continue`. This prevents the loop from becoming stuck at `3`.

### Common Mistake

The following code creates an infinite loop:

```python
i = 1

while i <= 5:
    if i == 3:
        continue

    print(i)
    i += 1
```

When `i` becomes `3`, Python repeatedly executes `continue` before reaching `i += 1`.

A safer structure is:

```python
i = 1

while i <= 5:
    current_value = i
    i += 1

    if current_value == 3:
        continue

    print(current_value)
```

[Back to Index](#index)

---

<a id="while-else"></a>

## `while-else` Statement

A `while` loop can include an `else` block.

The `else` block runs when the loop ends normally because its condition becomes false.

It does not run when the loop is terminated by `break`.

### Normal Completion

```python
i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed successfully.")
```

**Output:**

```text
1
2
3
Loop completed successfully.
```

### Loop Terminated with `break`

```python
i = 1

while i <= 3:
    print(i)

    if i == 2:
        break

    i += 1
else:
    print("Loop completed successfully.")
```

**Output:**

```text
1
2
```

The `else` block is skipped because the loop ended with `break`.

### Search Example

```python
target = 7
number = 1

while number <= 5:
    if number == target:
        print("Target found.")
        break

    number += 1
else:
    print("Target not found.")
```

**Output:**

```text
Target not found.
```

[Back to Index](#index)

---

<a id="input-validation-loops"></a>

## Input-Validation Loops

An input-validation loop repeatedly requests input until the user provides an acceptable value.

### Validating a Number from 1 to 50

```python
valid_minimum = 1
valid_maximum = 50

user_input = input("Enter a number between 1 and 50: ").strip()

while (
    not user_input.isdigit()
    or not valid_minimum <= int(user_input) <= valid_maximum
):
    print("Invalid input. Enter a whole number between 1 and 50.")
    user_input = input("Enter a number between 1 and 50: ").strip()

number = int(user_input)

print(f"You entered a valid number: {number}")
```

**Example interaction:**

```text
Enter a number between 1 and 50: hello
Invalid input. Enter a whole number between 1 and 50.
Enter a number between 1 and 50: 75
Invalid input. Enter a whole number between 1 and 50.
Enter a number between 1 and 50: 25
You entered a valid number: 25
```

The `or` operator is necessary because the input is invalid when either:

* It is not composed entirely of digits.
* It is outside the required range.

### Validation with `try` and `except`

Using exception handling supports a wider range of numeric input formats.

```python
while True:
    user_input = input(
        "Enter a whole number between 1 and 50: "
    ).strip()

    try:
        number = int(user_input)
    except ValueError:
        print("Enter a valid whole number.")
        continue

    if 1 <= number <= 50:
        break

    print("The number must be between 1 and 50.")

print(f"You entered a valid number: {number}")
```

[Back to Index](#index)

---

<a id="accumulator-pattern"></a>

## Accumulator Pattern

An accumulator stores a result that is updated during each loop iteration.

Accumulators can be used for:

* Totals
* Products
* Character counts
* Building strings
* Aggregating data

### Summing Numbers from 1 to 10

```python
n = 10
total = 0
counter = 1

while counter <= n:
    total += counter
    counter += 1

print(f"The sum of numbers from 1 to {n} is {total}.")
```

**Output:**

```text
The sum of numbers from 1 to 10 is 55.
```

The accumulator changes as follows:

```text
0 + 1  = 1
1 + 2  = 3
3 + 3  = 6
6 + 4  = 10
...
45 + 10 = 55
```

### Multiplication Accumulator

```python
number = 1
product = 1

while number <= 5:
    product *= number
    number += 1

print(product)
```

**Output:**

```text
120
```

[Back to Index](#index)

---

<a id="flag-controlled-loop"></a>

## Flag-Controlled Loop

A flag-controlled loop uses a Boolean variable to determine whether the loop should continue.

The flag usually has names such as:

* `running`
* `found`
* `is_valid`
* `keep_going`

### Example

```python
running = True
a = 4
target = 10

while running:
    print(a)

    if a == target:
        running = False
    else:
        a += 1

print("Target reached.")
```

**Output:**

```text
4
5
6
7
8
9
10
Target reached.
```

The loop terminates when `running` is changed from `True` to `False`.

### Flag Versus `break`

The same logic can often be written with `break`:

```python
a = 4
target = 10

while True:
    print(a)

    if a == target:
        break

    a += 1
```

Use a flag when the running state must be checked or modified in several places.

[Back to Index](#index)

---

<a id="nested-while-loops"></a>

## Nested `while` Loops

A nested loop is a loop placed inside another loop.

For every iteration of the outer loop, the inner loop runs through all of its iterations.

### Printing a 3 × 3 Grid

```python
outer = 1

while outer <= 3:
    inner = 1

    while inner <= 3:
        print(f"({outer},{inner})", end=" ")
        inner += 1

    print()
    outer += 1
```

**Output:**

```text
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
```

The outer loop controls the rows, while the inner loop controls the columns.

> The inner counter must normally be reset at the beginning of every outer-loop iteration.

[Back to Index](#index)

---

<a id="while-pattern-printing"></a>

## Pattern Printing with `while`

Nested `while` loops can generate grids, triangles, and other structured output.

### Printing a 3 × 5 Star Grid

```python
row = 1
total_rows = 3
total_columns = 5

while row <= total_rows:
    column = 1

    while column <= total_columns:
        print("*", end=" ")
        column += 1

    print()
    row += 1
```

**Output:**

```text
* * * * *
* * * * *
* * * * *
```

### Printing a Triangle

```python
row = 1
total_rows = 5

while row <= total_rows:
    column = 1

    while column <= row:
        print("*", end=" ")
        column += 1

    print()
    row += 1
```

**Output:**

```text
*
* *
* * *
* * * *
* * * * *
```

[Back to Index](#index)

---

<a id="while-number-series"></a>

## Number-Series Generation

A `while` loop can generate a numerical sequence by updating a value after each iteration.

### Even Numbers from 2 to 10

```python
number = 2

while number <= 10:
    print(number)
    number += 2
```

**Output:**

```text
2
4
6
8
10
```

### Multiples of 10

```python
number = 1

while number <= 5:
    print(number * 10)
    number += 1
```

**Output:**

```text
10
20
30
40
50
```

### Arithmetic Sequence

```python
current_value = 5
difference = 3
terms_printed = 0

while terms_printed < 5:
    print(current_value)
    current_value += difference
    terms_printed += 1
```

**Output:**

```text
5
8
11
14
17
```

[Back to Index](#index)

---

<a id="while-string-processing"></a>

## String Processing with `while`

A string can be processed character by character using an index.

### Converting Characters to Uppercase

```python
input_string = "hello world"
index = 0

while index < len(input_string):
    print(input_string[index].upper(), end="")
    index += 1

print()
```

**Output:**

```text
HELLO WORLD
```

### Counting Vowels

```python
text = "Hello World"
index = 0
vowel_count = 0

while index < len(text):
    if text[index].lower() in "aeiou":
        vowel_count += 1

    index += 1

print(f"Vowels: {vowel_count}")
```

**Output:**

```text
Vowels: 3
```

A `for` loop is generally more direct for character-by-character string iteration, but a `while` loop is useful when explicit index control is required.

[Back to Index](#index)

---

<a id="for-loop-with-range"></a>

## `for` Loop with `range()`

A `for` loop iterates over the elements of an iterable.

The `range()` function produces a sequence of integers and is commonly used to repeat code a specific number of times.

### Syntax

```python
for index in range(stop):
    # Code executed during each iteration
```

`range(stop)` generates integers from `0` up to, but not including, `stop`.

### Printing Numbers from 0 to 4

```python
for i in range(5):
    print(i)
```

**Output:**

```text
0
1
2
3
4
```

The sequence generated by `range(5)` is:

```text
0, 1, 2, 3, 4
```

The loop runs five times.

### Repeating an Action

```python
for _ in range(3):
    print("Hello")
```

**Output:**

```text
Hello
Hello
Hello
```

The name `_` is conventionally used when the loop variable is not needed.

[Back to Index](#index)

---

<a id="range-start-stop"></a>

## `range()` with Start and Stop

The two-argument form of `range()` specifies the beginning and end of the sequence.

### Syntax

```python
range(start, stop)
```

* `start` is included.
* `stop` is excluded.
* The default step is `1`.

### Example

```python
for i in range(2, 6):
    print(i)
```

**Output:**

```text
2
3
4
5
```

The value `6` is excluded.

### Empty Range

```python
for i in range(5, 2):
    print(i)
```

This loop produces no output because the default positive step cannot move from `5` toward `2`.

[Back to Index](#index)

---

<a id="range-with-step"></a>

## `range()` with a Step

The third argument to `range()` controls how much the current value changes after each iteration.

### Syntax

```python
range(start, stop, step)
```

### Even Numbers

```python
for i in range(0, 10, 2):
    print(i)
```

**Output:**

```text
0
2
4
6
8
```

The sequence begins at `0`, increases by `2`, and stops before `10`.

### Odd Numbers

```python
for i in range(1, 10, 2):
    print(i)
```

**Output:**

```text
1
3
5
7
9
```

### Step Cannot Be Zero

```python
for i in range(1, 10, 0):
    print(i)
```

**Error:**

```text
ValueError: range() arg 3 must not be zero
```

A zero step would prevent the sequence from progressing.

[Back to Index](#index)

---

<a id="negative-step-range"></a>

## `range()` with a Negative Step

A negative step generates numbers in descending order.

### Countdown from 10 to 1

```python
for i in range(10, 0, -1):
    print(i)
```

**Output:**

```text
10
9
8
7
6
5
4
3
2
1
```

The stop value `0` is excluded.

### Decreasing by Two

```python
for i in range(10, 0, -2):
    print(i)
```

**Output:**

```text
10
8
6
4
2
```

When the step is negative, the start value should normally be greater than the stop value.

[Back to Index](#index)

---

<a id="nested-for-loops"></a>

## Nested `for` Loops

A nested `for` loop places one loop inside another.

### Structure

```python
for outer_value in outer_iterable:
    for inner_value in inner_iterable:
        # Inner loop code
```

### Example

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

**Output:**

```text
i: 0, j: 0
i: 0, j: 1
i: 1, j: 0
i: 1, j: 1
i: 2, j: 0
i: 2, j: 1
```

The outer loop runs three times. During each outer iteration, the inner loop runs twice.

The total number of inner executions is:

```text
3 × 2 = 6
```

[Back to Index](#index)

---

<a id="for-break"></a>

## `break` in a `for` Loop

The `break` statement immediately terminates the nearest enclosing `for` loop.

### Stop When a Condition Is Met

```python
for i in range(5):
    if i > 2:
        print(i)
        break
```

**Output:**

```text
3
```

The values `0`, `1`, and `2` do not satisfy `i > 2`.

When `i` becomes `3`, the program prints it and terminates the loop.

### Search Example

```python
numbers = [4, 7, 12, 19]
target = 12

for number in numbers:
    if number == target:
        print("Target found.")
        break
```

**Output:**

```text
Target found.
```

[Back to Index](#index)

---

<a id="for-continue"></a>

## `continue` in a `for` Loop

The `continue` statement skips the remaining code in the current iteration and moves to the next item.

### Skip the Number 5

```python
for number in range(1, 11):
    if number == 5:
        continue

    print(number)
```

**Output:**

```text
1
2
3
4
6
7
8
9
10
```

### Print Only Even Numbers

```python
for number in range(1, 11):
    if number % 2 != 0:
        continue

    print(number)
```

**Output:**

```text
2
4
6
8
10
```

[Back to Index](#index)

---

<a id="for-else"></a>

## `for-else` Statement

A `for` loop can include an `else` block.

The `else` block runs when the loop completes normally.

It does not run when the loop is terminated by `break`.

### Loop Terminated with `break`

```python
for number in range(1, 6):
    if number == 4:
        print("Breaking at", number)
        break
else:
    print("Loop completed.")
```

**Output:**

```text
Breaking at 4
```

### Normal Completion

```python
for number in range(1, 4):
    print(number)
else:
    print("Loop completed.")
```

**Output:**

```text
1
2
3
Loop completed.
```

### Search Pattern

```python
numbers = [2, 4, 6, 8]
target = 5

for number in numbers:
    if number == target:
        print("Target found.")
        break
else:
    print("Target not found.")
```

**Output:**

```text
Target not found.
```

[Back to Index](#index)

---

<a id="loop-variable-scope"></a>

## Loop-Variable Scope

A `for` loop does not create a separate local scope in Python.

When a loop executes at least once, its variable remains available after the loop and contains the final assigned value.

```python
for i in range(5):
    print(i)

print(f"The final value of i is {i}.")
```

**Output:**

```text
0
1
2
3
4
The final value of i is 4.
```

### Empty Loop

When a loop executes zero times and the variable did not already exist, the variable is not created.

```python
for value in range(0):
    print(value)

print(value)
```

**Error:**

```text
NameError: name 'value' is not defined
```

Do not rely unnecessarily on a loop variable after the loop. Store the required result in a clearly named variable instead.

[Back to Index](#index)

---

<a id="iterating-over-strings"></a>

## Iterating Over Strings

A string is an iterable sequence of characters.

A `for` loop can access each character directly without using indexes.

```python
text = "hello"

for character in text:
    print(character)
```

**Output:**

```text
h
e
l
l
o
```

### Printing on One Line

```python
text = "hello"

for character in text:
    print(character.upper(), end="")

print()
```

**Output:**

```text
HELLO
```

### Iterating with Indexes

Use `enumerate()` when both the index and character are needed.

```python
text = "Python"

for index, character in enumerate(text):
    print(index, character)
```

**Output:**

```text
0 P
1 y
2 t
3 h
4 o
5 n
```

[Back to Index](#index)

---

<a id="for-pattern-printing"></a>

## Pattern Printing with `for`

Nested `for` loops can generate visual patterns.

### Right-Angled Triangle

```python
for row in range(5):
    for column in range(row + 1):
        print("*", end=" ")

    print()
```

**Output:**

```text
*
* *
* * *
* * * *
* * * * *
```

The outer loop controls the number of rows.

The inner loop executes:

```text
row 0 → 1 time
row 1 → 2 times
row 2 → 3 times
row 3 → 4 times
row 4 → 5 times
```

### Simplified String-Repetition Version

```python
for row in range(1, 6):
    print("* " * row)
```

**Output:**

```text
*
* *
* * *
* * * *
* * * * *
```

[Back to Index](#index)

---

<a id="multiplication-tables"></a>

## Multiplication Tables

Nested loops can generate several multiplication tables.

```python
for number in range(1, 3):
    for multiplier in range(1, 8):
        product = number * multiplier
        print(f"{number} × {multiplier} = {product}")

    print()
```

**Output:**

```text
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3
1 × 4 = 4
1 × 5 = 5
1 × 6 = 6
1 × 7 = 7

2 × 1 = 2
2 × 2 = 4
2 × 3 = 6
2 × 4 = 8
2 × 5 = 10
2 × 6 = 12
2 × 7 = 14
```

The outer loop selects the table, while the inner loop selects the multiplier.

[Back to Index](#index)

---

<a id="series-summation"></a>

## Series Summation

Series summation adds a sequence of values using an accumulator.

### Sum of the First Five Natural Numbers

```text
1 + 2 + 3 + 4 + 5 = 15
```

### Using a `for` Loop

```python
n = 5
total_sum = 0

for number in range(1, n + 1):
    total_sum += number

print(
    f"The sum of the first {n} natural numbers "
    f"is {total_sum}."
)
```

**Output:**

```text
The sum of the first 5 natural numbers is 15.
```

### Using `sum()`

Python also provides the built-in `sum()` function:

```python
n = 5
total_sum = sum(range(1, n + 1))

print(total_sum)
```

**Output:**

```text
15
```

The loop-based version is useful for learning the accumulator pattern.

[Back to Index](#index)

---

<a id="factorial-calculation"></a>

## Factorial Calculation

The factorial of a non-negative integer `n` is the product of all positive integers from `1` through `n`.

It is written as `n!`.

For example:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

By definition:

```text
0! = 1
```

### Using a `for` Loop

```python
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print(f"The factorial of {n} is {factorial}.")
```

**Example interaction:**

```text
Enter a non-negative integer: 5
The factorial of 5 is 120.
```

The accumulator must be initialized before the loop:

```python
factorial = 1
```

Starting with zero would make every result zero.

### Example with Zero

```text
Enter a non-negative integer: 0
The factorial of 0 is 1.
```

For `n = 0`, `range(1, 1)` is empty, so the initial accumulator value `1` remains unchanged.

[Back to Index](#index)

---

<a id="factor-finding"></a>

## Factor Finding

A factor divides a number exactly without leaving a remainder.

For example, the factors of `12` are:

```text
1, 2, 3, 4, 6, 12
```

### Program

```python
number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Enter an integer greater than zero.")
else:
    print(f"Factors of {number}:")

    for candidate in range(1, number + 1):
        if number % candidate == 0:
            print(candidate)
```

**Example interaction:**

```text
Enter a positive integer: 12
Factors of 12:
1
2
3
4
6
12
```

The condition:

```python
number % candidate == 0
```

checks whether the division produces a remainder of zero.

[Back to Index](#index)

---

<a id="prime-number-checking"></a>

## Prime-Number Checking

A prime number is an integer greater than `1` with exactly two positive factors:

* `1`
* The number itself

Examples of prime numbers include:

```text
2, 3, 5, 7, 11, 13
```

### Basic Program

```python
number = int(input("Enter an integer: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True

    for candidate in range(2, number):
        if number % candidate == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
```

### Example

```text
Enter an integer: 13
13 is a prime number.
```

### More Efficient Version

A divisor larger than the square root of the number does not need to be tested when no smaller divisor has been found.

```python
number = int(input("Enter an integer: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    maximum_candidate = int(number ** 0.5)

    for candidate in range(2, maximum_candidate + 1):
        if number % candidate == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
```

### Using `for-else`

```python
number = int(input("Enter an integer: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    for candidate in range(2, int(number ** 0.5) + 1):
        if number % candidate == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
```

The `else` block runs only when no divisor causes the loop to execute `break`.

[Back to Index](#index)

---

<a id="character-counting"></a>

## Character Counting

A loop can count how many times a character occurs in a string.

```python
text = "Hello, World!"
character_to_count = "o"
count = 0

for character in text:
    if character == character_to_count:
        count += 1

print(f"Count of '{character_to_count}': {count}")
```

**Output:**

```text
Count of 'o': 2
```

### Case-Insensitive Counting

```python
text = "Hello, World!"
character_to_count = "l"
count = 0

for character in text:
    if character.lower() == character_to_count.lower():
        count += 1

print(f"Count: {count}")
```

**Output:**

```text
Count: 3
```

Python strings also provide a built-in `count()` method:

```python
text = "Hello, World!"

print(text.count("o"))
```

**Output:**

```text
2
```

The loop-based implementation is useful when more complex counting conditions are required.

[Back to Index](#index)

---

<a id="loop-summary"></a>

## Loop Summary

| Feature                    | Purpose                                        |
| -------------------------- | ---------------------------------------------- |
| `while condition`          | Repeats while a condition remains true         |
| `for item in iterable`     | Processes each item in an iterable             |
| `range(stop)`              | Generates integers from `0` to `stop - 1`      |
| `range(start, stop)`       | Generates values from `start` to before `stop` |
| `range(start, stop, step)` | Generates values using a custom step           |
| `break`                    | Immediately terminates the nearest loop        |
| `continue`                 | Skips the rest of the current iteration        |
| Loop `else`                | Runs when a loop completes without `break`     |
| Accumulator                | Builds a result over several iterations        |
| Flag                       | Uses a Boolean variable to control a loop      |
| Nested loop                | Places one loop inside another                 |

### Choosing Between `while` and `for`

Use a `while` loop when:

* The number of iterations is not known in advance.
* Repetition depends on a changing condition.
* Input must be requested until it is valid.
* Explicit control over an index or state is required.

Use a `for` loop when:

* Iterating through a string or collection.
* Repeating code a known number of times.
* Processing every item in an iterable.
* Generating values with `range()`.

### Combined Example

```python
valid_numbers = []

while len(valid_numbers) < 3:
    user_input = input("Enter an integer: ").strip()

    try:
        number = int(user_input)
    except ValueError:
        print("Invalid integer.")
        continue

    valid_numbers.append(number)

print("\nEntered numbers:")

total = 0

for number in valid_numbers:
    print(number)
    total += number

print(f"Total: {total}")
```

**Example interaction:**

```text
Enter an integer: 5
Enter an integer: hello
Invalid integer.
Enter an integer: 10
Enter an integer: 15

Entered numbers:
5
10
15
Total: 30
```

[Back to Index](#index)