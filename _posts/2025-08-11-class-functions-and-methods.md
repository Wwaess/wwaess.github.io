---
title: "Class Functions and Methods"
date: 2025-08-11 00:00:00 +0000
categories: [OOP]
tags: [OOP]
---

# Class Functions and Methods

Chapters 16 and 17 of *Think Python* by Allen Downey explores two sets of key concepts. Namely, Chapter 16 explores how we can use classes to represent geometric objects (using the `jupyturtle` module in Python), and Chapter 17 introduces *inheritance*, the feature "most often associated" with OOP, where new classes are defined using other existing classes. 

# Classes and Objects

## Creating a Point

A screen, being a 2D canvas, requires two variables - an x- and y-coordinate - to uniquely identify a point on it. Of note, typically in computer graphics, the y-coordinate refers to the amount of pixels _down_ the screen (so `(0,0)` is the top-right-most pixel). 

We can represent this point
- using two variables `x` and `y`
- as elements in a list or tuple
- create a new type to represent points as objects in their own right
...and given that this is OOP - you can guess which one we're gonna use. 

We'll define a new class called Point: 

```python
class Point:
    """Represents a point in 2D"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Point({self.x}, {self.y})' 
```

