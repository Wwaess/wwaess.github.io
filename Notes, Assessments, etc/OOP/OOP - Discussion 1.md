INITIAL POST
```
### **  
Initial Post: Prioritising Factors Influencing Software Reusability**

**Padhy et al. (2018) identify twelve factors in Table 1 that influence the reusability of object-oriented software, emphasising assets beyond code. I propose a four-tier prioritisation, grouping these factors based on their impact on creating reusable, modular, and maintainable Python-based OOP systems. This framework aligns with design principles like encapsulation, inheritance, and low coupling (Chidamber & Kemerer, 1994).**

#### **Tier 1 – Foundational OO Design Properties (Highest Priority)**

**Design Patterns (DP): Reusable solutions (e.g., Factory, Decorator) enhance flexibility and cross-project adaptability (Padhy et al., 2018, p. 434).**

**Modules in the Program (MIP): Python’s modular structure (e.g., imports) promotes encapsulation and reuse by reducing interdependencies.**

**Architecture Driven Approach (ADP): A robust architecture (e.g., MVC in Django) ensures component interoperability and scalability.  
  
**

#### **Tier 2 – Structural Enablers (High Priority)**

**Inheritance: Reusability often “occurs through inheritance” (Padhy et al., 2018, p. 433). However, deep inheritance (high DIT) can hinder maintainability and performance.**

**Requirement Analysis (RA): Early design generalisation and abstraction enables future reuse (p. 435).**

**Service Contracts (SC): Well-defined interfaces (e.g., FastAPI endpoints) enable interaction and reuse across systems.  
  
**

#### **Tier 3 – Quality and Usability Factors (Medium Priority)**

**Documentation in Project (DIP): Python docstrings and type hints improve usability and reduce errors (Boehm, 1988).**

**Test Cases/Test Design (TCTD): Reusable test suites (e.g., pytest) strengthen quality assurance and prevent regressions.**

**Algorithms Used in the Program (AP): Reusable algorithmic components can be encapsulated as classes or functions.  
  
**

#### **Tier 4 – Supporting Factors (Lower Priority)**

**Models in the Project (MP): UML and diagrams are helpful but less actionable than code-level reuse.**

**Knowledge Requirement (KR): Tacit knowledge supports reuse but lacks automation and consistency.**

**Planning Stage (PS): Indirectly facilitates reuse through better project structuring.**

**Used Data (UD): Context-specific; valuable in data-centric systems, less so in general OOP.**

This prioritisation reflects Padhy et al.’s (2018) emphasis on “frequently researched reusable assets” (Figure 3, p. 435) and aligns with Python’s strengths in dynamic typing, modularity, and design flexibility. While priorities may shift in specific contexts (e.g. real-time or legacy systems), this structure ensures a solid foundation for reusability in Python OOP projects.

---

References  
Boehm, B.W. (1988) ‘A spiral model of software development and enhancement’, Computer, 21(5), pp. 61–72.  
Chidamber, S.R. and Kemerer, C.F. (1994) ‘A metrics suite for object-oriented design’, IEEE Transactions on Software Engineering, 20(6), pp. 476–493.  
Padhy, N., Satapathy, S. and Singh, R.P. (2018) State-of-the-Art Object-Oriented Metrics and Its Reusability: A Decade Review. In: Satapathy, S.C., Bhateja, V. and Das, S. (eds.) Smart Computing and Informatics. Springer, Singapore, pp. 431–441. [https://doi.org/10.1007/978-981-10-5544-7_42](https://doi.org/10.1007/978-981-10-5544-7_42)
```


__Initial Post: Prioritising Software Reusability Factors__

Unlike procedural programming, which relies on writing methods that perform operations on given data inputs, object-oriented programming (OOP) focuses on interactions between collections of data and methods called _objects_ (W3Schools, n.d.). To this extent, the aim for OOP is to keep repetition of code to a minimum, which generally makes software more efficient due to there being less to compute. 

Padhy et al. (2018: Table 1) explores a dozen factors that contribute towards code reusability, which I'll attempt to categorise by priority, taking inspiration from Ahmaro et al (2014). 

**Tier 1 - Foundational Factors**
i.e. Architecture-driven approaches, design patterns and requirement analyses. 
These set the **direction and structure** for the design and composition of the software. ADP ensures the structure can be easily scaled up, DP allows for enhanced maintainability, and RA makes sure that the software(s) that is/are designed is/are built to meet the specification (Efendi, 2024). 

**Tier 2 - Implementation-Level Factors**
i.e. Modules in the program, documentations in the project, service contracts and test case suites. 
These not only make reusing the code practical, but also minimises the friction that would otherwise be caused by inconsistencies. MIP and TCTD enable new implementations to be added with minimal disruption and be tested efficiently, while DIP and SC provide clarity to software development teams. 

**Tier 3 - Contextual Factors**
i.e. whatever data is used (UD), program algorithms, knowledge requirements and models in the project. 
While important for the specific design specifications, these are less transferable and thus take less priority as a classification of *reusability*. Their applicability is often limited to similar domains or problem contexts, and they may require significant adaptation before reuse is possible. As such, they are best leveraged once foundational and implementation-level factors are mature, ensuring that the effort invested in adapting them yields meaningful returns (Ahmaro et al., 2014; Padhy et al., 2021). 

**References:**
Efendi, F. (2024) *Understanding Design Patterns: Definition, Purpose, and Benefits*. Available at: https://softwarepatternslexicon.com/mastering-design-patterns/1/1/
Ibraheem Y.Y. Ahmaro, Abdallah M. Abualkishik and Mohd Zaliman Mohd Yusoff (2014) *Taxonomy, Definition, Approaches, Benefits, Reusability Levels, Factors and Adaption of Software Reusability: A Review of the Research Literature* Available at: https://scialert.net/fulltext/?doi=jas.2014.2396.2421
Padhy, N., Satapathy, S. and Singh, R.P. (2018) *State-of-the-Art Object-Oriented Metrics and Its Reusability: A Decade Review*. Available at: https://doi.org/10.1007/978-981-10-5544-7_42
W3Schools (n.d.) *Java OOP (Object-Oriented Programming)*. Available at: https://www.w3schools.com/java/java_oop.asp

Architecture-driven approach (ADP) [the overall structure of the project/component]
Design patterns (DP) [Reuse the whole design if the same requirement occurs]
Requirement Analysis (RA) [Gathering info on what the system must do]

Modules in the Program (MIP) [collections of instructions as .dll files that are typically called once]
Documentation in Project (DIP) [Written guides and manuals]
Service Contracts (SC) [Agreements/interfaces between the developers and users]
Test cases / test design (TCTD) [the test case suite, which can be reused for different versions of the same software]

Used in the Data (UD)[reaccessing data]
Program algorithms (AP) [reusable algorithms if the same problem occurs in the pic - software design]
Knowledge Requirement (KR) [The know0how gained during the software development]
Models in the Project (MP) [Diagrams or abstractions of the system (UML etc.)]







Used in the Data (UD)[reaccessing data]
Modules in the Program (MIP) [collections of instructions as .dll files that are typically called once]
Architecture-driven approach (ADP) [the overall structure of the project/component]
Program algorithms (AP) [reusable algorithms if the same problem occurs in the pic - software design]
Design patterns (DP) [Reuse the whole design if the same requirement occurs]
Documentation in Project (DIP) [Written guides and manuals]
Knowledge Requirement (KR) [The know0how gained during the software development]
Models in the Project (MP) [Diagrams or abstractions of the system (UML etc.)]
Requirement Analysis (RA) [Gathering info on what the system must do]
Service Contracts (SC) [Agreements/interfaces between the developers and users]
Test cases / test design (TCTD) [the test case suite, which can be reused for different versions of the same software]