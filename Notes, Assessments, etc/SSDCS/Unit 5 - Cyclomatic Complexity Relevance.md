For **Unit 5**

``` 
The Cyclomatic Complexity is commonly considered in modules on testing the validity of code design today. However, in your opinion, should it be? Does it remain relevant today? Specific to the focus of this module, is it relevant in our quest to develop secure software? 
``` 

Cyclomatic complexity is a metric used to measure the "complexity" of a program, specifically by counting the number of decisions it makes[^1]. By drawing a connected graph - a **control flow graph** - from the program in question, the metric is defined as 

$M = E - N + 2P$

where: 
- $M =$ the cyclomatic complexity,
- $E =$ the number of edges in the graph,
- $N =$ the number of nodes in the graph, and
- $P =$ the number of _connected_ components.

In practice, this $M$ is representative of the amount of independent execution paths the code has to go through to run successfully - the higher the complexity, the more involved the code is, and the greater the risk of poor maintenance. 

In theory, having this as a metric is useful for the testing phase of software development: with a concrete number of independent path executions calculated, each path can be checked at least once, ensuring nothing's been overlooked. Furthermore, if the cyclomatic complexity is too high, it can serve as a warning sign that the code may be too convoluted, making it harder to test, debug, and maintain effectively.

# References
[^1]: https://www.geeksforgeeks.org/dsa/cyclomatic-complexity/