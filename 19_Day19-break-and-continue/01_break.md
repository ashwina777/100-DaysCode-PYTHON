# Break Statement in Python
In Python, the `break` statement is used to exit the loop prematurely, regardless of whether the loop's condition has been satisfied or not. It is typically used inside loops (such as `for` or `while` loops) to terminate the loop's execution based on a certain condition.

Here's a basic example of using the `break` statement within a `while` loop:

```python
count = 0
while True:  # Infinite loop
    print(count)
    count += 1
    if count >= 5:
        break  # Exit the loop when count reaches 5

Sure, here's the given text in Markdown format:

markdown
Copy code
In Python, the `break` statement is used to exit the loop prematurely, regardless of whether the loop's condition has been satisfied or not. It is typically used inside loops (such as `for` or `while` loops) to terminate the loop's execution based on a certain condition.

Here's a basic example of using the `break` statement within a `while` loop:

```python
count = 0
while True:  # Infinite loop
    print(count)
    count += 1
    if count >= 5:
        break  # Exit the loop when count reaches 5
```
In this example:

- The while True creates an infinite loop because the condition is always true.
- Inside the loop, count is incremented by 1 in each iteration.
- The if statement checks if count has reached 5.
- When count is greater than or equal to 5, the break statement is executed, causing the loop to terminate immediately.

> The break statement can be used in for loops as well, with a similar effect of prematurely ending the loop's execution based on a specific condition.
