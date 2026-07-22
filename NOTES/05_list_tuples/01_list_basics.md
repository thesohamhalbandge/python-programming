<a id="lists-in-python"></a>

## Lists in Python

A **list** is an ordered and mutable collection of items.

Lists can store:

* Integers
* Floats
* Strings
* Boolean values
* Other lists
* Mixed data types

Because lists are mutable, their contents can be changed after creation.

<a id="index"></a>

## Index

1. [Creating Lists](#creating-lists)

   * [Using Square Brackets](#lists-square-brackets)
   * [Using the `list()` Constructor](#list-constructor)
   * [Creating Mixed and Nested Lists](#mixed-and-nested-lists)
2. [Accessing Elements with Positive Indexes](#positive-list-indexing)

   * [Index Errors](#list-index-errors)
3. [Accessing Elements with Negative Indexes](#negative-list-indexing)
4. [Modifying List Elements](#modifying-list-elements)

   * [Using Positive Indexes](#modify-positive-index)
   * [Using Negative Indexes](#modify-negative-index)
5. [Adding Elements with `append()`](#append-method)
6. [Adding Elements with `insert()`](#insert-method)
7. [Removing Elements with `remove()`](#remove-method)
8. [Removing Elements with `pop()`](#pop-method)

   * [Removing the Last Element](#pop-last-element)
   * [Removing by Index](#pop-specific-index)
9. [Checking List Length](#checking-list-length)
10. [Using List Length in Loops](#list-length-loops)
11. [List Method Summary](#list-method-summary)

---

<a id="creating-lists"></a>

## Creating Lists

Lists can be created using:

* Square brackets: `[]`
* The built-in `list()` constructor

<a id="lists-square-brackets"></a>

### 1. Using Square Brackets

An empty list can be created using empty square brackets.

```python
empty_list = []

print(empty_list)
print(type(empty_list))
```

**Output:**

```text
[]
<class 'list'>
```

A list containing values can be created by placing comma-separated items inside square brackets.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits)
```

**Output:**

```text
['apple', 'banana', 'cherry']
```

[Back to Index](#index)

---

<a id="list-constructor"></a>

### 2. Using the `list()` Constructor

The `list()` constructor can also create an empty list.

```python
empty_list = list()

print(empty_list)
```

**Output:**

```text
[]
```

The `list()` constructor can convert an iterable into a list.

For example, converting a string creates a list containing its individual characters:

```python
text = "hello"
characters = list(text)

print(characters)
```

**Output:**

```text
['h', 'e', 'l', 'l', 'o']
```

A tuple can also be converted to a list:

```python
numbers_tuple = (10, 20, 30)
numbers_list = list(numbers_tuple)

print(numbers_list)
```

**Output:**

```text
[10, 20, 30]
```

[Back to Index](#index)

---

<a id="mixed-and-nested-lists"></a>

### 3. Creating Mixed and Nested Lists

A Python list can contain values of different data types.

```python
mixed_values = ["world", 42, 3.14, False]

print(mixed_values)
```

**Output:**

```text
['world', 42, 3.14, False]
```

A list can also contain other lists.

```python
nested_list = [
    [1, 2, 3],
    ["apple", "banana"],
    [True, False],
]

print(nested_list)
```

**Output:**

```text
[[1, 2, 3], ['apple', 'banana'], [True, False]]
```

Although mixed-type lists are supported, lists containing related types are often easier to understand and process.

[Back to Index](#index)

---

<a id="positive-list-indexing"></a>

## Accessing Elements with Positive Indexes

Lists are ordered collections. Each element has an index representing its position.

Positive indexing starts at `0`.

For the following list:

```python
fruits = ["apple", "banana", "cherry"]
```

the indexes are:

```text
Element: apple  banana  cherry
Index:     0       1       2
```

### Syntax

```python
element = list_name[index]
```

### Example

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

**Output:**

```text
apple
banana
cherry
```

The expressions mean:

```text
fruits[0] → first element
fruits[1] → second element
fruits[2] → third element
```

[Back to Index](#index)

---

<a id="list-index-errors"></a>

### Index Errors

Accessing an index outside the valid range raises an `IndexError`.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[3])
```

**Error:**

```text
IndexError: list index out of range
```

The list contains three elements, so its valid positive indexes are:

```text
0, 1, 2
```

The maximum valid positive index can be calculated as:

```text
len(list_name) - 1
```

For example:

```python
fruits = ["apple", "banana", "cherry"]

last_index = len(fruits) - 1

print(last_index)
print(fruits[last_index])
```

**Output:**

```text
2
cherry
```

[Back to Index](#index)

---

<a id="negative-list-indexing"></a>

## Accessing Elements with Negative Indexes

Negative indexing accesses list elements from the end.

* `-1` represents the last element.
* `-2` represents the second-to-last element.
* `-3` represents the third-to-last element.

For the following list:

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
```

the indexes are:

```text
Element:         apple  banana  cherry  date  elderberry
Positive index:    0       1       2      3       4
Negative index:   -5      -4      -3     -2      -1
```

### Example

```python
fruits = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
]

last_fruit = fruits[-1]
second_last_fruit = fruits[-2]

print(last_fruit)
print(second_last_fruit)
```

**Output:**

```text
elderberry
date
```

Negative indexing is useful when the list length is unknown.

```python
numbers = [10, 20, 30, 40]

print(numbers[-1])
```

**Output:**

```text
40
```

[Back to Index](#index)

---

<a id="modifying-list-elements"></a>

## Modifying List Elements

Lists are **mutable**, meaning their elements can be changed after the list has been created.

### Syntax

```python
list_name[index] = new_value
```

The index must refer to an existing element.

<a id="modify-positive-index"></a>

### 1. Modifying with a Positive Index

```python
fruits = ["apple", "banana", "cherry"]

fruits[1] = "blueberry"

print(fruits)
```

**Output:**

```text
['apple', 'blueberry', 'cherry']
```

The value at index `1` changes from `"banana"` to `"blueberry"`.

```text
Before: ['apple', 'banana',    'cherry']
After:  ['apple', 'blueberry', 'cherry']
```

[Back to Index](#index)

---

<a id="modify-negative-index"></a>

### 2. Modifying with a Negative Index

```python
shopping_list = [
    "rice",
    "eggs",
    "vegetables",
    "juice",
]

shopping_list[-1] = "bread"

print(shopping_list)
```

**Output:**

```text
['rice', 'eggs', 'vegetables', 'bread']
```

The index `-1` refers to the final element.

### Invalid Modification Index

Trying to modify an index that does not exist raises an `IndexError`.

```python
fruits = ["apple", "banana"]

fruits[5] = "orange"
```

**Error:**

```text
IndexError: list assignment index out of range
```

Assigning to an index cannot be used to add a new element beyond the current list length. Use `append()` or `insert()` instead.

[Back to Index](#index)

---

<a id="append-method"></a>

## Adding Elements with `append()`

The `append()` method adds one element to the end of a list.

It modifies the original list in place.

### Syntax

```python
list_name.append(element)
```

### Example

```python
fruits = []

fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")

print(fruits)
```

**Output:**

```text
['apple', 'banana', 'cherry']
```

The list changes after each operation:

```text
[] 
↓ append("apple")
['apple']
↓ append("banana")
['apple', 'banana']
↓ append("cherry")
['apple', 'banana', 'cherry']
```

### `append()` Adds One Element

When a list is appended, the entire list becomes one nested element.

```python
numbers = [1, 2]
numbers.append([3, 4])

print(numbers)
```

**Output:**

```text
[1, 2, [3, 4]]
```

The list `[3, 4]` is added as a single element.

### Return Value

The `append()` method returns `None`.

```python
fruits = ["apple"]

result = fruits.append("banana")

print(fruits)
print(result)
```

**Output:**

```text
['apple', 'banana']
None
```

Do not assign the result of `append()` back to the list:

```python
fruits = ["apple"]

fruits = fruits.append("banana")

print(fruits)
```

**Output:**

```text
None
```

The method modifies the original list and returns `None`.

[Back to Index](#index)

---

<a id="insert-method"></a>

## Adding Elements with `insert()`

The `insert()` method adds one element at a specified index.

Existing elements at and after that position are shifted to the right.

### Syntax

```python
list_name.insert(index, element)
```

### Example

```python
numbers = [1, 2, 4, 5]

numbers.insert(2, 3)

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

The number `3` is inserted at index `2`.

```text
Before: [1, 2, 4, 5]
Index:   0  1  2  3

After:  [1, 2, 3, 4, 5]
Index:   0  1  2  3  4
```

### Inserting at the Beginning

```python
fruits = ["banana", "cherry"]

fruits.insert(0, "apple")

print(fruits)
```

**Output:**

```text
['apple', 'banana', 'cherry']
```

### Inserting Beyond the List Length

When the index is greater than the list length, the element is inserted at the end.

```python
numbers = [1, 2, 3]

numbers.insert(100, 4)

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4]
```

Like `append()`, `insert()` modifies the list and returns `None`.

[Back to Index](#index)

---

<a id="remove-method"></a>

## Removing Elements with `remove()`

The `remove()` method deletes the first occurrence of a specified value.

### Syntax

```python
list_name.remove(value)
```

### Example

```python
numbers = [1, 2, 3, 2, 4, 5]

numbers.remove(2)

print(numbers)
```

**Output:**

```text
[1, 3, 2, 4, 5]
```

Only the first occurrence of `2` is removed.

```text
Before: [1, 2, 3, 2, 4, 5]
After:  [1,    3, 2, 4, 5]
```

### Removing a Missing Value

If the value does not exist, `remove()` raises a `ValueError`.

```python
fruits = ["apple", "banana"]

fruits.remove("orange")
```

**Error:**

```text
ValueError: list.remove(x): x not in list
```

Check membership before removing a value:

```python
fruits = ["apple", "banana"]

if "orange" in fruits:
    fruits.remove("orange")
else:
    print("The value was not found.")
```

**Output:**

```text
The value was not found.
```

The `remove()` method modifies the list and returns `None`.

[Back to Index](#index)

---

<a id="pop-method"></a>

## Removing Elements with `pop()`

The `pop()` method removes an element and returns the removed value.

It can remove:

* The final element
* An element at a specified index

### Syntax

```python
removed_value = list_name.pop()
removed_value = list_name.pop(index)
```

<a id="pop-last-element"></a>

### 1. Removing the Last Element

When no index is provided, `pop()` removes the last element.

```python
fruits = ["apple", "banana", "cherry"]

removed_fruit = fruits.pop()

print("Removed fruit:", removed_fruit)
print("Updated list:", fruits)
```

**Output:**

```text
Removed fruit: cherry
Updated list: ['apple', 'banana']
```

The index `-1` is used implicitly.

[Back to Index](#index)

---

<a id="pop-specific-index"></a>

### 2. Removing an Element at a Specific Index

```python
fruits = ["apple", "banana", "cherry", "date"]

removed_fruit = fruits.pop(2)

print("Removed fruit:", removed_fruit)
print("Updated list:", fruits)
```

**Output:**

```text
Removed fruit: cherry
Updated list: ['apple', 'banana', 'date']
```

The element at index `2` is removed and returned.

### Using a Negative Index

```python
numbers = [10, 20, 30, 40]

removed_number = numbers.pop(-2)

print(removed_number)
print(numbers)
```

**Output:**

```text
30
[10, 20, 40]
```

### Popping from an Empty List

```python
items = []

items.pop()
```

**Error:**

```text
IndexError: pop from empty list
```

An invalid index also raises an `IndexError`.

```python
items = ["a", "b"]

items.pop(5)
```

**Error:**

```text
IndexError: pop index out of range
```

[Back to Index](#index)

---

<a id="checking-list-length"></a>

## Checking List Length

The built-in `len()` function returns the number of elements in a list.

### Syntax

```python
length = len(list_name)
```

### Example

```python
fruits = ["apple", "banana", "cherry", "date"]

number_of_fruits = len(fruits)

print("Number of fruits:", number_of_fruits)
```

**Output:**

```text
Number of fruits: 4
```

The result of `len()` is an integer.

```python
fruits = ["apple", "banana", "cherry"]

length = len(fruits)

print(type(length))
```

**Output:**

```text
<class 'int'>
```

### Empty List Length

```python
items = []

print(len(items))
```

**Output:**

```text
0
```

### Length Counts Top-Level Elements

A nested list counts as one element.

```python
items = [1, 2, [3, 4, 5]]

print(len(items))
```

**Output:**

```text
3
```

The top-level elements are:

```text
1
2
[3, 4, 5]
```

[Back to Index](#index)

---

<a id="list-length-loops"></a>

## Using List Length in Loops

The length of a list can be used to control a loop.

### Printing List Indexes with a `while` Loop

```python
numbers = [10, 20, 30, 40, 50]

index = 0

while index < len(numbers):
    print(index)
    index += 1
```

**Output:**

```text
0
1
2
3
4
```

These are the indexes, not the list elements.

### Printing the Elements

Use each index to access its corresponding value:

```python
numbers = [10, 20, 30, 40, 50]

index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
```

**Output:**

```text
10
20
30
40
50
```

### Printing Indexes and Elements

```python
numbers = [10, 20, 30, 40, 50]

index = 0

while index < len(numbers):
    print(f"Index {index}: {numbers[index]}")
    index += 1
```

**Output:**

```text
Index 0: 10
Index 1: 20
Index 2: 30
Index 3: 40
Index 4: 50
```

### Using a `for` Loop

A `for` loop is often simpler when only the elements are needed:

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

**Output:**

```text
10
20
30
40
50
```

Use `enumerate()` when both indexes and values are needed:

```python
numbers = [10, 20, 30, 40, 50]

for index, number in enumerate(numbers):
    print(f"Index {index}: {number}")
```

**Output:**

```text
Index 0: 10
Index 1: 20
Index 2: 30
Index 3: 40
Index 4: 50
```

[Back to Index](#index)

---

<a id="list-method-summary"></a>

## List Method Summary

| Operation            | Syntax                       | Purpose                               |
| -------------------- | ---------------------------- | ------------------------------------- |
| Create an empty list | `items = []`                 | Creates an empty list                 |
| Convert an iterable  | `list(iterable)`             | Creates a list from an iterable       |
| Access an element    | `items[index]`               | Retrieves an element                  |
| Modify an element    | `items[index] = value`       | Replaces an existing element          |
| Add to the end       | `items.append(value)`        | Adds one element at the end           |
| Insert at an index   | `items.insert(index, value)` | Adds one element at a position        |
| Remove by value      | `items.remove(value)`        | Removes the first matching value      |
| Remove by index      | `items.pop(index)`           | Removes and returns an element        |
| Remove the last item | `items.pop()`                | Removes and returns the final element |
| Check length         | `len(items)`                 | Returns the number of elements        |

### Combined Example

```python
fruits = ["apple", "banana"]

fruits.append("cherry")
fruits.insert(1, "orange")
fruits[0] = "mango"

removed_fruit = fruits.pop()
fruits.remove("banana")

print("Removed:", removed_fruit)
print("Final list:", fruits)
print("Length:", len(fruits))
```

**Output:**

```text
Removed: cherry
Final list: ['mango', 'orange']
Length: 2
```

The list changes as follows:

```text
Initial:
['apple', 'banana']

After append("cherry"):
['apple', 'banana', 'cherry']

After insert(1, "orange"):
['apple', 'orange', 'banana', 'cherry']

After fruits[0] = "mango":
['mango', 'orange', 'banana', 'cherry']

After pop():
['mango', 'orange', 'banana']

After remove("banana"):
['mango', 'orange']
```

[Back to Index](#index)