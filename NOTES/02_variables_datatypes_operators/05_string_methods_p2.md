<a id="string-searching-and-formatting-methods"></a>

## String Searching and Formatting Methods in Python

Python provides built-in string methods for searching, counting, replacing, splitting, joining, validating, padding, and aligning text.

Because strings are immutable, these methods do not modify the original string. Methods such as `replace()`, `join()`, `zfill()`, and `center()` return new strings.

<a id="index"></a>

## Index

1. [Finding Substrings with `find()`](#find-method)

   * [Basic Usage](#find-basic-usage)
   * [Substring Not Found](#find-substring-not-found)
   * [Using Start and End Parameters](#find-start-and-end)
2. [Finding Substrings with `index()`](#index-method)

   * [`find()` Compared with `index()`](#find-versus-index)
   * [Handling `ValueError`](#handling-index-value-error)
3. [Counting Occurrences with `count()`](#count-method)

   * [Counting Without a Range](#count-without-range)
   * [Counting Within a Range](#count-within-range)
   * [Non-Overlapping Matches](#count-non-overlapping)
4. [Replacing Content with `replace()`](#replace-method)

   * [Replacing All Matches](#replace-all-matches)
   * [Limiting Replacements](#limiting-replacements)
   * [Case Sensitivity](#replace-case-sensitivity)
5. [Splitting Strings with `split()`](#split-method)

   * [Splitting on Whitespace](#split-whitespace)
   * [Using a Separator](#split-separator)
   * [Limiting the Number of Splits](#split-maxsplit)
6. [Joining Strings with `join()`](#join-method)

   * [Joining List Elements](#joining-list-elements)
   * [Joining Characters](#joining-characters)
   * [Joining Non-String Values](#joining-non-string-values)
7. [Checking String Beginnings with `startswith()`](#startswith-method)

   * [Checking One Prefix](#checking-one-prefix)
   * [Checking Multiple Prefixes](#checking-multiple-prefixes)
   * [Using Start and End Parameters](#startswith-range)
8. [Checking String Endings with `endswith()`](#endswith-method)

   * [Checking One Suffix](#checking-one-suffix)
   * [Checking Multiple Suffixes](#checking-multiple-suffixes)
   * [Using Start and End Parameters](#endswith-range)
9. [Padding Strings with `zfill()`](#zfill-method)

   * [Basic Zero Padding](#basic-zero-padding)
   * [Padding Signed Numbers](#padding-signed-numbers)
   * [Width Smaller Than the String](#zfill-smaller-width)
10. [Centering Strings with `center()`](#center-method)

    * [Centering with Spaces](#centering-with-spaces)
    * [Using a Fill Character](#center-fill-character)
    * [Uneven Padding](#center-uneven-padding)

---

<a id="find-method"></a>

## Finding Substrings with `find()`

The `find()` method searches for a substring and returns the starting index of its first occurrence.

If the substring is not found, `find()` returns `-1`.

### Syntax

```python
string.find(substring, start, end)
```

* `substring` is the sequence of characters to search for.
* `start` is the optional index where the search begins.
* `end` is the optional index where the search stops. This index is excluded.

Both `start` and `end` follow the same rules as string slicing.

<a id="find-basic-usage"></a>

### 1. Basic Usage

```python
text = "Hello, welcome to the world of Python!"
position = text.find("welcome")

print(position)
```

**Output:**

```text
7
```

The substring `"welcome"` begins at index `7`.

```text
H e l l o ,   w e l c o m e
0 1 2 3 4 5 6 7
```

<a id="find-substring-not-found"></a>

### 2. Substring Not Found

```python
text = "The quick brown fox jumps over the lazy dog"
position = text.find("fix")

print(position)
```

**Output:**

```text
-1
```

The substring `"fix"` does not appear in the string, so `find()` returns `-1`.

<a id="find-start-and-end"></a>

### 3. Using Start and End Parameters

```python
text = "Python is easy. Python is powerful."

position = text.find("Python", 10, 30)

print(position)
```

**Output:**

```text
16
```

The search begins at index `10` and stops before index `30`. Therefore, Python ignores the first occurrence and finds the second occurrence at index `16`.

A search may also return `-1` when the substring exists outside the specified range.

```python
text = "The quick brown fox jumps over the lazy dog"
position = text.find("fox", 20, 40)

print(position)
```

**Output:**

```text
-1
```

The substring `"fox"` exists in the complete string, but it does not occur between indexes `20` and `40`.

[Back to Index](#index)

---

<a id="index-method"></a>

## Finding Substrings with `index()`

The `index()` method searches for a substring and returns the starting index of its first occurrence.

### Syntax

```python
string.index(substring, start, end)
```

Its parameters work like those of `find()`:

* `substring` is the text to search for.
* `start` is the optional starting index.
* `end` is the optional ending index and is excluded.

The main difference is what happens when the substring is not found.

* `find()` returns `-1`.
* `index()` raises a `ValueError`.

<a id="find-versus-index"></a>

### 1. `find()` Compared with `index()`

```python
text = "Hello World"

print(text.find("o"))
print(text.index("o"))
```

**Output:**

```text
4
4
```

Both methods return `4` because the first `"o"` occurs at index `4`.

When the substring is missing:

```python
text = "Hello World"

print(text.find("z"))
```

**Output:**

```text
-1
```

Using `index()` with the same missing substring raises an error:

```python
text = "Hello World"

print(text.index("z"))
```

**Error:**

```text
ValueError: substring not found
```

<a id="handling-index-value-error"></a>

### 2. Handling `ValueError`

Use `try` and `except` when a missing substring is expected and you still want to use `index()`.

```python
text = "Hello World"

try:
    position = text.index("z")
    print(position)
except ValueError:
    print("Substring not found.")
```

**Output:**

```text
Substring not found.
```

Use `find()` when returning `-1` is convenient. Use `index()` when a missing substring should be treated as an error.

[Back to Index](#index)

---

<a id="count-method"></a>

## Counting Occurrences with `count()`

The `count()` method returns the number of times a substring occurs in a string.

### Syntax

```python
string.count(substring, start, end)
```

* `substring` is the sequence to count.
* `start` is the optional index where counting begins.
* `end` is the optional index where counting stops and is excluded.

<a id="count-without-range"></a>

### 1. Counting Without a Range

```python
text = "Hello, welcome to Python programming. Python is fun."
python_count = text.count("Python")

print(python_count)
```

**Output:**

```text
2
```

The substring `"Python"` appears twice.

The search is case-sensitive:

```python
text = "Python python PYTHON"

print(text.count("Python"))
```

**Output:**

```text
1
```

Only the exact substring `"Python"` is counted.

<a id="count-within-range"></a>

### 2. Counting Within a Range

```python
text = "Hello, welcome to the world of Python programming. Python is fun."
range_count = text.count("Python", 20, 50)

print(range_count)
```

**Output:**

```text
1
```

Only the portion from index `20` up to, but not including, index `50` is searched.

<a id="count-non-overlapping"></a>

### 3. Non-Overlapping Matches

The `count()` method counts non-overlapping occurrences.

```python
text = "aaaa"

print(text.count("aa"))
```

**Output:**

```text
2
```

Python counts the following two matches:

```text
aa aa
```

It does not count every possible overlapping occurrence.

[Back to Index](#index)

---

<a id="replace-method"></a>

## Replacing Content with `replace()`

The `replace()` method returns a new string in which occurrences of one substring are replaced with another substring.

### Syntax

```python
string.replace(old, new, count)
```

* `old` is the substring to replace.
* `new` is the replacement substring.
* `count` is the optional maximum number of replacements.

When `count` is omitted, every matching occurrence is replaced.

<a id="replace-all-matches"></a>

### 1. Replacing All Matches

```python
text = "I like apples. Green apples are delicious."
modified_text = text.replace("apples", "oranges")

print(modified_text)
```

**Output:**

```text
I like oranges. Green oranges are delicious.
```

The original string remains unchanged:

```python
print(text)
```

**Output:**

```text
I like apples. Green apples are delicious.
```

<a id="limiting-replacements"></a>

### 2. Limiting the Number of Replacements

The third argument limits how many occurrences are replaced.

```python
text = "one one one one"
limited_text = text.replace("one", "two", 2)

print(limited_text)
```

**Output:**

```text
two two one one
```

Only the first two occurrences are replaced.

<a id="replace-case-sensitivity"></a>

### 3. Case Sensitivity

The `replace()` method is case-sensitive.

```python
text = "I love apples. Apples are my favorite fruit."
modified_text = text.replace("apples", "oranges")

print(modified_text)
```

**Output:**

```text
I love oranges. Apples are my favorite fruit.
```

The lowercase substring `"apples"` is replaced, but `"Apples"` remains unchanged.

```python
text = "I love apples. Apples are my favorite fruit."
limited_text = text.replace("apples", "oranges", 1)

print(limited_text)
```

**Output:**

```text
I love oranges. Apples are my favorite fruit.
```

[Back to Index](#index)

---

<a id="split-method"></a>

## Splitting Strings with `split()`

The `split()` method divides a string into a list of substrings.

### Syntax

```python
string.split(separator, maxsplit)
```

* `separator` specifies where the string should be divided.
* `maxsplit` specifies the maximum number of splits.

Both parameters are optional.

<a id="split-whitespace"></a>

### 1. Splitting on Whitespace

When no separator is supplied, Python splits the string on whitespace.

```python
text = "Hello world! Welcome to Python."
words = text.split()

print(words)
```

**Output:**

```text
['Hello', 'world!', 'Welcome', 'to', 'Python.']
```

When no separator is provided:

* Consecutive whitespace characters are treated as one separator.
* Leading and trailing whitespace is ignored.
* Spaces, tabs, and newline characters can act as separators.

```python
text = "  Python   is\tpowerful\nand readable  "

print(text.split())
```

**Output:**

```text
['Python', 'is', 'powerful', 'and', 'readable']
```

<a id="split-separator"></a>

### 2. Using a Separator

```python
data = "apple,banana,cherry"
fruits = data.split(",")

print(fruits)
```

**Output:**

```text
['apple', 'banana', 'cherry']
```

When an explicit separator is supplied, consecutive separators can produce empty strings.

```python
data = "apple,,cherry"

print(data.split(","))
```

**Output:**

```text
['apple', '', 'cherry']
```

> For complete CSV files, use Python's `csv` module because CSV data may contain quoted commas and other special cases.

<a id="split-maxsplit"></a>

### 3. Limiting the Number of Splits

The `maxsplit` argument controls the maximum number of divisions.

```python
text = "one two three four five"
limited_split = text.split(" ", 2)

print(limited_split)
```

**Output:**

```text
['one', 'two', 'three four five']
```

Only two splits are performed. The remaining text becomes the final list element.

```python
record = "name:age:location:occupation"
parts = record.split(":", 2)

print(parts)
```

**Output:**

```text
['name', 'age', 'location:occupation']
```

[Back to Index](#index)

---

<a id="join-method"></a>

## Joining Strings with `join()`

The `join()` method combines the string elements of an iterable into one string.

The string on which `join()` is called becomes the separator.

### Syntax

```python
separator.join(iterable)
```

* `separator` is placed between the elements.
* `iterable` can be a list, tuple, string, or another iterable containing strings.

<a id="joining-list-elements"></a>

### 1. Joining List Elements

```python
words = ["Python", "is", "readable"]
sentence = " ".join(words)

print(sentence)
```

**Output:**

```text
Python is readable
```

Using a comma as the separator:

```python
fruits = ["apple", "banana", "cherry"]
result = ", ".join(fruits)

print(result)
```

**Output:**

```text
apple, banana, cherry
```

Using an empty separator combines the elements without adding characters between them:

```python
letters = ["P", "y", "t", "h", "o", "n"]

print("".join(letters))
```

**Output:**

```text
Python
```

<a id="joining-characters"></a>

### 2. Joining Characters

A string is itself an iterable of characters.

```python
separator = "-"
original_string = "Hello"
result = separator.join(original_string)

print(result)
```

**Output:**

```text
H-e-l-l-o
```

Adding spaces between characters:

```python
separator = " "
original_string = "World"
result = separator.join(original_string)

print(result)
```

**Output:**

```text
W o r l d
```

<a id="joining-non-string-values"></a>

### 3. Joining Non-String Values

Every item passed to `join()` must be a string.

The following example raises an error:

```python
numbers = [1, 2, 3]

result = "-".join(numbers)
```

**Error:**

```text
TypeError: sequence item 0: expected str instance, int found
```

Convert the values to strings first:

```python
numbers = [1, 2, 3]
converted_numbers = [str(number) for number in numbers]

result = "-".join(converted_numbers)

print(result)
```

**Output:**

```text
1-2-3
```

The conversion can also be performed with `map()`:

```python
numbers = [1, 2, 3]

result = "-".join(map(str, numbers))

print(result)
```

**Output:**

```text
1-2-3
```

[Back to Index](#index)

---

<a id="startswith-method"></a>

## Checking String Beginnings with `startswith()`

The `startswith()` method checks whether a string begins with a specified prefix.

It returns either `True` or `False`.

### Syntax

```python
string.startswith(prefix, start, end)
```

* `prefix` is the substring to check.
* `start` is the optional index where checking begins.
* `end` is the optional index where checking stops and is excluded.

<a id="checking-one-prefix"></a>

### 1. Checking One Prefix

```python
message = "Hello, world!"
result = message.startswith("Hello")

print(result)
```

**Output:**

```text
True
```

A prefix must match exactly, including capitalization.

```python
message = "Hello, world!"

print(message.startswith("hello"))
```

**Output:**

```text
False
```

<a id="checking-multiple-prefixes"></a>

### 2. Checking Multiple Prefixes

Pass a tuple of prefixes to check several possibilities.

```python
file_name = "document.pdf"
result = file_name.startswith(("doc", "file", "report"))

print(result)
```

**Output:**

```text
True
```

The result is `True` because `"document.pdf"` begins with `"doc"`.

> Multiple prefixes must be supplied as a tuple, using parentheses.

<a id="startswith-range"></a>

### 3. Using Start and End Parameters

```python
text = "Welcome to Python programming!"
result = text.startswith("Python", 11, 17)

print(result)
```

**Output:**

```text
True
```

Python checks the section from index `11` to index `17`:

```text
Python
```

The `end` index is excluded.

[Back to Index](#index)

---

<a id="endswith-method"></a>

## Checking String Endings with `endswith()`

The `endswith()` method checks whether a string ends with a specified suffix.

It returns either `True` or `False`.

### Syntax

```python
string.endswith(suffix, start, end)
```

* `suffix` is the substring to check.
* `start` is the optional index where checking begins.
* `end` is the optional index where checking stops and is excluded.

<a id="checking-one-suffix"></a>

### 1. Checking One Suffix

```python
text = "Hello, world!"

print(text.endswith("world!"))
print(text.endswith("Hello"))
```

**Output:**

```text
True
False
```

The check is case-sensitive:

```python
filename = "REPORT.PDF"

print(filename.endswith(".pdf"))
```

**Output:**

```text
False
```

For a case-insensitive extension check, normalize the string first:

```python
filename = "REPORT.PDF"

print(filename.lower().endswith(".pdf"))
```

**Output:**

```text
True
```

<a id="checking-multiple-suffixes"></a>

### 2. Checking Multiple Suffixes

Pass a tuple to check multiple possible suffixes.

```python
filename = "document.pdf"
result = filename.endswith((".pdf", ".docx", ".txt"))

print(result)
```

**Output:**

```text
True
```

The result is `True` because the filename ends with `".pdf"`.

<a id="endswith-range"></a>

### 3. Using Start and End Parameters

The optional range limits the portion of the string being checked.

```python
text = "Hello, world!"

print(text.endswith("lo", 0, 5))
```

**Output:**

```text
True
```

Python checks the substring:

```text
Hello
```

That substring ends with `"lo"`.

Another example:

```python
text = "Hello, world!"

print(text.endswith("world", 0, 12))
```

**Output:**

```text
True
```

Python checks the substring:

```text
Hello, world
```

That portion ends with `"world"`.

[Back to Index](#index)

---

<a id="zfill-method"></a>

## Padding Strings with `zfill()`

The `zfill()` method pads a string with leading zeros until it reaches a specified width.

It is commonly used for:

* Identification numbers
* Invoice numbers
* File numbers
* Dates and times
* Uniform numeric displays

### Syntax

```python
string.zfill(width)
```

`width` is the total desired length of the resulting string.

<a id="basic-zero-padding"></a>

### 1. Basic Zero Padding

```python
number = "42"
padded_number = number.zfill(5)

print(padded_number)
```

**Output:**

```text
00042
```

The original string contains two characters. Three zeros are added to produce a total width of five.

```python
print(len(padded_number))
```

**Output:**

```text
5
```

<a id="padding-signed-numbers"></a>

### 2. Padding Signed Numbers

When a string begins with `+` or `-`, zeros are inserted after the sign.

```python
negative_number = "-5"
padded_negative = negative_number.zfill(4)

print(padded_negative)
```

**Output:**

```text
-005
```

A positive sign is handled similarly:

```python
positive_number = "+5"

print(positive_number.zfill(4))
```

**Output:**

```text
+005
```

The sign remains at the beginning of the string.

<a id="zfill-smaller-width"></a>

### 3. Width Smaller Than the String

If the requested width is less than or equal to the current string length, the string is returned unchanged.

```python
long_number = "123456"
padded_number = long_number.zfill(3)

print(padded_number)
```

**Output:**

```text
123456
```

The original string is already longer than three characters, so no zeros are added.

```python
number = "123"

print(number.zfill(3))
```

**Output:**

```text
123
```

[Back to Index](#index)

---

<a id="center-method"></a>

## Centering Strings with `center()`

The `center()` method returns a new string centered within a specified width.

### Syntax

```python
string.center(width, fillchar)
```

* `width` is the total desired length.
* `fillchar` is the optional character used for padding.
* The default fill character is a space.
* `fillchar` must contain exactly one character.

<a id="centering-with-spaces"></a>

### 1. Centering with Spaces

```python
text = "Hello"
centered_text = text.center(10)

print(repr(centered_text))
```

**Output:**

```text
'  Hello   '
```

The resulting string contains:

* Two spaces on the left
* The text `"Hello"`
* Three spaces on the right

Using `repr()` makes the surrounding spaces visible.

<a id="center-fill-character"></a>

### 2. Using a Fill Character

```python
text = "Hello"
centered_text = text.center(10, "*")

print(centered_text)
```

**Output:**

```text
**Hello***
```

The resulting string has a total length of `10`.

```python
print(len(centered_text))
```

**Output:**

```text
10
```

The fill character must be exactly one character long.

The following example raises an error:

```python
text = "Hello"

print(text.center(10, "**"))
```

**Error:**

```text
TypeError: The fill character must be exactly one character long
```

<a id="center-uneven-padding"></a>

### 3. Uneven Padding

When the available padding cannot be divided evenly, the extra fill character is placed on the right side.

```python
text = "Hello"
result = text.center(10, "*")

print(result)
```

**Output:**

```text
**Hello***
```

The original string has a length of `5`, while the requested width is `10`.

```text
Available padding = 10 - 5 = 5
```

Because five padding characters cannot be split equally:

* Two are placed on the left.
* Three are placed on the right.

If the requested width is smaller than the string's current length, the string is returned unchanged.

```python
text = "Hello"

print(text.center(3, "*"))
```

**Output:**

```text
Hello
```

[Back to Index](#index)