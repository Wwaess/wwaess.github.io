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

```py
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
```py
start = Point(0, 0)
print(start)
```

```output
Point(0, 0)
```

We can add some more functions to change these types (i.e. the variables). We call values *mutable* when they can be changed during program execution; program-defined types are generally *mutable*. 
Let's add a method `translate` to add `dx` and `dy` (changes) to the attributes `x` and `y`:
```py
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

Now to actually draw it - well, we first need to find the other points, then make the Line objects needed to draw the sides, then actually draw them: 
```py
%%add_method_to Rectangle

    def make_points(self): 
        p1 = self.corner
        p2 = p1.translated(self.width, 0)
        p3 = p2.translated(0, self.height)
        p4 = p3.translated(-self.width, 0)
        return p1, p2, p3, p4
    
    def make_lines(self):
        p1, p2, p3, p4 = make_points(self) # using the method we just created
        return Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)

    def draw(self):
        lines = self.make_lines()
        for line in lines:
            line.draw()
```

Now if we call
```py
make_turtle() # to summon the almighty turtle of computer science
line1.draw() # that x-axis
line2.draw() # that y-axis
box1.draw() # ...the box we just specified
```

we end up with... a box. 

## Changing Rectangles

We can add a `grow` function:
```py
%%add_method_to Rectangle

    def grow(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight
```

```py
box2 = copy(box1)
box2.grow(60, 40)
### print(box2)
box2.draw()
```

Now, this works fine - but we can't do the same with translation. If we used 
```py 
def translate(self, dx, dy): 
    self.corner.translate(dx, dy)
``` 

then this will move BOTH rectangles! That's because the `copy` function is a little odd. 
`box1 is box2` will return `False`, which is what we expected. But the POINTERS `corner` in each of these boxes _point_ to the same... _Point_ object... `DIAGRAM`:

To actually force a new copy that points to its own new contained objects, we need to grab `from copy import deepcopy`. 


## Polymorphism
Given that both Lines and Boxes now have a `draw` function, we can invoke those with the same command: 

```py
shapes = [line1, line2, box3, box4]

make_turtle()
for shape in shapes: 
    shape.draw()
```

This last line, where we've called a `.draw()` for shapes, regardless of whether they're a line or a box, is a feature called **polymorphism** - we invoke the same command, but each Object interprets it however they're defined in their own class description. 

## Debugging
Recall that we had to `deepcopy` instead of `copy` the rectangles from earlier so that we could actually `translate` them. 
Ideally we can try to avoid subtle bugs like that if we can do one of two things, generally speaking:
- avoid sharing objects; or 
- avoid modifying them. 

The first example, we've just gone through - that's what `deepcopy` took care of. 
For the second - replace _impure_ functions like `translate` with _pure_ functions like `translated`... apparently. 



# Inheritance

## Representing Cards

If we want to represent the cards in a standard deck of 52, it's pretty obvious that a Card class should contain the attributes `rank` and `suit`. We *could* encode these as strings, but then it makes it harder to figure out how to compare cards...

Let's instead use integers to encode them. Let Clubs be `0`, Diamonds be `1`, Hearts be `2` and Spades be `3`. Similarly let Jack be `11`, Queen be `12` and King be `13`. Now Ace can either be `1` or `14`, depending on how we want to classify its position among the ranks. 

To represent these encodings, we can actually use a string **list**, which indexes from 0 (meaning we need to add a `None` to the rank list): 

```py
class Card:
    """Represents a standard playing card, out of a deck of 52"""
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
```

Now, we can call these attributes from the class itself (instead of from an _instance_ of the class) - so to see the list of suit names, we can call `Card.suit_names()`. 

## Card Attributes

To actually generate a card, we'll use the `__init__` function: 
```py
%%add_method_to Card

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
```
Now we can create a Card object like `queen = Card(1,12)`. 

## Printing Cards

Now to print them: 
```py
%%add_method_to Card

    def __str__(self):
        rank_name = Card.rank_names[self.rank]]
        suit_name = Card.suit_names[self.suit]]
        return f'{rank_name} of {suit_name}'
```
Now calling `print(queen)` will output `Queen of Diamonds`.

