For **UNIT 6**
# Encapsulation

```
This section seems to be missing from the textbook referenced: I've based these notes from Chapter 4 of Think Python, where encapsulation is introduced. 
```

This is when you write a block of code into a function; you can call this function however many times you need it. 

It's also a nifty way of documentation wihtout commenting - though you should still comment what the function does / is for.

The function 

```py
def square(length): 
    for i in range(4):
        forward(length)
        left(90)
```

depends on the input `length` that gets passed through. This dependency is called a *parameter*; defining a function with a parameter is called *parametrisation*. 

So if we wanted to draw two squares with different sizes, we just need to pass the sizes through, instead of rewriting the whole code block again: 

```py
make_turtle()
square(120)
square(200)
```

A function can have as many parameters as needed:
```py
def polygon(n, length):
    ...
```

Good practice is to also name these again when calling the function:

```py
polygon( n = 3, length = 100 )
```

for a triangle, for example. 


## Refactoring

This is a related concept where functions are built off of other functions. 

Suppose we made an even more general function `polyline(...)`:

```py
def polyline(n, length, angle):
    for i in range(n):
        forward(length)
        left(angle)
```

We can then define `polygon` by passing the angle in terms of `n`:
```py 
def polygon(n, length):
    angle = 360.0 / n
    polyline(n, length, angle)
```

Similarly we can define a function `arc(...)` to draw... well, an arc, out of the `polyline(...)` function:
```py
def arc(radius, angle): # angle in degrees
    # l = r theta (angle in radians; needs conversion)
    arc_length = 2 * math.pi * radius * angle / 360 
    # Set an integer n, and split the arc into n sections
    n = 30
    length = arc_length / n
    step_angle = angle / n
    # Now call polyline
    polyline(n, length, step_angle)
```

And we can use this itself to make a `circle(...)` function:

```py
def circle(radius):
    arc(radius, 360)
```

Refactoring's usually going to happen later on rather than pre-emptively; when you notice you're repeating code blocks in different functions, make a dedicated function out of that code block!

## Development plans?
*Think Python* (Ch. 4) suggests - and then immediately states that it has drawbacks - that the procedure to encapsulation and generalisation could be done as follows: 

1 - Write a small program without function definitions;
2 - Identify coherent pieces and refactor;
3 - Generalise the function(s) by adding parameters where needed. 

Then repeat these steps. 



# References

Downey, A.B. (2012) *Think Python: How to Think Like a Computer Scientist*. 2nd edn. Sebastopol, CA: O’Reilly Media.