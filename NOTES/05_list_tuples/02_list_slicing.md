<a id="slicing-in-python"></a>

## Slicing in Python

Slicing extracts a portion of a sequence using index positions.

It works with sequence types such as:

* Lists
* Strings
* Tuples
* Ranges

The general slicing syntax is:

```python
sequence[start:stop:step]
```

The parameters mean:

* `start`: index where the slice begins
* `stop`: index where the slice ends, not included
* `step`: interval between selected elements

All three parameters are optional.

<a id="index"></a>

## Index

1. [Basic Slicing](#basic-slicing)
2. [How Slice Boundaries Work](#slice-boundaries)
3. [Slicing from the Beginning](#slicing-from-beginning)
4. [Slicing to the End](#slicing-to-end)
5. [Copying a Sequence with Slicing](#copying-with-slicing)
6. [Negative-Index Slicing](#negative-index-slicing)
7. [Positive-Step Slicing](#positive-step-slicing)
8. [Negative-Step Slicing](#negative-step-slicing)
9. [Reversing a Sequence](#reversing-a-sequence)
10. [Slice Assignment](#slice-assignment)

    * [Replacing Elements](#replacing-with-slice-assignment)
    * [Inserting Elements](#inserting-with-slice-assignment)
    * [Changing Slice Length](#changing-slice-length)
    * [Extended Slice Assignment](#extended-slice-assignment)
11. [Slice Deletion](#slice-deletion)
12. [Slicing Strings and Tuples](#slicing-immutable-sequences)
13. [Common Slicing Errors](#common-slicing-errors)
14. [Slicing Summary](#slicing-summary)

---

<a id="basic-slicing"></a>

## Basic Slicing

Basic slicing uses the following structure:

```python
sequence[start:stop]
```

The element at `start` is included, while the element at `stop` is excluded.

### Example

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[1:4]

print(result)
```

**Output:**

```text
[20, 30, 40]
```

The selected indexes are:

```text
Index:    0   1   2   3   4
Value:   10  20  30  40  50
              └───────┘

numbers[1:4] → indexes 1, 2, and 3
```

Index `4` is excluded.

### Slicing Does Not Modify the Original List

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[1:4]

print("Original:", numbers)
print("Slice:", result)
```

**Output:**

```text
Original: [10, 20, 30, 40, 50]
Slice: [20, 30, 40]
```

A normal list slice creates a new list containing references to the selected elements.

[Back to Index](#index)

---

<a id="slice-boundaries"></a>

## How Slice Boundaries Work

Unlike direct indexing, slicing does not normally raise an `IndexError` when its boundaries exceed the sequence length.

Python adjusts out-of-range slice boundaries automatically.

```python
numbers = [10, 20, 30]

print(numbers[0:100])
print(numbers[50:100])
```

**Output:**

```text
[10, 20, 30]
[]
```

The stop index `100` is beyond the list length, so Python stops at the actual end.

The second slice begins beyond the end of the list, so it produces an empty list.

### Empty Slice

A forward slice is empty when the start position is at or beyond the stop position.

```python
numbers = [10, 20, 30, 40]

print(numbers[3:1])
print(numbers[2:2])
```

**Output:**

```text
[]
[]
```

A positive step moves from left to right. Therefore, it cannot move from index `3` toward index `1`.

[Back to Index](#index)

---

<a id="slicing-from-beginning"></a>

## Slicing from the Beginning

Omit the `start` value to begin slicing from the start of the sequence.

### Syntax

```python
sequence[:stop]
```

For a positive step, the omitted start value defaults to the beginning of the sequence.

### Example

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[:3]

print(result)
```

**Output:**

```text
[10, 20, 30]
```

This is equivalent to:

```python
result = numbers[0:3]
```

### String Example

```python
text = "Python"

print(text[:3])
```

**Output:**

```text
Pyt
```

The selected indexes are `0`, `1`, and `2`.

[Back to Index](#index)

---

<a id="slicing-to-end"></a>

## Slicing to the End

Omit the `stop` value to continue slicing through the end of the sequence.

### Syntax

```python
sequence[start:]
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

print(fruits[1:])
```

**Output:**

```text
['banana', 'cherry', 'date', 'elderberry']
```

The slice starts at index `1` and includes every remaining element.

### Starting from the Last Two Elements

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[-2:])
```

**Output:**

```text
[40, 50]
```

[Back to Index](#index)

---

<a id="copying-with-slicing"></a>

## Copying a Sequence with Slicing

Omitting both `start` and `stop` selects the entire sequence.

```python
sequence[:]
```

For a list, this creates a shallow copy.

```python
original = [10, 20, 30]
copied = original[:]

print(original)
print(copied)
print(original is copied)
print(original == copied)
```

**Output:**

```text
[10, 20, 30]
[10, 20, 30]
False
True
```

The lists contain equal values but are separate list objects.

### Shallow-Copy Behavior

A shallow copy does not recursively copy nested objects.

```python
original = [[1, 2], [3, 4]]
copied = original[:]

copied[0].append(99)

print(original)
print(copied)
```

**Output:**

```text
[[1, 2, 99], [3, 4]]
[[1, 2, 99], [3, 4]]
```

The outer lists are different objects, but their nested lists are shared.

[Back to Index](#index)

---

<a id="negative-index-slicing"></a>

## Negative-Index Slicing

Negative indexes count backward from the end of a sequence.

* `-1` refers to the last element.
* `-2` refers to the second-to-last element.
* `-3` refers to the third-to-last element.

For this list:

```python
numbers = [5, 10, 15, 20, 25, 30]
```

the indexes are:

```text
Value:           5   10   15   20   25   30
Positive index:  0    1    2    3    4    5
Negative index: -6   -5   -4   -3   -2   -1
```

### Extracting the Last Three Elements

```python
numbers = [5, 10, 15, 20, 25, 30]

subset = numbers[-3:]

print(subset)
```

**Output:**

```text
[20, 25, 30]
```

The slice starts at index `-3` and continues to the end.

### Slicing a String

```python
text = "Python Programming"

result = text[-11:]

print(result)
```

**Output:**

```text
Programming
```

### Extracting a Partial Range

```python
colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
]

result = colors[-4:-1]

print(result)
```

**Output:**

```text
['blue', 'green', 'yellow']
```

The slice begins at `-4`, which refers to `"blue"`, and stops before `-1`, which refers to `"purple"`.

[Back to Index](#index)

---

<a id="positive-step-slicing"></a>

## Positive-Step Slicing

The `step` parameter controls the interval between selected elements.

### Syntax

```python
sequence[start:stop:step]
```

A positive step moves from left to right.

### Every Second Element

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])
```

**Output:**

```text
[10, 30, 50]
```

The selected indexes are:

```text
0, 2, 4
```

### Specific Range with a Step

```python
letters = ["a", "b", "c", "d", "e", "f", "g"]

print(letters[1:6:2])
```

**Output:**

```text
['b', 'd', 'f']
```

The selected indexes are:

```text
1, 3, 5
```

### Every Third Element

```python
values = [5, 10, 15, 20, 25, 30, 35]

print(values[0:7:3])
```

**Output:**

```text
[5, 20, 35]
```

The selected indexes are:

```text
0, 3, 6
```

### Omitting Start and Stop

```python
text = "ABCDEFGHIJ"

print(text[::3])
```

**Output:**

```text
ADGJ
```

[Back to Index](#index)

---

<a id="negative-step-slicing"></a>

## Negative-Step Slicing

A negative step moves through a sequence from right to left.

### Syntax

```python
sequence[start:stop:negative_step]
```

For a negative step:

* The start position should normally be to the right of the stop position.
* The stop position remains excluded.
* The omitted defaults differ from those used with a positive step.

### Last Three Elements in Reverse Order

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[-1:-4:-1]

print(result)
```

**Output:**

```text
[50, 40, 30]
```

The selected indexes are:

```text
-1, -2, -3
```

The stop index `-4` is excluded.

### Partial Reverse Slice

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

result = numbers[-2:-6:-2]

print(result)
```

**Output:**

```text
[60, 40]
```

The selected positions are:

```text
Index -2 → 60
Index -4 → 40
```

The next position would be `-6`, but the stop position is excluded.

### Using Positive Indexes with a Negative Step

```python
letters = ["a", "b", "c", "d", "e", "f"]

print(letters[4:1:-1])
```

**Output:**

```text
['e', 'd', 'c']
```

The selected indexes are:

```text
4, 3, 2
```

Index `1` is excluded.

[Back to Index](#index)

---

<a id="reversing-a-sequence"></a>

## Reversing a Sequence

Use a step of `-1` to reverse an entire sequence.

### Reversing a List

```python
numbers = [10, 20, 30, 40, 50]

reversed_numbers = numbers[::-1]

print(reversed_numbers)
```

**Output:**

```text
[50, 40, 30, 20, 10]
```

The original list is unchanged:

```python
print(numbers)
```

**Output:**

```text
[10, 20, 30, 40, 50]
```

### Reversing a String

```python
text = "Python"

reversed_text = text[::-1]

print(reversed_text)
```

**Output:**

```text
nohtyP
```

### Palindrome Check

```python
word = "level"

is_palindrome = word == word[::-1]

print(is_palindrome)
```

**Output:**

```text
True
```

[Back to Index](#index)

---

<a id="slice-assignment"></a>

## Slice Assignment

Slice assignment modifies several list elements at once.

It is supported by mutable sequence types such as lists.

### Syntax

```python
list_name[start:stop] = new_values
```

The right side must be an iterable.

Slice assignment can:

* Replace elements
* Insert elements
* Remove elements
* Change the list length

Strings and tuples do not support slice assignment because they are immutable.

<a id="replacing-with-slice-assignment"></a>

### 1. Replacing Multiple Elements

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:4] = [100, 200, 300]

print(numbers)
```

**Output:**

```text
[10, 100, 200, 300, 50]
```

The original elements at indexes `1`, `2`, and `3` are replaced.

```text
Before: [10,  20,  30,  40, 50]
After:  [10, 100, 200, 300, 50]
```

[Back to Index](#index)

---

<a id="inserting-with-slice-assignment"></a>

### 2. Inserting Elements Without Replacing

Use an empty slice where `start` and `stop` are equal.

```python
letters = ["a", "b", "e"]

letters[2:2] = ["c", "d"]

print(letters)
```

**Output:**

```text
['a', 'b', 'c', 'd', 'e']
```

Because `letters[2:2]` contains no elements, nothing is removed. The new values are inserted at index `2`.

### Inserting at the Beginning

```python
numbers = [30, 40]

numbers[:0] = [10, 20]

print(numbers)
```

**Output:**

```text
[10, 20, 30, 40]
```

### Inserting at the End

```python
numbers = [10, 20]

numbers[len(numbers):] = [30, 40]

print(numbers)
```

**Output:**

```text
[10, 20, 30, 40]
```

Using `extend()` is usually clearer when adding several elements to the end.

[Back to Index](#index)

---

<a id="changing-slice-length"></a>

### 3. Changing Slice Length

With an ordinary slice using a step of `1`, the number of replacement values does not need to match the number of removed values.

### Replacing Two Elements with Three

```python
numbers = [10, 20, 30, 40]

numbers[1:3] = [100, 200, 300]

print(numbers)
```

**Output:**

```text
[10, 100, 200, 300, 40]
```

The list becomes longer.

### Replacing Three Elements with One

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:4] = [999]

print(numbers)
```

**Output:**

```text
[10, 999, 50]
```

The list becomes shorter.

### Assigning a String

Because a string is iterable, each character becomes a separate list element.

```python
letters = ["a", "b", "c"]

letters[1:2] = "XY"

print(letters)
```

**Output:**

```text
['a', 'X', 'Y', 'c']
```

To insert the entire string as one element, place it inside a list:

```python
letters = ["a", "b", "c"]

letters[1:2] = ["XY"]

print(letters)
```

**Output:**

```text
['a', 'XY', 'c']
```

[Back to Index](#index)

---

<a id="extended-slice-assignment"></a>

### 4. Extended Slice Assignment

A slice with a step other than `1` is called an extended slice.

```python
list_name[start:stop:step] = new_values
```

For extended slice assignment, the number of replacement values must exactly match the number of selected positions.

### Valid Example

```python
numbers = [10, 20, 30, 40, 50, 60]

numbers[::2] = [100, 300, 500]

print(numbers)
```

**Output:**

```text
[100, 20, 300, 40, 500, 60]
```

The selected indexes are `0`, `2`, and `4`, so exactly three replacement values are required.

### Invalid Example

```python
numbers = [10, 20, 30, 40, 50, 60]

numbers[::2] = [100, 200]
```

**Error:**

```text
ValueError: attempt to assign sequence of size 2 to extended slice of size 3
```

[Back to Index](#index)

---

<a id="slice-deletion"></a>

## Slice Deletion

Multiple list elements can be removed using either:

* Assignment of an empty iterable
* The `del` statement

### Deleting with an Empty List

```python
numbers = [10, 20, 30, 40, 50, 60]

numbers[1:4] = []

print(numbers)
```

**Output:**

```text
[10, 50, 60]
```

The elements at indexes `1`, `2`, and `3` are removed.

### Deleting from the Beginning

```python
letters = ["a", "b", "c", "d", "e"]

letters[:2] = []

print(letters)
```

**Output:**

```text
['c', 'd', 'e']
```

### Deleting to the End

```python
values = [1, 2, 3, 4, 5, 6, 7]

values[3:] = []

print(values)
```

**Output:**

```text
[1, 2, 3]
```

### Using `del`

The `del` statement provides a direct way to delete a slice.

```python
numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)
```

**Output:**

```text
[10, 50]
```

### Deleting Alternating Elements

```python
numbers = [10, 20, 30, 40, 50, 60]

del numbers[::2]

print(numbers)
```

**Output:**

```text
[20, 40, 60]
```

The elements originally located at indexes `0`, `2`, and `4` are deleted.

### Clearing a List with Slicing

```python
numbers = [10, 20, 30]

numbers[:] = []

print(numbers)
```

**Output:**

```text
[]
```

This empties the existing list object.

The following form is equivalent:

```python
del numbers[:]
```

[Back to Index](#index)

---

<a id="slicing-immutable-sequences"></a>

## Slicing Strings and Tuples

Strings and tuples support reading slices, but they do not support slice assignment.

### String Slicing

```python
text = "Python Programming"

print(text[0:6])
print(text[7:])
print(text[::-1])
```

**Output:**

```text
Python
Programming
gnimmargorP nohtyP
```

### Tuple Slicing

```python
numbers = (10, 20, 30, 40, 50)

result = numbers[1:4]

print(result)
print(type(result))
```

**Output:**

```text
(20, 30, 40)
<class 'tuple'>
```

Slicing preserves the general sequence type:

* A list slice produces a list.
* A string slice produces a string.
* A tuple slice produces a tuple.

### Invalid String Slice Assignment

```python
text = "Python"

text[0:2] = "J"
```

**Error:**

```text
TypeError: 'str' object does not support item assignment
```

Create a new string instead:

```python
text = "Python"

text = "J" + text[2:]

print(text)
```

**Output:**

```text
Jthon
```

[Back to Index](#index)

---

<a id="common-slicing-errors"></a>

## Common Slicing Errors

### 1. Using a Step of Zero

A slice step cannot be zero.

```python
numbers = [10, 20, 30]

print(numbers[::0])
```

**Error:**

```text
ValueError: slice step cannot be zero
```

A zero step would prevent the slice from moving through the sequence.

### 2. Using the Wrong Direction

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[4:1])
```

**Output:**

```text
[]
```

The default step is positive, but index `4` is to the right of index `1`.

Use a negative step:

```python
print(numbers[4:1:-1])
```

**Output:**

```text
[50, 40, 30]
```

### 3. Forgetting That `stop` Is Excluded

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:3])
```

**Output:**

```text
[20, 30]
```

Index `3`, containing `40`, is excluded.

To include the element at index `3`, use a stop value of `4`:

```python
print(numbers[1:4])
```

**Output:**

```text
[20, 30, 40]
```

### 4. Confusing Indexing with Slicing

Direct indexing returns one element:

```python
numbers = [10, 20, 30]

print(numbers[1])
```

**Output:**

```text
20
```

Slicing returns a sequence:

```python
print(numbers[1:2])
```

**Output:**

```text
[20]
```

Direct indexing may raise an `IndexError`, while out-of-range slicing generally returns a shortened or empty sequence.

```python
numbers = [10, 20, 30]

print(numbers[100:])
```

**Output:**

```text
[]
```

[Back to Index](#index)

---

<a id="slicing-summary"></a>

## Slicing Summary

| Operation         | Syntax                    | Description                              |
| ----------------- | ------------------------- | ---------------------------------------- |
| Basic slice       | `items[start:stop]`       | Selects from `start` through `stop - 1`  |
| From beginning    | `items[:stop]`            | Starts from the beginning                |
| To end            | `items[start:]`           | Continues through the end                |
| Full slice        | `items[:]`                | Selects the entire sequence              |
| Positive step     | `items[start:stop:step]`  | Moves from left to right                 |
| Negative step     | `items[start:stop:-step]` | Moves from right to left                 |
| Reverse sequence  | `items[::-1]`             | Produces a reversed copy                 |
| Replace slice     | `items[a:b] = values`     | Replaces several list elements           |
| Insert values     | `items[i:i] = values`     | Inserts values without removing elements |
| Delete slice      | `items[a:b] = []`         | Removes selected elements                |
| Delete with `del` | `del items[a:b]`          | Deletes selected elements                |
| Clear list        | `items[:] = []`           | Removes every element                    |

### Combined Example

```python
numbers = [10, 20, 30, 40, 50, 60]

first_three = numbers[:3]
last_three = numbers[-3:]
alternating = numbers[::2]
reversed_numbers = numbers[::-1]

print("First three:", first_three)
print("Last three:", last_three)
print("Alternating:", alternating)
print("Reversed:", reversed_numbers)

numbers[1:3] = [200, 300, 400]
numbers[2:2] = [999]
del numbers[-2:]

print("Modified:", numbers)
```

**Output:**

```text
First three: [10, 20, 30]
Last three: [40, 50, 60]
Alternating: [10, 30, 50]
Reversed: [60, 50, 40, 30, 20, 10]
Modified: [10, 200, 999, 300, 400]
```

The original list changes as follows:

```text
Initial:
[10, 20, 30, 40, 50, 60]

After numbers[1:3] = [200, 300, 400]:
[10, 200, 300, 400, 40, 50, 60]

After numbers[2:2] = [999]:
[10, 200, 999, 300, 400, 40, 50, 60]

After del numbers[-2:]:
[10, 200, 999, 300, 400]
```

[Back to Index](#index)