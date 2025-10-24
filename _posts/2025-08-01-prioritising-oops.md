---
title: "OPP Software Reusability"
date: 2025-08-01 00:00:00 +0000
categories: [OOP]
tags: [OOP]
---

For **DISCUSSION 1**
# Prioritising Software Reusability Factors

Unlike procedural programming, which relies on writing methods that perform operations on given data inputs, object-oriented programming (OOP) focuses on interactions between collections of data and methods called objects (W3Schools, n.d.). To this extent, the aim for OOP is to keep repetition of code to a minimum, which generally makes software more efficient due to there being less to compute.

Padhy et al. (2018: Table 1) explores a dozen factors that contribute towards code reusability, which I'll attempt to categorise by priority, taking inspiration from the paper itself and from Ahmaro et al (2014).

## Tier 1 - Foundational Factors
i.e. Architecture-driven approaches, design patterns and requirement analyses.
These set the direction and structure for the design and composition of the software. ADP ensures the structure can be easily scaled up, DP allows for enhanced maintainability, and RA makes sure that the software(s) that is/are designed is/are built to meet the specification (Efendi, 2024).

## Tier 2 - Implementation-Level Factors
i.e. Modules in the program, documentations in the project, service contracts and test case suites.
These not only make reusing the code practical, but also minimises the friction that would otherwise be caused by inconsistencies. MIP and TCTD enable new implementations to be added with minimal disruption and be tested efficiently, while DIP and SC provide clarity to software development teams.

## Tier 3 - Contextual Factors
i.e. whatever data is used (UD), program algorithms, knowledge requirements and models in the project.
While important for the specific design specifications, these are less transferable and thus take less priority as a classification of reusability. Their applicability is often limited to similar domains or problem contexts, and they may require significant adaptation before reuse is possible. As such, they are best leveraged once foundational and implementation-level factors are mature, ensuring that the effort invested in adapting them yields meaningful returns (Ahmaro et al., 2014; Padhy et al., 2021).



#### References:
Efendi, F. (2024) Understanding Design Patterns: Definition, Purpose, and Benefits. Available at: https://softwarepatternslexicon.com/mastering-design-patterns/1/1/
Ibraheem Y.Y. Ahmaro, Abdallah M. Abualkishik and Mohd Zaliman Mohd Yusoff (2014) Taxonomy, Definition, Approaches, Benefits, Reusability Levels, Factors and Adaption of Software Reusability: A Review of the Research Literature. Available at: https://scialert.net/fulltext/?doi=jas.2014.2396.2421
Padhy, N., Satapathy, S. and Singh, R.P. (2018) State-of-the-Art Object-Oriented Metrics and Its Reusability: A Decade Review. Available at: https://doi.org/10.1007/978-981-10-5544-7_42
W3Schools (n.d.) Java OOP (Object-Oriented Programming). Available at: https://www.w3schools.com/java/java_oop.asp
