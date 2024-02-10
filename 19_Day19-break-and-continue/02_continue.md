# Continue Statement in Python
In Python, the `continue` statement is used to skip the rest of the code inside a loop for the current iteration and proceed to the next iteration. It is typically used inside loops (such as `for` or `while` loops) to skip certain iterations based on a specific condition without terminating the entire loop.

Here's a basic example of using the `continue` statement within a `for` loop:

```python
for i in range(1, 6):
    if i == 3:
        continue  # Skip printing number 3
    print(i)
```
In this example:

- The loop iterates over the numbers from 1 to 5.
- The if statement checks if the current value of i is equal to 3.
- If i is equal to 3, the continue statement is executed, causing the loop to skip the rest of the code block for that iteration.
- As a result, the number 3 is not printed, and the loop proceeds to the next iteration.
> The continue statement can also be used with while loops in a similar manner to skip specific iterations based on a condition.
