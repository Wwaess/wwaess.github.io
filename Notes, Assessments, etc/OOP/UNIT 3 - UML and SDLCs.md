For **UNIT 3**
# What is an SDLC?

A **software development life cycle (SDLC)** refers to a process used by development teams when designing and building software of a high quality [^1]. 

While these vary from team to team, they can generally be outlined in 6 steps [^1]: 
- **Plan** - deduce costs, timeframes, resource management and work allocation. This typically involves making a dedicated document. 
- **Design** - analyse requirements and determine a solution to create the desired software, along with how best to integrate it with whatever software the client organisation already uses. 
- **Implement** - write the code. 
- **Test** - check the software for bugs, either manually or by automating tests. If there are many teams working on the code, this often happens in tandem with the implementation phase. 
- **Deploy** - send this code out as its own _copy_ - allowing users already using an existing version to continue using it while updates are made. 
- **Maintain** - fix bugs and resolve further issues as and when they arise. 

# Where do UMLs fit into this?

**Unified modelling languages (UMLs)** are general-purpose languages for modelling how a system should operate. It's more of a visual aid than a proper programming language, and while there are *some* standards[^2], they come in a variety of flavours. 

The core point of them is to show how a system is structured, how it behaves, and to provide a rough outline to guide a team on what is and isn't implemented into the system. 

Oh, and it's for showing off to non-techy shareholders about what your code does, without having to show the code itself. [It's more involved than that, but this is the funnier explanation for this point :D]

UMLs are generally going to be needed in the planning phases to help define what key functions the client organisation's system must be able to do. For obvious reasons, the design phases also need to make heavy use of UMLs, since they... well, _contain the designs_. 
UMLs can also be used for the testing phases wherein case diagrams and sequence diagrams can demonstrate example test cases. If the system passes these, we can confirm whether the sepcification requirements have been met. 

<!-- Outside of these phases, these diagrams aren't really directly involved. While they're a component of the implementation phase because they came from the previous stages, I'm not going to claim that UMLs are "applicable" at this stage of an SDLC only for the same reason that a map for a treasure -->

<!-- TODO: 
- Check TYPES of UML diagrams to deduce where to put which type in different SDLC stages
-->


# References
[^1]: https://aws.amazon.com/what-is/sdlc
[^2]: https://www.iso.org/standard/52854.html