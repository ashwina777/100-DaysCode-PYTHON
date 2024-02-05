# String Operations in Python

Strings are a fundamental data type in Python, and the language provides a variety of operations to manipulate and work with them effectively.

## 1. Concatenation

Concatenation is the process of combining strings. You can use the `+` operator to concatenate two or more strings:

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe 
```
## 2. String Multiplication
You can use the * operator to repeat a string multiple times:

```python
greeting = "Hello "
repeat_greeting = greeting * 3
print(repeat_greeting)  # Output: Hello Hello Hello
```
## 3. Accessing Characters
Individual characters in a string can be accessed using indexing. Indexing starts at 0 for the first character:

```python
language = "Python"
first_letter = language[0]
print(first_letter)  # Output: P
```
## 4. String Slicing
String slicing allows you to extract a substring from a string by specifying a range:

```python
message = "Hello, World!"
substring = message[7:12]
print(substring)  # Output: World
```
## 5. String Methods 
will discuss string methods in next module