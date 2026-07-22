<a id="list-methods-and-comprehensions-in-python"></a>

## List Methods and Comprehensions in Python

Python lists provide methods for adding, searching, sorting, reversing, copying, and removing elements.

Python also supports **list comprehensions**, which provide a concise way to create new lists from existing iterables.

<a id="index"></a>

## Index

1. [Extending a List with `extend()`](#list-extend)

   * [`extend()` with Different Iterables](#extend-different-iterables)
   * [`append()` Versus `extend()`](#append-versus-extend)
2. [List Concatenation](#list-concatenation)

   * [`+` Versus `extend()`](#concatenation-versus-extend)
3. [Counting Elements with `count()`](#list-count)
4. [Finding an Element with `index()`](#list-index)

   * [Searching Within a Range](#index-search-range)
   * [Handling Missing Values](#index-missing-values)
5. [Sorting Lists with `sort()`](#list-sort)

   * [Descending Order](#sort-descending)
   * [Sorting with `key`](#sort-with-key)
   * [Sorting Limitations](#sort-limitations)
   * [`sort()` Versus `sorted()`](#sort-versus-sorted)
6. [Reversing Lists with `reverse()`](#list-reverse)
7. [Copying Lists with `copy()`](#list-copy)

   * [Shallow-Copy Behavior](#shallow-copy-behavior)
8. [Clearing Lists with `clear()`](#list-clear)

   * [`clear()` Versus Reassignment](#clear-versus-reassignment)
9. [Basic List Comprehensions](#basic-list-comprehension)
10. [List Comprehensions with Conditions](#list-comprehension-condition)
11. [Conditional Expressions in Comprehensions](#conditional-expression-comprehension)
12. [List Method Summary](#list-method-summary)

---

<a id="list-extend"></a>

## Extending a List with `extend()`

The `extend()` method adds every element from an iterable to the end of an existing list.

It modifies the original list in place.

### Syntax

```python
list_name.extend(iterable)
```

An iterable can be a:

* List
* Tuple
* String
* Set
* Range
* Dictionary
* Generator
* Other iterable object

### Basic Example

```python
original_list = [1, 2, 3]
new_elements = [4, 5, 6]

original_list.extend(new_elements)

print(original_list)
```

**Output:**

```text
[1, 2, 3, 4, 5, 6]
```

The list changes as follows:

```text
[1, 2, 3]
     ↓ extend([4, 5, 6])
[1, 2, 3, 4, 5, 6]
```

### Return Value

The `extend()` method modifies the list and returns `None`.

```python
numbers = [1, 2, 3]

result = numbers.extend([4, 5])

print(numbers)
print(result)
```

**Output:**

```text
[1, 2, 3, 4, 5]
None
```

Do not assign the result of `extend()` back to the list:

```python
numbers = [1, 2, 3]

numbers = numbers.extend([4, 5])

print(numbers)
```

**Output:**

```text
None
```

[Back to Index](#index)

---

<a id="extend-different-iterables"></a>

### `extend()` with Different Iterables

Because `extend()` accepts any iterable, it can add elements from several data types.

### Extending with a Tuple

```python
numbers = [1, 2]

numbers.extend((3, 4))

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4]
```

### Extending with a String

A string is an iterable of characters. Therefore, each character is added separately.

```python
letters = ["A", "B"]

letters.extend("CD")

print(letters)
```

**Output:**

```text
['A', 'B', 'C', 'D']
```

To add the entire string as one element, use `append()`:

```python
letters = ["A", "B"]

letters.append("CD")

print(letters)
```

**Output:**

```text
['A', 'B', 'CD']
```

### Extending with a Range

```python
numbers = [1, 2]

numbers.extend(range(3, 7))

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4, 5, 6]
```

### Extending with a Set

```python
numbers = [1, 2]

numbers.extend({3, 4, 5})

print(numbers)
```

The values are added, but the order should not be relied upon because sets are unordered collections.

### Extending with a Dictionary

Iterating over a dictionary produces its keys.

```python
items = ["start"]
data = {"name": "Alice", "age": 25}

items.extend(data)

print(items)
```

**Output:**

```text
['start', 'name', 'age']
```

To add the dictionary's values instead:

```python
items = ["start"]
data = {"name": "Alice", "age": 25}

items.extend(data.values())

print(items)
```

**Output:**

```text
['start', 'Alice', 25]
```

[Back to Index](#index)

---

<a id="append-versus-extend"></a>

### `append()` Versus `extend()`

The `append()` method adds one object.

The `extend()` method adds every element from an iterable.

```python
numbers1 = [1, 2]
numbers1.append([3, 4])

numbers2 = [1, 2]
numbers2.extend([3, 4])

print(numbers1)
print(numbers2)
```

**Output:**

```text
[1, 2, [3, 4]]
[1, 2, 3, 4]
```

| Method           | Operation                         | Result           |
| ---------------- | --------------------------------- | ---------------- |
| `append([3, 4])` | Adds the list as one element      | `[1, 2, [3, 4]]` |
| `extend([3, 4])` | Adds each list element separately | `[1, 2, 3, 4]`   |

[Back to Index](#index)

---

<a id="list-concatenation"></a>

## List Concatenation

The `+` operator combines two lists and creates a new list.

It does not modify either original list.

### Example

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2

print("First list:", list1)
print("Second list:", list2)
print("Combined list:", combined_list)
```

**Output:**

```text
First list: [1, 2, 3]
Second list: [4, 5, 6]
Combined list: [1, 2, 3, 4, 5, 6]
```

The identity of the new list is different from both original lists:

```python
print(combined_list is list1)
print(combined_list is list2)
```

**Output:**

```text
False
False
```

### Concatenation Requires Lists

Both operands of list concatenation must be lists.

```python
numbers = [1, 2, 3]

result = numbers + (4, 5)
```

**Error:**

```text
TypeError: can only concatenate list (not "tuple") to list
```

Convert the tuple to a list first:

```python
numbers = [1, 2, 3]

result = numbers + list((4, 5))

print(result)
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

[Back to Index](#index)

---

<a id="concatenation-versus-extend"></a>

### `+` Versus `extend()`

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
```

Using concatenation:

```python
combined = list1 + list2
```

* Creates a new list
* Leaves `list1` unchanged
* Requires another list as the right operand

Using `extend()`:

```python
list1.extend(list2)
```

* Modifies `list1`
* Does not create a separate combined list
* Accepts any iterable

| Feature                    | `list1 + list2` | `list1.extend(iterable)` |
| -------------------------- | --------------- | ------------------------ |
| Modifies the original list | No              | Yes                      |
| Creates a new list         | Yes             | No                       |
| Accepts any iterable       | No              | Yes                      |
| Return value               | New list        | `None`                   |

### Using `+=`

The `+=` operator extends a list in place.

```python
numbers = [1, 2, 3]

numbers += [4, 5]

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

For lists, `+=` behaves similarly to `extend()`.

```python
numbers = [1, 2]

numbers += (3, 4)

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4]
```

Unlike list concatenation with `+`, list `+=` can accept another iterable.

[Back to Index](#index)

---

<a id="list-count"></a>

## Counting Elements with `count()`

The `count()` method returns the number of times a value occurs in a list.

It does not modify the list.

### Syntax

```python
list_name.count(value)
```

### Example

```python
fruits = [
    "apple",
    "banana",
    "cherry",
    "apple",
    "cherry",
]

apple_count = fruits.count("apple")

print("Apple count:", apple_count)
```

**Output:**

```text
Apple count: 2
```

### Missing Value

When the value is absent, `count()` returns `0`.

```python
numbers = [1, 2, 3, 4]

print(numbers.count(10))
```

**Output:**

```text
0
```

It does not raise an error for a missing value.

### Counting Is Case-Sensitive

```python
words = ["Python", "python", "PYTHON", "Python"]

print(words.count("Python"))
```

**Output:**

```text
2
```

Only exact matches are counted.

### Counting Nested Lists

```python
items = [[1, 2], [3, 4], [1, 2]]

print(items.count([1, 2]))
```

**Output:**

```text
2
```

The method compares list elements using equality.

[Back to Index](#index)

---

<a id="list-index"></a>

## Finding an Element with `index()`

The `index()` method searches for a value and returns the index of its first occurrence.

### Syntax

```python
list_name.index(value)
list_name.index(value, start)
list_name.index(value, start, stop)
```

The parameters are:

* `value`: value to locate
* `start`: optional starting index
* `stop`: optional ending index, excluded

### Basic Example

```python
fruits = ["apple", "banana", "cherry", "apple"]

apple_index = fruits.index("apple")

print(apple_index)
```

**Output:**

```text
0
```

Although `"apple"` appears twice, `index()` returns only the first matching index.

### Finding Another Occurrence

```python
fruits = ["apple", "banana", "cherry", "apple"]

second_apple = fruits.index("apple", 1)

print(second_apple)
```

**Output:**

```text
3
```

The search begins at index `1`, so the occurrence at index `0` is ignored.

[Back to Index](#index)

---

<a id="index-search-range"></a>

### Searching Within a Range

The `start` index is included, while the `stop` index is excluded.

```python
letters = ["a", "b", "c", "b", "d", "b"]

result = letters.index("b", 2, 5)

print(result)
```

**Output:**

```text
3
```

The search examines indexes:

```text
2, 3, 4
```

Index `5` is excluded.

### Negative Search Indexes

Negative indexes can also be used:

```python
numbers = [10, 20, 30, 20, 40]

result = numbers.index(20, -3)

print(result)
```

**Output:**

```text
3
```

The search begins three positions from the end.

[Back to Index](#index)

---

<a id="index-missing-values"></a>

### Handling Missing Values

When a value is not found, `index()` raises a `ValueError`.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits.index("orange"))
```

**Error:**

```text
ValueError: 'orange' is not in list
```

Check membership before calling `index()`:

```python
fruits = ["apple", "banana", "cherry"]
target = "orange"

if target in fruits:
    print(fruits.index(target))
else:
    print("The value was not found.")
```

**Output:**

```text
The value was not found.
```

Alternatively, use exception handling:

```python
fruits = ["apple", "banana", "cherry"]

try:
    position = fruits.index("orange")
    print(position)
except ValueError:
    print("The value was not found.")
```

**Output:**

```text
The value was not found.
```

[Back to Index](#index)

---

<a id="list-sort"></a>

## Sorting Lists with `sort()`

The `sort()` method rearranges a list's elements in place.

By default, it sorts values in ascending order.

### Syntax

```python
list_name.sort(key=None, reverse=False)
```

The optional parameters are:

* `key`: function used to generate a comparison key
* `reverse`: when `True`, sorts in descending order

### Sorting Numbers

```python
numbers = [5, 1, 8, 3, 2]

numbers.sort()

print(numbers)
```

**Output:**

```text
[1, 2, 3, 5, 8]
```

### Sorting Strings

```python
fruits = ["cherry", "apple", "banana"]

fruits.sort()

print(fruits)
```

**Output:**

```text
['apple', 'banana', 'cherry']
```

String sorting is based on lexicographical ordering and is case-sensitive.

### Return Value

The `sort()` method returns `None`.

```python
numbers = [3, 1, 2]

result = numbers.sort()

print(numbers)
print(result)
```

**Output:**

```text
[1, 2, 3]
None
```

Do not assign the result back to the list:

```python
numbers = [3, 1, 2]

numbers = numbers.sort()

print(numbers)
```

**Output:**

```text
None
```

[Back to Index](#index)

---

<a id="sort-descending"></a>

### Sorting in Descending Order

Set `reverse=True` to sort from largest to smallest.

```python
numbers = [5, 1, 8, 3, 2]

numbers.sort(reverse=True)

print(numbers)
```

**Output:**

```text
[8, 5, 3, 2, 1]
```

Strings can also be sorted in reverse order:

```python
fruits = ["cherry", "apple", "banana"]

fruits.sort(reverse=True)

print(fruits)
```

**Output:**

```text
['cherry', 'banana', 'apple']
```

[Back to Index](#index)

---

<a id="sort-with-key"></a>

### Sorting with `key`

The `key` parameter accepts a function that produces the value used for comparison.

### Case-Insensitive Sorting

```python
words = ["banana", "Apple", "cherry", "apricot"]

words.sort(key=str.lower)

print(words)
```

**Output:**

```text
['Apple', 'apricot', 'banana', 'cherry']
```

The original strings are not converted to lowercase. Lowercase versions are used only as comparison keys.

### Sorting by Length

```python
words = ["elephant", "cat", "giraffe", "dog"]

words.sort(key=len)

print(words)
```

**Output:**

```text
['cat', 'dog', 'giraffe', 'elephant']
```

### Sorting a List of Dictionaries

```python
students = [
    {"name": "Alice", "score": 82},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 75},
]

students.sort(key=lambda student: student["score"])

print(students)
```

**Output:**

```text
[{'name': 'Charlie', 'score': 75}, {'name': 'Alice', 'score': 82}, {'name': 'Bob', 'score': 95}]
```

The `lambda` function returns each student's score as the sorting key.

### Stable Sorting

Python's sorting algorithm is stable.

When two elements have the same key, their original relative order is preserved.

```python
students = [
    ("Alice", 90),
    ("Bob", 80),
    ("Charlie", 90),
]

students.sort(key=lambda student: student[1])

print(students)
```

**Output:**

```text
[('Bob', 80), ('Alice', 90), ('Charlie', 90)]
```

`"Alice"` remains before `"Charlie"` because both have the same score.

[Back to Index](#index)

---

<a id="sort-limitations"></a>

### Sorting Limitations

Elements must be mutually comparable according to the selected key.

A list containing unrelated types may not be sortable:

```python
values = [10, "apple", 3.5]

values.sort()
```

**Error:**

```text
TypeError: '<' not supported between instances of 'str' and 'int'
```

Python cannot determine a natural ordering between strings and numbers.

A key function can sometimes provide a common comparison type:

```python
values = [10, "apple", 3.5]

values.sort(key=str)

print(values)
```

**Output:**

```text
[10, 3.5, 'apple']
```

The values are ordered according to their string representations.

> Using `key=str` produces textual ordering, not numerical ordering.

[Back to Index](#index)

---

<a id="sort-versus-sorted"></a>

### `sort()` Versus `sorted()`

The `sort()` method:

* Works only on lists
* Modifies the original list
* Returns `None`

The built-in `sorted()` function:

* Accepts any iterable
* Returns a new list
* Leaves the original object unchanged

```python
numbers = [5, 1, 8, 3, 2]

sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
```

**Output:**

```text
Original: [5, 1, 8, 3, 2]
Sorted: [1, 2, 3, 5, 8]
```

| Feature                    | `list.sort()` | `sorted(iterable)` |
| -------------------------- | ------------- | ------------------ |
| Modifies original          | Yes           | No                 |
| Returns a list             | No            | Yes                |
| Accepts non-list iterables | No            | Yes                |
| Supports `key`             | Yes           | Yes                |
| Supports `reverse`         | Yes           | Yes                |

[Back to Index](#index)

---

<a id="list-reverse"></a>

## Reversing Lists with `reverse()`

The `reverse()` method reverses the current order of a list in place.

It does not sort the values.

### Syntax

```python
list_name.reverse()
```

### Reversing Strings in a List

```python
fruits = ["apple", "banana", "cherry", "date"]

fruits.reverse()

print(fruits)
```

**Output:**

```text
['date', 'cherry', 'banana', 'apple']
```

### Reversing Mixed Data Types

```python
mixed_values = [1, "apple", 2.5, True]

mixed_values.reverse()

print(mixed_values)
```

**Output:**

```text
[True, 2.5, 'apple', 1]
```

The method does not compare the values, so mixed data types can be reversed safely.

### Return Value

The `reverse()` method returns `None`.

```python
numbers = [1, 2, 3]

result = numbers.reverse()

print(numbers)
print(result)
```

**Output:**

```text
[3, 2, 1]
None
```

### `reverse()` Versus Slicing

```python
numbers = [1, 2, 3, 4]
```

Using `reverse()`:

```python
numbers.reverse()
```

* Modifies the original list
* Returns `None`

Using slicing:

```python
reversed_numbers = numbers[::-1]
```

* Creates a new list
* Leaves the original list unchanged

Using `reversed()`:

```python
reversed_iterator = reversed(numbers)
reversed_numbers = list(reversed_iterator)
```

* Returns an iterator
* Does not modify the original list

[Back to Index](#index)

---

<a id="list-copy"></a>

## Copying Lists with `copy()`

The `copy()` method creates a shallow copy of a list.

The copied list:

* Contains the same elements
* Is a separate outer list object
* Can be modified independently at the top level

### Syntax

```python
copied_list = original_list.copy()
```

### Basic Example

```python
original_list = [10, 20, 30]
copied_list = original_list.copy()

print("Original list:", original_list)
print("Copied list:", copied_list)
```

**Output:**

```text
Original list: [10, 20, 30]
Copied list: [10, 20, 30]
```

### Comparing Identity and Equality

```python
original_list = [10, 20, 30]
copied_list = original_list.copy()

print(original_list == copied_list)
print(original_list is copied_list)
```

**Output:**

```text
True
False
```

The lists contain equal values but are different objects.

### Modifying the Copied List

```python
numbers = [10, 20, 30]
numbers_copy = numbers.copy()

numbers_copy.append(40)

print("Original list:", numbers)
print("Copied list:", numbers_copy)
```

**Output:**

```text
Original list: [10, 20, 30]
Copied list: [10, 20, 30, 40]
```

Appending to the copied outer list does not affect the original list.

Other common shallow-copy techniques include:

```python
copy1 = original_list[:]
copy2 = list(original_list)
```

[Back to Index](#index)

---

<a id="shallow-copy-behavior"></a>

### Shallow-Copy Behavior

A shallow copy creates a new outer list but does not recursively copy nested mutable objects.

```python
original = [[1, 2], [3, 4]]
copied = original.copy()

copied[0].append(99)

print("Original:", original)
print("Copied:", copied)
```

**Output:**

```text
Original: [[1, 2, 99], [3, 4]]
Copied: [[1, 2, 99], [3, 4]]
```

Both outer lists refer to the same nested lists.

```python
print(original is copied)
print(original[0] is copied[0])
```

**Output:**

```text
False
True
```

To recursively copy nested objects, use `deepcopy()` from the `copy` module:

```python
from copy import deepcopy

original = [[1, 2], [3, 4]]
copied = deepcopy(original)

copied[0].append(99)

print("Original:", original)
print("Copied:", copied)
```

**Output:**

```text
Original: [[1, 2], [3, 4]]
Copied: [[1, 2, 99], [3, 4]]
```

[Back to Index](#index)

---

<a id="list-clear"></a>

## Clearing Lists with `clear()`

The `clear()` method removes every element from a list.

It modifies the existing list object and returns `None`.

### Syntax

```python
list_name.clear()
```

### Basic Example

```python
fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)
```

**Output:**

```text
[]
```

### Clearing and Reusing a List

```python
numbers = [1, 2, 3, 4, 5]

numbers.clear()

numbers.append(10)
numbers.append(20)

print(numbers)
```

**Output:**

```text
[10, 20]
```

### Return Value

```python
numbers = [1, 2, 3]

result = numbers.clear()

print(numbers)
print(result)
```

**Output:**

```text
[]
None
```

The following operations also clear a list in place:

```python
numbers[:] = []
```

```python
del numbers[:]
```

[Back to Index](#index)

---

<a id="clear-versus-reassignment"></a>

### `clear()` Versus Reassignment

Clearing a list and assigning a new empty list are not always equivalent.

### Using `clear()`

```python
list1 = [1, 2, 3]
list2 = list1

list1.clear()

print(list1)
print(list2)
```

**Output:**

```text
[]
[]
```

Both variables refer to the same list object, so both observe the change.

### Using Reassignment

```python
list1 = [1, 2, 3]
list2 = list1

list1 = []

print(list1)
print(list2)
```

**Output:**

```text
[]
[1, 2, 3]
```

Reassignment makes `list1` refer to a new empty list. It does not modify the original list referenced by `list2`.

### Identity Example

```python
numbers = [1, 2, 3]
original_id = id(numbers)

numbers.clear()

print(id(numbers) == original_id)
```

**Output:**

```text
True
```

The existing list object is retained.

> `clear()` is useful when other parts of a program hold references to the same list and should observe that it has been emptied.

[Back to Index](#index)

---

<a id="basic-list-comprehension"></a>

## Basic List Comprehensions

A list comprehension creates a new list by evaluating an expression for every item in an iterable.

### Syntax

```python
new_list = [expression for item in iterable]
```

The components are:

* `expression`: value placed in the new list
* `item`: variable representing the current element
* `iterable`: object being processed

### Creating Squares

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

The equivalent traditional loop is:

```python
numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
```

### Creating a Character List

```python
word = "Python"

characters = [character for character in word]

print(characters)
```

**Output:**

```text
['P', 'y', 't', 'h', 'o', 'n']
```

For this particular task, the built-in `list()` constructor is simpler:

```python
characters = list(word)
```

### Converting Words to Uppercase

```python
words = ["python", "java", "go"]

uppercase_words = [word.upper() for word in words]

print(uppercase_words)
```

**Output:**

```text
['PYTHON', 'JAVA', 'GO']
```

### Using `range()`

```python
numbers = [number for number in range(1, 6)]

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

List comprehensions are often concise and readable for simple transformations. A normal loop is usually clearer when the logic contains several statements or complex side effects.

[Back to Index](#index)

---

<a id="list-comprehension-condition"></a>

## List Comprehensions with Conditions

A condition placed after the iterable filters which items are included.

### Syntax

```python
new_list = [
    expression
    for item in iterable
    if condition
]
```

Only items for which the condition is true are included.

### Filtering Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

**Output:**

```text
[2, 4, 6]
```

The equivalent loop is:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
```

### Filtering and Transforming

The expression can transform the values that pass the filter.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print(even_squares)
```

**Output:**

```text
[4, 16, 36]
```

### Extracting Long Words

```python
words = [
    "apple",
    "banana",
    "cherry",
    "kiwi",
    "mango",
]

long_words = [
    word
    for word in words
    if len(word) > 5
]

print(long_words)
```

**Output:**

```text
['banana', 'cherry']
```

### Filtering Non-Empty Strings

```python
values = ["Python", "", "Java", "", "Go"]

non_empty_values = [
    value
    for value in values
    if value
]

print(non_empty_values)
```

**Output:**

```text
['Python', 'Java', 'Go']
```

### Multiple Conditions

```python
numbers = range(1, 21)

results = [
    number
    for number in numbers
    if number % 2 == 0 and number > 10
]

print(results)
```

**Output:**

```text
[12, 14, 16, 18, 20]
```

[Back to Index](#index)

---

<a id="conditional-expression-comprehension"></a>

## Conditional Expressions in Comprehensions

A conditional expression transforms every item into one of two possible values.

### Syntax

```python
new_list = [
    value_if_true if condition else value_if_false
    for item in iterable
]
```

This differs from a filtering condition.

### Labeling Numbers as Even or Odd

```python
numbers = [1, 2, 3, 4, 5]

labels = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(labels)
```

**Output:**

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

Every input number produces one output element.

### Replacing Negative Values

```python
numbers = [5, -2, 8, -1, 0]

normalized = [
    number if number >= 0 else 0
    for number in numbers
]

print(normalized)
```

**Output:**

```text
[5, 0, 8, 0, 0]
```

### Filtering Versus Conditional Transformation

Filtering syntax:

```python
[number for number in numbers if number > 0]
```

* Excludes values that fail the condition
* May create a shorter list

Conditional-expression syntax:

```python
[number if number > 0 else 0 for number in numbers]
```

* Processes every value
* Produces one output for every input

### Combining Transformation and Filtering

```python
numbers = [-3, -2, -1, 0, 1, 2, 3]

results = [
    number ** 2
    for number in numbers
    if number > 0
]

print(results)
```

**Output:**

```text
[1, 4, 9]
```

The filter runs first conceptually, and the expression is applied only to retained values.

[Back to Index](#index)

---

<a id="list-method-summary"></a>

## List Method Summary

| Operation               | Syntax                                     | Modifies original? | Return value     |
| ----------------------- | ------------------------------------------ | -----------------: | ---------------- |
| Extend with iterable    | `items.extend(iterable)`                   |                Yes | `None`           |
| Concatenate lists       | `list1 + list2`                            |                 No | New list         |
| Count occurrences       | `items.count(value)`                       |                 No | Integer          |
| Find first index        | `items.index(value)`                       |                 No | Integer          |
| Sort list               | `items.sort()`                             |                Yes | `None`           |
| Reverse list            | `items.reverse()`                          |                Yes | `None`           |
| Copy list               | `items.copy()`                             |                 No | New shallow list |
| Clear list              | `items.clear()`                            |                Yes | `None`           |
| Create transformed list | `[expression for item in iterable]`        |                 No | New list         |
| Filter values           | `[item for item in iterable if condition]` |                 No | New list         |

### Combined Example

```python
numbers = [5, 2, 8, 2, 1]

numbers.extend([10, 4])

print("Extended:", numbers)
print("Count of 2:", numbers.count(2))
print("First index of 2:", numbers.index(2))

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

numbers_copy = numbers.copy()
numbers_copy.clear()

print("Original:", numbers)
print("Cleared copy:", numbers_copy)

even_squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print("Even squares:", even_squares)
```

**Output:**

```text
Extended: [5, 2, 8, 2, 1, 10, 4]
Count of 2: 2
First index of 2: 1
Sorted: [1, 2, 2, 4, 5, 8, 10]
Reversed: [10, 8, 5, 4, 2, 2, 1]
Original: [10, 8, 5, 4, 2, 2, 1]
Cleared copy: []
Even squares: [100, 64, 16, 4, 4]
```

[Back to Index](#index)