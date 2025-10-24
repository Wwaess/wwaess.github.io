---
title: "Errors and Data Structures"
date: 2025-09-23 00:00:00 +0000
categories: [OOP]
tags: [OOP]
---

For **UNIT 8**
# Errors and Data Structures

# Errors
Errors happen naturally while coding. We can run parts of our code in a simulated separation if we want to debug and hunt for them, without causing the entire program to crash. 

In Python, this is done withe the "try" and "except" keywords:

```py 
try:
    # Do something, which might have an error
except """We can specify errors here if we want""":
    # Handle the error
``` 

Here's an example of this with some error handling: 

```py
"""This code block asks for two user-input numbers and divides one by the other."""
try: 
    # Get user input
    x = int(input("Enter the dividend: "))
    y = int(input("Enter the divisor: "))

    # Try to divide them
    result = x / y
    print("Result: ", result)

except ValueError:
    # Executed if x and/or y isn't a number - since the int() casting fails
    print("[ERROR] You must enter numbers only!")

except (TypeError, ZeroDivisionError):
    # TypeError is rare, but would execute if e.g. the program tries to divide a string by an integer, which does not work
    # ZeroDivisionError will happen if y = 0. 
    print("[ERROR] Cannot divide by 0, or invalid operation occurred")

```

## Data Structures
Here are some set operators:
- UNION (A ∪ B): Create a set of all elements that are in A, B, or both
- INTERSECTION (A ∩ B): Create a set of all elements that are in both A and B
- DIFFERENCE (A - B): Create a set of all elements that are in A but not in B
- SYMMETRIC DIFFERENCE (A △ B): `DIFFERENCE(UNION(A, B), INTERSECTION(A, B))`

At present I don't know whether I'd need all of these in the summative assessment. Maybe the union operator would make sense when checking for whether _any_ of the components needed for a build are missing (since just one item missing is enough to abort the build, and more than one item can be missing). 

"Write a Python program to carry out a linear search on a list data structure"

```py
def linear_search(data_list, target):
    # Go through the list, item by item
    for index in range(len(data_list)):
        if data_list[index] == target: # check if indexed is target
            return index # and return it if so
    return -1 # return -1 as a failure; standard practice apparently

# example list
items = ["bridge", "strings", "pickup", "tuner", "fretwire"]

# ask what to search for
search_item = input("Enter what item to search for: ")

# call linear_search()
linear_search(items, search_item)

# display the result
if result != -1:
    print(f"{search item} found at index {result}.")
else:  
    print(f"Sorry, \"{search item}\" is not in the list. ")
```

