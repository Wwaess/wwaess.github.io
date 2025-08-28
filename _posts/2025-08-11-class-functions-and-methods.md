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

The `__init__` method takes the coordinates as parameters and assigns them as attributes to `self`. 
The `__str__` method returns a string representation of this `Point`. 

Now we can display a point like so:
```python
start = Point(0, 0)
print(start)
```

```output
Point(0, 0)
```

We can add some more functions to change these types (i.e. the variables). We call values *mutable* when they can be changed during program execution; program-defined types are generally *mutable*. 
Let's add a method `translate` to add `dx` and `dy` (changes) to the attributes `x` and `y`:
```python
%%add_method_to Point
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

Suppose we wanted to change a _copy_ of a point. We can import `copy` from the library that is... also called `copy` (are you kidding me) to... well, _copy_ the point; we can then modify the copy. 
```py
from copy import copy

end1 = copy(start) # So this is now another Point object
end1.translate(300,0)
print(end1)
```

```output
Point(300, 0)
```

We can put both of these together - "translate a copied point" - into another method called `translated`: 

```py
%%add_method_to Point

    def translated(self, dx = 0, dy = 0):
        point = copy(self)
        point.translate(dx,dy)
        return point
```

(NB: this relies on `copy`, so we still need that import-line at the top.)
This is analogous to Python's inbuilt `sort` and `sorted` functions, whereby the first one _modifies_ a list, but the second one actually _creates_ a new list. 

```py
end2 = start.translated(0, 150)
print(end2)
```
```output
Point(0, 150)
```
