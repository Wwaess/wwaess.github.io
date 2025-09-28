---
title: "Cyclomatic Complexity"
date: 2025-09-27 00:00:00 +0000
categories: [OOP]
tags: [OOP]
---

# What is Cyclomatic Complexity?

Cyclomatic complexity refers to a metric developed by Thomas McCabe to measure how "complex" a program is, by counting how many decision it makes.[^1] It's slightly more involved than that, as it bascially converts the program into a directed graph called a **control flow graph** and then defines the metric as 

M = E - N + 2P

where: 
- M is the cyclomatic complexity,
- E = the number of edges in the graph,
- N = the number of nodes in the graph, and
- P = the number of _connected_ components.

If the "program" in question is just a single method (such as in this activity for this portfolio), then P = 1. So for a single subroutine the formula is `M = E - N + 2`. 

```C#
public static string IntroducePerson(string name, int age)
{
    var response = $"Hi! My name is {name} and I'm {age} years old.";

    if (age >= 18)
        response += " I'm an adult.";

    if (name.Length > 7)
        response += " I have a long name.";

    return response;
}
```

This can be converted into this graph:

[well crap, I still don't know how to add images properly here, assume the decision graph is here]

This has 11 edges and 10 nodes, so the cyclomatic complexity of this piece of code is 11 - 10 + 2 = **3**. 



# References:

[^1]: https://www.geeksforgeeks.org/dsa/cyclomatic-complexity/