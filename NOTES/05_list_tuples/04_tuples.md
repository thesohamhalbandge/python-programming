<a id="tuples-in-python"></a>

## Tuples in Python

A **tuple** is an ordered collection of elements.

Tuples can store:

* Integers
* Floats
* Strings
* Boolean values
* Lists
* Other tuples
* Mixed data types

The main characteristic of a tuple is that it is **immutable**. After a tuple has been created, its element references cannot be added, removed, or replaced.

<a id="index"></a>

## Index

1. [Characteristics of Tuples](#tuple-characteristics)
2. [Creating Tuples](#creating-tuples)

   * [Using Parentheses](#tuple-parentheses)
   * [Tuple Packing](#tuple-packing)
   * [Using the `tuple()` Constructor](#tuple-constructor)
   * [Creating a Single-Element Tuple](#single-element-tuple)
   * [Creating an Empty Tuple](#empty-tuple)
3. [Tuples Versus Lists](#tuples-versus-lists)
4. [Nested Tuples](#nested-tuples)
5. [Tuple Packing and Unpacking](#tuple-packing-unpacking)
6. [Positive Tuple Indexing](#positive-tuple-indexing)
7. [Negative Tuple Indexing](#negative-tuple-indexing)
8. [Tuple Slicing](#tuple-slicing)

   * [Basic Slicing](#basic-tuple-slicing)
   * [Omitting Slice Boundaries](#omitting-tuple-slice-boundaries)
   * [Slicing with a Step](#tuple-step-slicing)
   * [Negative-Index Slicing](#negative-tuple-slicing)
   * [Reversing a Tuple](#reversing-a-tuple)
9. [Tuple Immutability](#tuple-immutability)

   * [Creating a Modified Tuple](#creating-modified-tuple)
   * [Mutable Objects Inside Tuples](#mutable-elements-in-tuples)
10. [Tuple Methods](#tuple-methods)

    * [`count()`](#tuple-count)
    * [`index()`](#tuple-index)
11. [Iterating Through Tuples](#iterating-tuples)

    * [Direct Iteration](#direct-tuple-iteration)
    * [Iteration with Indexes](#tuple-iteration-indexes)
    * [Using `enumerate()`](#tuple-enumerate)
12. [Tuples as Dictionary Keys](#tuples-as-dictionary-keys)
13. [Tuple Summary](#tuple-summary)

---

<a id="tuple-characteristics"></a>

## Characteristics of Tuples

Python tuples have several important characteristics.

### 1. Ordered

Tuple elements maintain their insertion order.

```python id="r4it3e"
colors = ("red", "green", "blue")

print(colors)
```

**Output:**

```text id="v6jwmm"
('red', 'green', 'blue')
```

The first element remains `"red"`, the second remains `"green"`, and the third remains `"blue"`.

### 2. Immutable

After creation, tuple elements cannot be replaced, added, or removed.

```python id="md96hy"
coordinates = (10, 20)

coordinates[0] = 50
```

**Error:**

```text id="f2fddj"
TypeError: 'tuple' object does not support item assignment
```

### 3. Allows Duplicate Values

A tuple may contain the same value more than once.

```python id="a13uj8"
numbers = (1, 2, 2, 3, 2)

print(numbers)
```

**Output:**

```text id="htzy71"
(1, 2, 2, 3, 2)
```

### 4. Allows Mixed Data Types

```python id="ra6bno"
record = ("Alice", 25, 5.6, True)

print(record)
```

**Output:**

```text id="o45il8"
('Alice', 25, 5.6, True)
```

### 5. Supports Indexing and Slicing

Tuple elements can be accessed using positive indexes, negative indexes, and slices.

```python id="6ou9vl"
values = (10, 20, 30, 40)

print(values[0])
print(values[-1])
print(values[1:3])
```

**Output:**

```text id="ixyobd"
10
40
(20, 30)
```

### 6. Can Contain Mutable Objects

A tuple itself is immutable, but it can contain mutable objects such as lists.

```python id="md7h1d"
data = ([1, 2], [3, 4])

data[0].append(99)

print(data)
```

**Output:**

```text id="4h783o"
([1, 2, 99], [3, 4])
```

The tuple still refers to the same list object, but the contents of that list can change.

[Back to Index](#index)

---

<a id="creating-tuples"></a>

## Creating Tuples

Tuples can be created in several ways:

* Using parentheses
* Using comma-separated values
* Using the `tuple()` constructor
* Creating an empty tuple
* Creating a single-element tuple

<a id="tuple-parentheses"></a>

### 1. Using Parentheses

The most common form places comma-separated elements inside parentheses.

```python id="buarpe"
numbers = (1, 2, 3)

print(numbers)
print(type(numbers))
```

**Output:**

```text id="j7sbdd"
(1, 2, 3)
<class 'tuple'>
```

The parentheses improve readability, but the commas are what create the tuple.

[Back to Index](#index)

---

<a id="tuple-packing"></a>

### 2. Tuple Packing

A tuple can be created without parentheses by separating values with commas.

```python id="aq7fnf"
coordinates = 10, 20, 30

print(coordinates)
print(type(coordinates))
```

**Output:**

```text id="ac6wix"
(10, 20, 30)
<class 'tuple'>
```

This process is called **tuple packing** because several values are packed into one tuple.

The following statements create equivalent tuples:

```python id="pmf4k3"
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3

print(tuple1 == tuple2)
```

**Output:**

```text id="jkzt08"
True
```

Parentheses are still recommended when they make the expression clearer.

[Back to Index](#index)

---

<a id="tuple-constructor"></a>

### 3. Using the `tuple()` Constructor

The `tuple()` constructor creates a tuple from an iterable.

### From a List

```python id="c32un6"
numbers_list = [1, 2, 3]
numbers_tuple = tuple(numbers_list)

print(numbers_tuple)
print(type(numbers_tuple))
```

**Output:**

```text id="w1vekb"
(1, 2, 3)
<class 'tuple'>
```

### From a String

A string is an iterable of characters.

```python id="g99yqe"
text = "Python"
characters = tuple(text)

print(characters)
```

**Output:**

```text id="d3pmjh"
('P', 'y', 't', 'h', 'o', 'n')
```

### From a Range

```python id="5243ov"
numbers = tuple(range(1, 6))

print(numbers)
```

**Output:**

```text id="d3d4z0"
(1, 2, 3, 4, 5)
```

### From a Set

```python id="jl6n9y"
values = tuple({10, 20, 30})

print(values)
```

The resulting order should not be relied upon because sets are unordered collections.

### From a Dictionary

Converting a dictionary to a tuple produces a tuple of its keys.

```python id="d45dwi"
user = {
    "name": "Alice",
    "age": 25,
}

keys = tuple(user)

print(keys)
```

**Output:**

```text id="ifxb6g"
('name', 'age')
```

Use `values()` to convert the values:

```python id="kvlo1v"
values = tuple(user.values())

print(values)
```

**Output:**

```text id="h5hfxs"
('Alice', 25)
```

[Back to Index](#index)

---

<a id="single-element-tuple"></a>

### 4. Creating a Single-Element Tuple

A single-element tuple requires a trailing comma.

```python id="cjxkxf"
single_value = (1,)

print(single_value)
print(type(single_value))
```

**Output:**

```text id="t9ii9i"
(1,)
<class 'tuple'>
```

Without the comma, Python treats the parentheses as ordinary grouping.

```python id="s1fe1u"
value = (1)

print(value)
print(type(value))
```

**Output:**

```text id="a8s0wb"
1
<class 'int'>
```

The comma creates the tuple:

```python id="wrxqpv"
value = 1,

print(value)
print(type(value))
```

**Output:**

```text id="2w93lx"
(1,)
<class 'tuple'>
```

> Parentheses alone do not create a tuple. The comma is essential.

[Back to Index](#index)

---

<a id="empty-tuple"></a>

### 5. Creating an Empty Tuple

An empty tuple can be created using empty parentheses.

```python id="u8bte4"
empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))
```

**Output:**

```text id="t0gyvb"
()
<class 'tuple'>
```

It can also be created using `tuple()`:

```python id="e9l65o"
empty_tuple = tuple()

print(empty_tuple)
```

**Output:**

```text id="45h2go"
()
```

[Back to Index](#index)

---

<a id="tuples-versus-lists"></a>

## Tuples Versus Lists

Tuples and lists are both ordered collections, but they differ mainly in mutability and intended use.

| Feature                    | Tuple                | List                                         |
| -------------------------- | -------------------- | -------------------------------------------- |
| Syntax                     | `(1, 2, 3)`          | `[1, 2, 3]`                                  |
| Ordered                    | Yes                  | Yes                                          |
| Mutable                    | No                   | Yes                                          |
| Supports indexing          | Yes                  | Yes                                          |
| Supports slicing           | Yes                  | Yes                                          |
| Allows duplicates          | Yes                  | Yes                                          |
| Allows mixed types         | Yes                  | Yes                                          |
| Can add or remove elements | No                   | Yes                                          |
| Common methods             | `count()`, `index()` | `append()`, `remove()`, `sort()`, and others |
| Suitable as dictionary key | Sometimes            | No                                           |

### Tuple Example

A tuple is useful for values that conceptually belong together and should not be reassigned individually.

```python id="tvq8k7"
dimensions = (1920, 1080)

print(dimensions)
```

**Output:**

```text id="ma0sk4"
(1920, 1080)
```

### List Example

A list is appropriate when the collection will change.

```python id="f2f8gy"
scores = [95, 88, 92, 85]

scores.append(100)

print(scores)
```

**Output:**

```text id="8jwvum"
[95, 88, 92, 85, 100]
```

### Performance Considerations

Tuples may use slightly less memory than equivalent lists and can sometimes be processed marginally faster.

However, the difference is usually small. Choose between a tuple and a list primarily according to meaning and mutability requirements:

* Use a tuple for a fixed record or fixed sequence.
* Use a list for a collection that needs to change.

### Homogeneous and Heterogeneous Data

Tuples are often used for heterogeneous records:

```python id="flsshn"
employee = ("Alice", 25, "Developer")
```

Lists are often used for collections of similar items:

```python id="pq416f"
scores = [85, 90, 78, 92]
```

These are common conventions rather than strict rules. Both structures can contain mixed or matching data types.

[Back to Index](#index)

---

<a id="nested-tuples"></a>

## Nested Tuples

A nested tuple contains one or more tuples as elements.

Nested tuples are useful for representing structured records, coordinates, tables, and grouped data.

### Example

```python id="lf03bl"
employee_records = (
    ("John Doe", "Sales", (2015, "Manager")),
    ("Jane Smith", "IT", (2018, "Developer")),
)

print(employee_records)
```

**Output:**

```text id="6w4msp"
(('John Doe', 'Sales', (2015, 'Manager')), ('Jane Smith', 'IT', (2018, 'Developer')))
```

### Accessing Nested Elements

```python id="5w38kw"
employee_records = (
    ("John Doe", "Sales", (2015, "Manager")),
    ("Jane Smith", "IT", (2018, "Developer")),
)

print(employee_records[0])
print(employee_records[0][0])
print(employee_records[0][2])
print(employee_records[0][2][1])
```

**Output:**

```text id="5gwd31"
('John Doe', 'Sales', (2015, 'Manager'))
John Doe
(2015, 'Manager')
Manager
```

The expression:

```python id="1ukopg"
employee_records[0][2][1]
```

is evaluated as follows:

```text id="gdfmrx"
employee_records[0]
→ ('John Doe', 'Sales', (2015, 'Manager'))

employee_records[0][2]
→ (2015, 'Manager')

employee_records[0][2][1]
→ 'Manager'
```

[Back to Index](#index)

---

<a id="tuple-packing-unpacking"></a>

## Tuple Packing and Unpacking

Tuple packing combines several values into one tuple.

```python id="i4uozw"
employee = "Alice", "IT", 2020

print(employee)
```

**Output:**

```text id="9tsvv8"
('Alice', 'IT', 2020)
```

Tuple unpacking assigns tuple elements to separate variables.

```python id="k9v0rl"
employee = ("Alice", "IT", 2020)

name, department, start_year = employee

print(name)
print(department)
print(start_year)
```

**Output:**

```text id="764axz"
Alice
IT
2020
```

The number of variables must match the number of tuple elements.

```python id="d1dq0x"
coordinates = (10, 20, 30)

x, y = coordinates
```

**Error:**

```text id="a2ttb1"
ValueError: too many values to unpack (expected 2)
```

### Nested Tuple Unpacking

```python id="tyf0ye"
employee = (
    "John Doe",
    "Sales",
    (2015, "Manager"),
)

employee_name, department, (start_year, position) = employee

print(
    f"Employee: {employee_name}, "
    f"Department: {department}, "
    f"Start Year: {start_year}, "
    f"Position: {position}"
)
```

**Output:**

```text id="zx2pha"
Employee: John Doe, Department: Sales, Start Year: 2015, Position: Manager
```

### Extended Unpacking

Use `*` to collect remaining elements into a list.

```python id="5h8z9x"
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

**Output:**

```text id="xoupku"
10
[20, 30, 40]
50
```

Although the original value is a tuple, the starred variable receives a list.

[Back to Index](#index)

---

<a id="positive-tuple-indexing"></a>

## Positive Tuple Indexing

Tuples are ordered, so each element has an index.

Positive indexing begins at `0`.

```python id="6ey9b4"
values = (10, 20, 30, 40)
```

The indexes are:

```text id="jp9nby"
Element:  10  20  30  40
Index:     0   1   2   3
```

### Example

```python id="izjfnp"
values = (10, 20, 30, 40)

first_item = values[0]
second_item = values[1]

print(first_item)
print(second_item)
```

**Output:**

```text id="lnmb2t"
10
20
```

### Invalid Index

Accessing an index that does not exist raises an `IndexError`.

```python id="ie92yj"
values = (10, 20, 30, 40)

print(values[4])
```

**Error:**

```text id="kib27c"
IndexError: tuple index out of range
```

For a tuple containing four elements, the valid positive indexes are:

```text id="hxqa3o"
0, 1, 2, 3
```

[Back to Index](#index)

---

<a id="negative-tuple-indexing"></a>

## Negative Tuple Indexing

Negative indexes access elements from the end of a tuple.

* `-1` is the last element.
* `-2` is the second-to-last element.
* `-3` is the third-to-last element.

```python id="47lw4s"
colors = (
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
)
```

The indexes are:

```text id="i4dg9s"
Element:         red  blue  green  yellow  purple
Positive index:   0     1      2       3       4
Negative index:  -5    -4     -3      -2      -1
```

### Example

```python id="4ms02n"
colors = (
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
)

last_color = colors[-1]
second_last_color = colors[-2]

print(last_color)
print(second_last_color)
```

**Output:**

```text id="2wvm2e"
purple
yellow
```

Negative indexing is useful when the tuple's exact length is unknown.

[Back to Index](#index)

---

<a id="tuple-slicing"></a>

## Tuple Slicing

Slicing extracts a range of elements from a tuple.

### Syntax

```python id="55b792"
tuple_name[start:stop:step]
```

The parameters are:

* `start`: beginning index, included
* `stop`: ending index, excluded
* `step`: distance between selected elements

All three values are optional.

A tuple slice produces a new tuple.

<a id="basic-tuple-slicing"></a>

### 1. Basic Slicing

```python id="895ygz"
numbers = (1, 2, 3, 4, 5, 6, 7)

result = numbers[2:5]

print(result)
print(type(result))
```

**Output:**

```text id="3dqav9"
(3, 4, 5)
<class 'tuple'>
```

The selected indexes are `2`, `3`, and `4`. Index `5` is excluded.

```text id="tg9j2e"
Index:   0  1  2  3  4  5  6
Value:   1  2  3  4  5  6  7
               └─────┘
```

[Back to Index](#index)

---

<a id="omitting-tuple-slice-boundaries"></a>

### 2. Omitting Slice Boundaries

Omit `start` to begin from the start of the tuple.

```python id="e7sk9l"
numbers = (1, 2, 3, 4, 5, 6, 7)

print(numbers[:4])
```

**Output:**

```text id="sjnvur"
(1, 2, 3, 4)
```

Omit `stop` to continue to the end.

```python id="ht1wug"
print(numbers[3:])
```

**Output:**

```text id="z7413c"
(4, 5, 6, 7)
```

Omit both to select the entire tuple.

```python id="okxz8a"
print(numbers[:])
```

**Output:**

```text id="16l07t"
(1, 2, 3, 4, 5, 6, 7)
```

For an immutable tuple, creating a full slice may return the same tuple object because no independent mutable container is required.

Do not rely on identity behavior here. Use equality when comparing tuple values.

[Back to Index](#index)

---

<a id="tuple-step-slicing"></a>

### 3. Slicing with a Step

The step determines the interval between selected elements.

```python id="lcxco8"
numbers = (1, 2, 3, 4, 5, 6, 7)

result = numbers[0:7:2]

print(result)
```

**Output:**

```text id="g48qsg"
(1, 3, 5, 7)
```

The selected indexes are:

```text id="5iyu8e"
0, 2, 4, 6
```

### Every Third Element

```python id="dpkw6m"
values = (10, 20, 30, 40, 50, 60, 70)

print(values[::3])
```

**Output:**

```text id="fcdtl0"
(10, 40, 70)
```

[Back to Index](#index)

---

<a id="negative-tuple-slicing"></a>

### 4. Negative-Index Slicing

Negative indexes can define slice boundaries relative to the end.

```python id="np9zrz"
numbers = (1, 2, 3, 4, 5, 6, 7)

result = numbers[-5:-2]

print(result)
```

**Output:**

```text id="uw1vxu"
(3, 4, 5)
```

The negative indexes correspond to:

```text id="kit257"
Value:           1   2   3   4   5   6   7
Negative index: -7  -6  -5  -4  -3  -2  -1
```

The slice begins at `-5` and stops before `-2`.

[Back to Index](#index)

---

<a id="reversing-a-tuple"></a>

### 5. Reversing a Tuple

Use a step of `-1` to create a reversed tuple.

```python id="s6po00"
numbers = (1, 2, 3, 4, 5, 6, 7)

reversed_numbers = numbers[::-1]

print(reversed_numbers)
```

**Output:**

```text id="91i4w5"
(7, 6, 5, 4, 3, 2, 1)
```

The original tuple remains unchanged.

```python id="pfrkff"
print(numbers)
```

**Output:**

```text id="wh24to"
(1, 2, 3, 4, 5, 6, 7)
```

### Partial Reverse Slice

```python id="9lbon6"
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[4:1:-1])
```

**Output:**

```text id="1um2zv"
(50, 40, 30)
```

The selected indexes are `4`, `3`, and `2`. Index `1` is excluded.

[Back to Index](#index)

---

<a id="tuple-immutability"></a>

## Tuple Immutability

Tuple elements cannot be reassigned after creation.

```python id="tuaez4"
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

days[0] = "Funday"
```

**Error:**

```text id="ybzfmi"
TypeError: 'tuple' object does not support item assignment
```

Tuples also do not provide methods such as:

* `append()`
* `insert()`
* `remove()`
* `pop()`
* `clear()`
* `sort()`
* `reverse()`

These methods would modify the tuple, which is not allowed.

<a id="creating-modified-tuple"></a>

### Creating a Modified Tuple

To represent changed data, create a new tuple.

```python id="in3kh6"
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

new_days = ("Funday",) + days[1:]

print(new_days)
```

**Output:**

```text id="b84eii"
('Funday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
```

The expression works as follows:

```text id="m7xfnx"
("Funday",)
+
("Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
```

The original tuple remains unchanged.

```python id="0oevhu"
print(days[0])
```

**Output:**

```text id="tlw2eq"
Monday
```

[Back to Index](#index)

---

<a id="mutable-elements-in-tuples"></a>

### Mutable Objects Inside Tuples

Tuple immutability means that the tuple's element references cannot be replaced.

It does not guarantee that every contained object is immutable.

```python id="iwg7dx"
data = (
    "Alice",
    [80, 90, 95],
)

data[1].append(100)

print(data)
```

**Output:**

```text id="ym31fv"
('Alice', [80, 90, 95, 100])
```

The list stored inside the tuple is mutable.

However, replacing that list is not allowed:

```python id="x6sxwz"
data[1] = [70, 75]
```

**Error:**

```text id="pj1e6j"
TypeError: 'tuple' object does not support item assignment
```

Therefore, a tuple does not automatically make all nested data immutable.

[Back to Index](#index)

---

<a id="tuple-methods"></a>

## Tuple Methods

Because tuples are immutable, they provide only two commonly used methods:

* `count()`
* `index()`

<a id="tuple-count"></a>

### 1. `count()`

The `count()` method returns the number of times a value occurs.

### Syntax

```python id="2wmt5c"
tuple_name.count(value)
```

### Example

```python id="ewzi8h"
numbers = (1, 2, 3, 2, 4, 2)

result = numbers.count(2)

print(result)
```

**Output:**

```text id="w8jzak"
3
```

When the value is absent, `count()` returns `0`.

```python id="i6l3ug"
print(numbers.count(10))
```

**Output:**

```text id="7bbzh7"
0
```

[Back to Index](#index)

---

<a id="tuple-index"></a>

### 2. `index()`

The `index()` method returns the index of the first matching value.

### Syntax

```python id="93w8y9"
tuple_name.index(value)
tuple_name.index(value, start)
tuple_name.index(value, start, stop)
```

### Example

```python id="itycp8"
colors = ("red", "blue", "green", "blue")

position = colors.index("blue")

print(position)
```

**Output:**

```text id="wdime4"
1
```

Only the first matching index is returned.

### Starting the Search Later

```python id="37p6mq"
second_position = colors.index("blue", 2)

print(second_position)
```

**Output:**

```text id="r2v3by"
3
```

### Missing Value

If the value is absent, `index()` raises a `ValueError`.

```python id="g9svow"
colors.index("purple")
```

**Error:**

```text id="z93v3r"
ValueError: tuple.index(x): x not in tuple
```

Check membership first when the value may be missing:

```python id="r29h6c"
target = "purple"

if target in colors:
    print(colors.index(target))
else:
    print("The value was not found.")
```

**Output:**

```text id="jpw60b"
The value was not found.
```

[Back to Index](#index)

---

<a id="iterating-tuples"></a>

## Iterating Through Tuples

A tuple is iterable, so its elements can be processed using loops.

<a id="direct-tuple-iteration"></a>

### 1. Direct Iteration

The most direct approach is to loop through the elements.

```python id="1emqrw"
numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number)
```

**Output:**

```text id="xkik2u"
1
2
3
4
5
```

The loop variable receives each tuple element in order.

### Iterating Through Records

```python id="n9gwse"
employees = (
    ("Alice", "IT"),
    ("Bob", "Sales"),
    ("Charlie", "Finance"),
)

for employee in employees:
    print(employee)
```

**Output:**

```text id="ny23ky"
('Alice', 'IT')
('Bob', 'Sales')
('Charlie', 'Finance')
```

### Unpacking During Iteration

```python id="cjb2nh"
employees = (
    ("Alice", "IT"),
    ("Bob", "Sales"),
    ("Charlie", "Finance"),
)

for name, department in employees:
    print(f"{name} works in {department}.")
```

**Output:**

```text id="b7u78g"
Alice works in IT.
Bob works in Sales.
Charlie works in Finance.
```

[Back to Index](#index)

---

<a id="tuple-iteration-indexes"></a>

### 2. Iteration with Indexes

Use `range()` and `len()` when explicit index access is required.

```python id="1mvxtu"
colors = ("red", "blue", "green", "yellow")

for index in range(len(colors)):
    print(colors[index])
```

**Output:**

```text id="z0nlbw"
red
blue
green
yellow
```

To display both indexes and elements:

```python id="gjdr86"
for index in range(len(colors)):
    print(f"Index {index}: {colors[index]}")
```

**Output:**

```text id="ir2y4q"
Index 0: red
Index 1: blue
Index 2: green
Index 3: yellow
```

Direct iteration is normally clearer when indexes are not needed.

[Back to Index](#index)

---

<a id="tuple-enumerate"></a>

### 3. Using `enumerate()`

The built-in `enumerate()` function provides both the index and element.

```python id="gb726e"
colors = ("red", "blue", "green", "yellow")

for index, color in enumerate(colors):
    print(f"Index {index}: {color}")
```

**Output:**

```text id="i9to2q"
Index 0: red
Index 1: blue
Index 2: green
Index 3: yellow
```

A custom starting index can be supplied:

```python id="nx9oz3"
for position, color in enumerate(colors, start=1):
    print(f"{position}. {color}")
```

**Output:**

```text id="7fvz2i"
1. red
2. blue
3. green
4. yellow
```

[Back to Index](#index)

---

<a id="tuples-as-dictionary-keys"></a>

## Tuples as Dictionary Keys

A dictionary key must be **hashable**.

A tuple can be used as a dictionary key only when all its elements are also hashable.

### Valid Tuple Key

```python id="8gluu9"
locations = {
    (19.0760, 72.8777): "Mumbai",
    (28.6139, 77.2090): "Delhi",
}

print(locations[(19.0760, 72.8777)])
```

**Output:**

```text id="iiipq3"
Mumbai
```

The coordinate tuples contain floats, which are hashable.

### Invalid Tuple Key

A tuple containing a list is not hashable.

```python id="wgqa2q"
invalid_key = ([1, 2], 3)

data = {
    invalid_key: "value"
}
```

**Error:**

```text id="8ysl6k"
TypeError: unhashable type: 'list'
```

Tuple immutability alone does not guarantee hashability. Every nested element must also be hashable.

Common hashable tuple elements include:

* Integers
* Floats
* Strings
* Boolean values
* `None`
* Other hashable tuples

[Back to Index](#index)

---

<a id="tuple-summary"></a>

## Tuple Summary

| Operation            | Syntax               | Result                        |
| -------------------- | -------------------- | ----------------------------- |
| Create a tuple       | `(1, 2, 3)`          | Tuple with three elements     |
| Tuple packing        | `1, 2, 3`            | Tuple with three elements     |
| Empty tuple          | `()`                 | Empty tuple                   |
| Single-element tuple | `(1,)`               | Tuple containing one element  |
| Convert an iterable  | `tuple(iterable)`    | New tuple                     |
| Positive indexing    | `items[0]`           | First element                 |
| Negative indexing    | `items[-1]`          | Last element                  |
| Basic slicing        | `items[1:4]`         | New tuple containing a range  |
| Reverse slicing      | `items[::-1]`        | Reversed tuple                |
| Count values         | `items.count(value)` | Number of matches             |
| Find index           | `items.index(value)` | First matching index          |
| Unpack tuple         | `a, b = items`       | Assigns elements to variables |
| Iterate directly     | `for item in items:` | Processes each element        |

### Combined Example

```python id="foy8qw"
student = (
    "Alice",
    21,
    ("Python", "SQL", "Git"),
)

name, age, skills = student

print(f"Name: {name}")
print(f"Age: {age}")
print("Skills:")

for position, skill in enumerate(skills, start=1):
    print(f"{position}. {skill}")

print("First skill:", skills[0])
print("Last skill:", skills[-1])
print("Reversed skills:", skills[::-1])
print("Python count:", skills.count("Python"))
```

**Output:**

```text id="yc99xw"
Name: Alice
Age: 21
Skills:
1. Python
2. SQL
3. Git
First skill: Python
Last skill: Git
Reversed skills: ('Git', 'SQL', 'Python')
Python count: 1
```

[Back to Index](#index)