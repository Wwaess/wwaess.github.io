For **Unit 10**

```
Read Schmitz et al (2016) article about faceted data.

Do you think this is a good approach to protect systems from data leakage? What are the pros and cons?
Create a basic outline design of how you would create such a system in Python. 
```
Some context - I could not confirm with certainty what article "Schmitz et al (2016) refers to; I've linked the article I *believe* is the intended article in the references section. 

Schmitz et al. (2016) proposes an information-flow control mechanism called _faceted values_. Such a value has _many_ views of the same data, such as a a private and public "facet", and which one is displayed depends on the privileges of the user who's accessing the value. The idea is to generalise the confidentiality rule of least privilege (No Security, 2026), whereby high-ranking users should see a _truer_ value, while low-ranking users should see a protected default. 

Earlier work introduced faceted values in an untyped λ-calculus (small models of a programming language that use just variables and functions), but this paper aims to use them in Haskell without runtime modification, by means of a library (as opposed to an extension). To do this, the system uses two "monads" (wrappers that carry extra information and enforce certain logical rules and computation procedures): 
- a **faceted monad** - which tracks _explicit_ flows in pure computations; 
- an **FIO monad** - which tracks _implicit_ flows in effectful computations (think I/O and code branching). 

The library provides faceted versions of _pure values_, _mutable reference cells_ (which they call "FioRef"), and _file/socket handles_ (similarly, "FHandle"). With these, the authors formally prove that the system can be written so that public outputs don't depend on private inputs (even if there are errors in the code). 


## Pros
- **Strong confidentiality guarantees** - by construction, public outputs don't depend on private inputs, and this is proven in the paper 
- **Explicit/Implicit flows distinctly handled** - due to the two different monads
- **No runtime modification needed** - because this is written as a library for Haskell, not an extension or compiler
- **Consistent views for different observers** - while higher-privilege users can see the "true" behaviour of the program, lower-privilege ones can still interact with a sanitised (if not "redacted") view of the data that the program handles. 

## Cons
- **Performance overload** - since faceted values can nest and branch which can increase the no. of code executions; that can be costly in a large system
- **Psychological complexity** (No Complexity, 2026) - as good implementation requires that developers understand well what monads and faceted structures are. Debugging can be more difficult because the behaviour is observer-role-dependent
- **Haskell only?** - Haskell is conceptually quite close to a λ-calculus, which is why the "translation" into Haskell works rather well. While in theory you could port the same guarantees into something like Python or C++, it might be more fragile in practice. 
- **I/O boundary problems?** - real-world hardware won't understand a _facet_ per se: they can't exactly accept more than one value at the same time. The security from this library relies on policies at these boundaries being properly enforced, so any mistakes here could compromise the system. 

In all, while it's a good _approach_ for protecting logical data leakage in code for an application, it's not that well suited as a drop-in "simply add" solution for entire production systems without carfeul engineering and performance trade-offs. 

See [here](<code snippets/faceted_data.py>) for an attempt to provide a similar function in Python. This should output: 
```
Low observer sees: True
High observer sees: False
```



References:
---
No Complexity (2026) **Saltzer and Schroeder's design principles**. Available at: https://nocomplexity.com/documents/securityarchitecture/architecture/saltzer_designprinciples.html
Schmitz, T., Rhodes, D., Austin, T. H., Knowles, K., Flanagan, C. (n.d.)  **Faceted Dynamic Information Flow via Control and Data Monads**. Available at: https://users.soe.ucsc.edu/~cormac/papers/16post.pdf
Wadler, P. (n.d.) **Monads for functional programming**. Available at: https://homepages.inf.ed.ac.uk/wadler/papers/marktoberdorf/baastad.pdf