# Match Case in Python

In Python, `match` is a feature introduced in ```Python 3.10``` as part of Pattern Matching. It provides a more concise and expressive way to perform pattern matching against the value of an expression. `match` can be thought of as an enhanced version of `switch` or `case` statements found in other programming languages.

The `match` statement allows you to compare a value against several patterns, executing different code blocks based on which pattern matches. The `match` statement works with constants, variables, and even more complex patterns like sequences and structures.

The `case` keyword is used within the `match` statement to define the different patterns and the corresponding actions to take when a pattern matches.

Here's a basic example to illustrate how `match` works:

```python
def classify_value(value):
    match value:
        case 1:
            print("Value is 1")
        match case 2 | 3:
            print("Value is 2 or 3")
            if value == 2:
                print("It's exactly 2!")
        case _:
            print("Value doesn't match any specific case")

# Test cases with different values and their expected outputs:
classify_value(1)  # Output: Value is 1
classify_value(2)  # Output: Value is 2 or 3 \n It's exactly 2!
classify_value(3)  # Output: Value is 2 or 3
classify_value(4)  # Output: Value doesn't match any specific case
```
### Explanation of Outputs:

- `classify_value(1)`: The input value is 1, which matches the pattern `case 1`, so it prints "Value is 1".
- `classify_value(2)`: The input value is 2, which matches the pattern `case 2 | 3`. It then enters the nested `match case` block, where it checks if `value` is exactly 2, printing "It's exactly 2!". Finally, it prints "Value is 2 or 3".
- `classify_value(3)`: Similar to the previous case, the input value is 3, which matches the pattern `case 2 | 3`. It follows the same execution path and prints "Value is 2 or 3".
- `classify_value(4)`: The input value is 4, which doesn't match any specific case, so it prints "Value doesn't match any specific case".
