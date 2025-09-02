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
```
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

## Creating a Line

Now that that's out of the way, let's define a class for a line segment (which is definitionally the shortest length between two points). As before, set up an `__init__` and a `__str__`: 

```py
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return f'Line({self.p1}, {self.p2})' 
```

Now we can display a `Line` object for an x-axis: 
```py
line1 = Line(start, end1)
print(Line1)
```
```output
Line(Point(0, 0), Point(300, 0))
```

Now, the actual `__str__` function is what is called when you ask the program to print the object with the class which contains the `__str__` function. So when we call the names of the point objects inside the `print` function when we print the `line1` object, the "Point" part of `Point`'s `__str__` gets called too. 

At this point, we can _print_ these results out, which is useful for debugging; but if we want to draw these, we need to grab that `jupyturtle` library. 

```py
from jupyturtle import make_turtle, jumpto, moveto
```
and use these to add a method in the `Line` class:
```py
%%add_method_to Line

    def draw(self):
        jumpto(self.p1.x, self.p1.y) # Go to the first coord. of the Line
        moveto(self.p2.x, self.p2.y) # DRAW to the second coord. of the Line
```

Now if we add a second line to represent the y-axis, we can draw the axes themselves in:

```py
line2 = Line(start, end2)
print(line2)
```
```output
Line(Point(0, 0), (0, 150))
```

```py
make_turtle()
line1.draw()
line2.draw()
```


## Equivalence and Identity

If we have two points with the same coordinates, we can use the `==` operator to compare them... only that the default behaviour is to return `True` only if they're the exact same object. So `p1 == p2` for two points with the same coordinates returns `False`. 

We can change this by adding a method to the class `Point` to define what "equals" should mean: 

```py
%%add_method_to Point

def __eq__(self, other):
    # Check each coordinate in SELF and OTHER
    return (self.x == other.x) and (self.y == other.y)
```

Now testing `p1 == p2` returns `True`! 
Note that `is` can never be overridden - it is exclusively used to detect whether two objects are identical. What we've defined is `equivalence`. 


## Creating a Rectangle

Let's draw rectangles. We won't consider rotations, so they're aligned with the axes. In that case, there are two possibilities of what attributes this `Rectangle` class should have: 
- Specify the width, height, and one corner's location;
- Specify two opposing corners. 

Let's try the first one: 

```py 
class Rectangle:
    """
    Represents a rectangle. 
    It has the attributes WIDTH, HEIGHT and CORNER. 
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

        def __str__(self): ### THIS SEEMS WRONG
            return f'Rectangle({self.width}, {self.height}, {self.corner})
```

Now if we define a point, we can build this rectangle:
```py 
corner = Point(30, 20)
box1 = Rectangle(100, 50, corner)
print(box1)
```
```output
Rectangle(100, 50, Point(30, 20))
```
