# Day 4 - Our First Program

Today we will write our first ever python program from scratch. It will consist of a bunch of print statements.
print can be used to print something on the console in python

# Python Print Statement

The `print()` function in Python is a built-in function used to display information on the console. It is a simple yet powerful tool for debugging and providing output in your Python programs.

## Syntax

The syntax of the `print()` function is straightforward:

```python
print(object(s), sep=separator, end=end, file=file, flush=flush)
```
**object(s)**: This is the object or objects you want to print. You can provide multiple objects separated by commas.

**sep (optional)**: The separator between the objects. It is a space by default.

**end (optional)**: The string that is printed at the end. The default is a newline character \n.

**file (optional)**: An object with a write() method. This parameter allows you to specify the file where the output will be written. The default is sys.stdout, which is the console.

**flush (optional)**: A boolean value. If True, the output is forcibly flushed. The default is False.