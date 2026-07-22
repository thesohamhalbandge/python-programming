<a id="tuple-methods-and-built-in-functions"></a>

## Tuple Methods and Built-In Functions in Python

Tuples provide two methods for searching and counting values:

* `count()`
* `index()`

Python also provides built-in functions that work with tuples, including:

* `len()`
* `min()`
* `max()`
* `sum()`

These operations inspect or calculate information from a tuple without modifying it.

<a id="index"></a>

## Index

1. [`count()` Method](#tuple-count-method)

   * [Counting a Missing Value](#counting-missing-value)
   * [Counting Different Data Types](#counting-different-types)
2. [`index()` Method](#tuple-index-method)

   * [Finding the First Occurrence](#finding-first-occurrence)
   * [Using the `start` Parameter](#tuple-index-start)
   * [Using `start` and `stop`](#tuple-index-range)
   * [Handling a Missing Value](#tuple-index-missing-value)
3. [`len()` Function](#tuple-len-function)
4. [`min()` Function](#tuple-min-function)

   * [`min()` with Strings](#tuple-min-strings)
   * [`min()` Errors](#tuple-min-errors)
5. [`max()` Function](#tuple-max-function)

   * [`max()` with Strings](#tuple-max-strings)
   * [`max()` Errors](#tuple-max-errors)
6. [`sum()` Function](#tuple-sum-function)

   * [Using the Optional Start Value](#tuple-sum-start)
   * [`sum()` Errors](#tuple-sum-errors)
7. [Combined Example](#tuple-functions-combined-example)
8. [Summary](#tuple-functions-summary)

---

<a id="tuple-count-method"></a>

## `count()` Method

The `count()` method returns the number of times a specified value occurs in a tuple.

It does not modify the tuple.

### Syntax

```python id="lz3p6x"
tuple_name.count(value)
```

The parameter is:

* `value`: the value whose occurrences should be counted

### Example

```python id="ej7olw"
colors = (
    "red",
    "blue",
    "green",
    "blue",
    "red",
    "blue",
)

blue_count = colors.count("blue")

print("Number of times 'blue' appears:", blue_count)
```

**Output:**

```text id="5dmbdn"
Number of times 'blue' appears: 3
```

The method checks every top-level element and counts exact equality matches.

```text id="z06zpl"
"red"   → no match
"blue"  → match 1
"green" → no match
"blue"  → match 2
"red"   → no match
"blue"  → match 3
```

The original tuple remains unchanged:

```python id="60vdlp"
print(colors)
```

**Output:**

```text id="gjbtuh"
('red', 'blue', 'green', 'blue', 'red', 'blue')
```

[Back to Index](#index)

---

<a id="counting-missing-value"></a>

### Counting a Missing Value

When the specified value does not exist, `count()` returns `0`.

It does not raise an error.

```python id="zjbj5g"
numbers = (10, 20, 30, 40)

result = numbers.count(100)

print(result)
```

**Output:**

```text id="7dsr8s"
0
```

This makes `count()` useful when a value may or may not be present.

```python id="1red41"
numbers = (10, 20, 20, 30)

if numbers.count(20) > 0:
    print("The tuple contains 20.")
```

**Output:**

```text id="86tokw"
The tuple contains 20.
```

For a simple membership check, the `in` operator is usually clearer:

```python id="oekfzw"
if 20 in numbers:
    print("The tuple contains 20.")
```

[Back to Index](#index)

---

<a id="counting-different-types"></a>

### Counting Different Data Types

The `count()` method works with any value that can be compared for equality.

### Counting Strings

String comparisons are case-sensitive.

```python id="v59e0u"
languages = ("Python", "python", "Python", "Java")

print(languages.count("Python"))
print(languages.count("python"))
```

**Output:**

```text id="fqgfoe"
2
1
```

### Counting Nested Tuples

```python id="eby211"
coordinates = (
    (1, 2),
    (3, 4),
    (1, 2),
)

print(coordinates.count((1, 2)))
```

**Output:**

```text id="nkjyhf"
2
```

Each nested tuple is treated as one top-level element.

### Booleans and Integers

In Python, `True` compares equal to `1`, and `False` compares equal to `0`.

```python id="7uv8ko"
values = (True, 1, False, 0, 2)

print(values.count(True))
print(values.count(False))
```

**Output:**

```text id="e0ojug"
2
2
```

The results include numerically equivalent Boolean and integer values.

[Back to Index](#index)

---

<a id="tuple-index-method"></a>

## `index()` Method

The `index()` method searches for a specified value and returns the index of its first occurrence.

It does not modify the tuple.

### Syntax

```python id="alnu6z"
tuple_name.index(value)
tuple_name.index(value, start)
tuple_name.index(value, start, stop)
```

The parameters are:

* `value`: value to search for
* `start`: optional index where the search begins
* `stop`: optional index where the search ends, not included

<a id="finding-first-occurrence"></a>

### Finding the First Occurrence

```python id="qf3qkc"
numbers = (10, 20, 30, 40, 50, 20)

position = numbers.index(20)

print("The first occurrence of 20 is at index:", position)
```

**Output:**

```text id="1hc3yk"
The first occurrence of 20 is at index: 1
```

Although `20` appears at indexes `1` and `5`, only the first matching index is returned.

```text id="suhmte"
Value:  10  20  30  40  50  20
Index:   0   1   2   3   4   5
             ↑
       first occurrence
```

[Back to Index](#index)

---

<a id="tuple-index-start"></a>

### Using the `start` Parameter

The optional `start` parameter specifies where the search should begin.

```python id="py4bnv"
numbers = (10, 20, 30, 40, 50, 20)

position = numbers.index(20, 2)

print(position)
```

**Output:**

```text id="cllzw8"
5
```

The search starts at index `2`, so the occurrence at index `1` is ignored.

```text id="npwbxr"
Search range:
Index 2 → end of tuple

Values checked:
30, 40, 50, 20
```

Negative starting indexes are also supported:

```python id="rsxbfa"
numbers = (10, 20, 30, 20, 40)

position = numbers.index(20, -3)

print(position)
```

**Output:**

```text id="0e9zkr"
3
```

The search begins three positions from the end.

[Back to Index](#index)

---

<a id="tuple-index-range"></a>

### Using `start` and `stop`

The search can be limited to a specific range.

```python id="qxrz4y"
letters = ("a", "b", "c", "b", "d", "b")

position = letters.index("b", 2, 5)

print(position)
```

**Output:**

```text id="ciqis6"
3
```

The search checks indexes `2`, `3`, and `4`.

Index `5` is excluded.

```text id="72sh3e"
Value:  a  b  c  b  d  b
Index:  0  1  2  3  4  5
               └─────┘
              searched
```

The syntax behaves similarly to slicing:

```python id="07ejcf"
tuple_name.index(value, start, stop)
```

However, `index()` returns an actual index from the original tuple, not an index relative to the selected range.

[Back to Index](#index)

---

<a id="tuple-index-missing-value"></a>

### Handling a Missing Value

If the value is not found in the specified search range, `index()` raises a `ValueError`.

```python id="v4kfak"
colors = ("red", "blue", "green")

position = colors.index("purple")
```

**Error:**

```text id="0g5ehe"
ValueError: tuple.index(x): x not in tuple
```

Check membership before calling `index()`:

```python id="ikqog0"
colors = ("red", "blue", "green")
target = "purple"

if target in colors:
    print(colors.index(target))
else:
    print("The value was not found.")
```

**Output:**

```text id="n4xxbu"
The value was not found.
```

Exception handling can also be used:

```python id="ty30j2"
colors = ("red", "blue", "green")

try:
    position = colors.index("purple")
    print(position)
except ValueError:
    print("The value was not found.")
```

**Output:**

```text id="j2k1yk"
The value was not found.
```

[Back to Index](#index)

---

<a id="tuple-len-function"></a>

## `len()` Function

The built-in `len()` function returns the number of top-level elements in a tuple.

### Syntax

```python id="ua28te"
len(tuple_name)
```

### Example

```python id="9go0az"
numbers = (10, 20, 30, 40)

length = len(numbers)

print(length)
print(type(length))
```

**Output:**

```text id="a4nfgx"
4
<class 'int'>
```

### Empty Tuple

```python id="ywa4yo"
empty_tuple = ()

print(len(empty_tuple))
```

**Output:**

```text id="ihzrka"
0
```

### Nested Tuple

A nested tuple counts as one top-level element.

```python id="owpo8d"
data = (
    10,
    20,
    (30, 40, 50),
)

print(len(data))
```

**Output:**

```text id="i44ezw"
3
```

The top-level elements are:

```text id="lsljvi"
10
20
(30, 40, 50)
```

The nested tuple's elements are not counted separately.

[Back to Index](#index)

---

<a id="tuple-min-function"></a>

## `min()` Function

The built-in `min()` function returns the smallest element in a non-empty tuple.

### Syntax

```python id="uf1aki"
min(tuple_name)
```

### Numeric Example

```python id="chunqh"
values = (5, 2, 8, 1)

smallest = min(values)

print(smallest)
```

**Output:**

```text id="jp9fof"
1
```

Integers and floats can be compared numerically:

```python id="7ieybv"
values = (5, 2.5, 8, 1.2)

print(min(values))
```

**Output:**

```text id="dwzcpe"
1.2
```

[Back to Index](#index)

---

<a id="tuple-min-strings"></a>

### `min()` with Strings

Strings are compared lexicographically according to their Unicode code points.

```python id="wh9e3k"
fruits = ("banana", "apple", "cherry")

print(min(fruits))
```

**Output:**

```text id="85ylcn"
apple
```

String comparison is case-sensitive:

```python id="h2ttrb"
words = ("banana", "Apple", "cherry")

print(min(words))
```

**Output:**

```text id="plw2gm"
Apple
```

Uppercase and lowercase characters have different Unicode code points.

Use `key=str.lower` with the multi-argument form of `min()` for a case-insensitive comparison:

```python id="kcm53i"
words = ("banana", "Apple", "cherry")

smallest = min(words, key=str.lower)

print(smallest)
```

**Output:**

```text id="p8zj0t"
Apple
```

[Back to Index](#index)

---

<a id="tuple-min-errors"></a>

### `min()` Errors

Calling `min()` on an empty tuple raises a `ValueError`.

```python id="4jkujf"
values = ()

print(min(values))
```

**Error:**

```text id="9pj06x"
ValueError: min() arg is an empty sequence
```

Values must also be mutually comparable.

```python id="pt6vhw"
values = (10, "20", 30)

print(min(values))
```

**Error:**

```text id="2ovxku"
TypeError: '<' not supported between instances of 'str' and 'int'
```

Mixed numeric types such as integers and floats can be compared, but unrelated types such as strings and integers generally cannot.

[Back to Index](#index)

---

<a id="tuple-max-function"></a>

## `max()` Function

The built-in `max()` function returns the largest element in a non-empty tuple.

### Syntax

```python id="vlprvj"
max(tuple_name)
```

### Numeric Example

```python id="4o8vp4"
values = (5, 2, 8, 1)

largest = max(values)

print(largest)
```

**Output:**

```text id="fxr4g9"
8
```

### Mixed Numeric Types

```python id="fvuh0p"
values = (5, 9.5, 8, 1.2)

print(max(values))
```

**Output:**

```text id="qz8kkn"
9.5
```

[Back to Index](#index)

---

<a id="tuple-max-strings"></a>

### `max()` with Strings

```python id="1ft0hf"
fruits = ("banana", "apple", "cherry")

print(max(fruits))
```

**Output:**

```text id="a05ksp"
cherry
```

The strings are compared lexicographically.

A `key` function can control the comparison:

```python id="ooy0sk"
words = ("cat", "elephant", "tiger")

longest = max(words, key=len)

print(longest)
```

**Output:**

```text id="0iuz45"
elephant
```

The value with the greatest length is returned.

[Back to Index](#index)

---

<a id="tuple-max-errors"></a>

### `max()` Errors

Calling `max()` on an empty tuple raises a `ValueError`.

```python id="t0822z"
values = ()

print(max(values))
```

**Error:**

```text id="23q8mb"
ValueError: max() arg is an empty sequence
```

Incompatible values raise a `TypeError`:

```python id="f7lciz"
values = (10, "20", 30)

print(max(values))
```

**Error:**

```text id="n2u4ke"
TypeError: '>' not supported between instances of 'str' and 'int'
```

[Back to Index](#index)

---

<a id="tuple-sum-function"></a>

## `sum()` Function

The built-in `sum()` function adds the numeric elements of an iterable.

### Syntax

```python id="2rur31"
sum(iterable)
sum(iterable, start)
```

### Example

```python id="i7sp4n"
values = (5, 10, 15)

total = sum(values)

print(total)
```

**Output:**

```text id="6vfijj"
30
```

The calculation is:

```text id="mlv4oj"
0 + 5 + 10 + 15 = 30
```

By default, `sum()` begins with `0`.

### Integers and Floats

```python id="bv4v0r"
values = (5, 2.5, 7)

print(sum(values))
```

**Output:**

```text id="m7wl23"
14.5
```

Because one value is a float, the result is a float.

### Empty Tuple

```python id="0o2wpo"
values = ()

print(sum(values))
```

**Output:**

```text id="8mk7kw"
0
```

Unlike `min()` and `max()`, `sum()` can process an empty tuple because its default starting value is `0`.

### Boolean Values

Booleans behave like integers in numeric operations.

```python id="gw84uz"
values = (True, False, True, True)

print(sum(values))
```

**Output:**

```text id="exxkpe"
3
```

This can be used to count how many Boolean conditions are true.

[Back to Index](#index)

---

<a id="tuple-sum-start"></a>

### Using the Optional Start Value

The second argument provides an initial value for the total.

```python id="02stcj"
values = (5, 10, 15)

result = sum(values, 100)

print(result)
```

**Output:**

```text id="zp6xjv"
130
```

The calculation is:

```text id="ylk20p"
100 + 5 + 10 + 15 = 130
```

The start value is added only once.

```python id="rrtx1x"
empty_values = ()

print(sum(empty_values, 100))
```

**Output:**

```text id="lr24b9"
100
```

[Back to Index](#index)

---

<a id="tuple-sum-errors"></a>

### `sum()` Errors

The elements must support addition with the running total.

A tuple containing strings cannot be passed directly to `sum()`:

```python id="8i5jt7"
words = ("Python", "is", "readable")

print(sum(words))
```

**Error:**

```text id="d5mhj7"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Use `join()` to combine strings:

```python id="ntxzyq"
words = ("Python", "is", "readable")

sentence = " ".join(words)

print(sentence)
```

**Output:**

```text id="nu2p4c"
Python is readable
```

A tuple containing incompatible numeric and non-numeric values also raises a `TypeError`.

```python id="o0w4xl"
values = (10, 20, "30")

print(sum(values))
```

**Error:**

```text id="4cptlj"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Convert compatible numeric strings before summing:

```python id="0fmgy9"
values = ("10", "20", "30")

converted_values = tuple(int(value) for value in values)

print(sum(converted_values))
```

**Output:**

```text id="58vxfh"
60
```

[Back to Index](#index)

---

<a id="tuple-functions-combined-example"></a>

## Combined Example

The following program uses tuple methods and built-in functions together.

```python id="4jdguv"
scores = (85, 92, 78, 92, 88, 95, 92)

target_score = 92

print("Scores:", scores)
print("Number of scores:", len(scores))
print("Lowest score:", min(scores))
print("Highest score:", max(scores))
print("Total score:", sum(scores))
print("Occurrences of 92:", scores.count(target_score))

if target_score in scores:
    print(
        "First index of 92:",
        scores.index(target_score),
    )
```

**Output:**

```text id="mmcm1h"
Scores: (85, 92, 78, 92, 88, 95, 92)
Number of scores: 7
Lowest score: 78
Highest score: 95
Total score: 622
Occurrences of 92: 3
First index of 92: 1
```

### Calculating the Average

```python id="2kdzmw"
scores = (85, 92, 78, 92, 88, 95, 92)

average = sum(scores) / len(scores)

print(f"Average score: {average:.2f}")
```

**Output:**

```text id="jd5cka"
Average score: 88.86
```

Before calculating an average, ensure that the tuple is not empty:

```python id="dlrd50"
scores = ()

if scores:
    average = sum(scores) / len(scores)
    print(average)
else:
    print("No scores are available.")
```

**Output:**

```text id="rwkm4q"
No scores are available.
```

[Back to Index](#index)

---

<a id="tuple-functions-summary"></a>

## Summary

| Operation                 | Syntax                            | Result                          |
| ------------------------- | --------------------------------- | ------------------------------- |
| Count a value             | `items.count(value)`              | Number of matching elements     |
| Find the first index      | `items.index(value)`              | Index of the first match        |
| Search from an index      | `items.index(value, start)`       | First match at or after `start` |
| Search within a range     | `items.index(value, start, stop)` | First match before `stop`       |
| Get tuple length          | `len(items)`                      | Number of top-level elements    |
| Find the minimum          | `min(items)`                      | Smallest comparable element     |
| Find the maximum          | `max(items)`                      | Largest comparable element      |
| Calculate the total       | `sum(items)`                      | Sum of numeric elements         |
| Sum with an initial value | `sum(items, start)`               | Initial value plus all elements |

### Behavior with an Empty Tuple

```python id="wbelmo"
empty_tuple = ()
```

| Operation                  | Result              |
| -------------------------- | ------------------- |
| `len(empty_tuple)`         | `0`                 |
| `empty_tuple.count(value)` | `0`                 |
| `sum(empty_tuple)`         | `0`                 |
| `min(empty_tuple)`         | Raises `ValueError` |
| `max(empty_tuple)`         | Raises `ValueError` |
| `empty_tuple.index(value)` | Raises `ValueError` |

[Back to Index](#index)