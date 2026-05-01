---
title: "Equivalence Classes"
date: 2026-03-04 00:00:00 +0000
categories: [SSDCS]
tags: [SSDCS]
---

For **UNIT 5**

# Equivalence Testing in Python

I've been given a file titled _equivalence.py_ (see SSDCS/Code). 

What it does is to take a list of objects - an "iterable" - and partition them based on whether they are deemed equivalent under an **equivalence relation** (a binary operation on two variables that outputs "T" or "F"). Two elements that are equivalent are said to be in the same **equivalence class**. 

In the code's `test_equivalence_partition()`, the equivalence relation 

```py
lambda x, y: (x - y) % 4 == 0
```

that is, the relation $xRy$, is the statement "$x \equiv y \mod 4$" to borrow from set theory. 


I note here that this is indeed a valid equivalence relation: 
- It's **reflexive**: $ xRx \iff x - x = 0 \mod 4 $ and this is true for any $x$. 
- It's **symmetric**: 
$$
\begin{align*}
    xRy & \implies x - y = 0 \mod 4 \\
        & \implies \exists k \in \mathbb {Z}: x - y = 4k \\
        & \implies \exists k \in \mathbb {Z}: y - x = 4(-k) \\
        & \implies y - x = 0 \mod 4 \\
        & \implies yRx
\end{align*}
$$
- It's **transitive**: supposing $xRy$ and $yRz$, then $zRy$ (from symmetry) and
$$
\begin{align*}
    x - y &= z - y = 0 &\mod 4 \\
    x &= z &\mod 4 \\
    x - z &= 0 &\mod 4 \\
    \text{so } & xRz.
\end{align*}
$$


The test code then runs this through the range `range(-3,5)` i.e. the integers -3 to 4 inclusive (W3Schools, n.d.) and groups elements in that range into their equivalence classes. 

As the task states, it does indeed output:

```py
{1, -3}
{2, -2}
{3, -1}
{0, 4}
-3 : {1, -3}
-2 : {2, -2}
-1 : {3, -1}
0 : {0, 4}
1 : {1, -3}
2 : {2, -2}
3 : {3, -1}
4 : {0, 4}
```

The first four lines do indeed describe the four equivalence classes in this range per this relation. 

In each subsequent line, it prints out an element from the range, followed by a colon and then the equivalence class to which that element belongs. 


Of note, this relation doesn't have to have its inputs be entirely numerical, though it does require some true/false statement. Changing the range to

`{ "Alpine", "Aston Martin", "Atlassian Williams", "Audi", "Cadillac", "Ferrari", "Haas", "McLaren", "Mercedes", "Racing Bulls", "Red Bull Racing" }`

and the equivalence relation to 

`lambda x, y : len(x) == len(y)`

the code does indeed deduce the correct equivalence classes: 

```py
{'Alpine'}
{'Racing Bulls', 'Aston Martin'}
{'Atlassian Williams'}
{'Audi', 'Haas'}
{'Mercedes', 'Cadillac'}
{'McLaren', 'Ferrari'}
{'Red Bull Racing'}
Alpine : {'Alpine'}
Aston Martin : {'Racing Bulls', 'Aston Martin'}
Atlassian Williams : {'Atlassian Williams'}
Audi : {'Audi', 'Haas'}
Cadillac : {'Mercedes', 'Cadillac'}
Ferrari : {'McLaren', 'Ferrari'}
Haas : {'Audi', 'Haas'}
McLaren : {'McLaren', 'Ferrari'}
Mercedes : {'Mercedes', 'Cadillac'}
Racing Bulls : {'Racing Bulls', 'Aston Martin'}
Red Bull Racing : {'Red Bull Racing'}
``` 

Of note, the equivalence relation does actually have to _be_ an equivalence relation. A relation like `lambda x, y : x > y` on a list of integers, which is transitive but not symmetric or reflexive, will cause an error. 

# References

W3Schools (n.d.) *Python range() Function*. Available at: https://www.w3schools.com/python/ref_func_range.asp [Accessed: 25th February 2026]. 