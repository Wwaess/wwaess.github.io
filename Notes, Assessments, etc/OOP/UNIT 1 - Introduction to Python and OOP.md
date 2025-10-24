For **UNIT 1**
# Introduction to Python (again) and the Object-Oriented Programming Philosophy

Some coding languages like C and Java are _procedural programming languages_. That is, you build a bunch of in-house functions, and then call these functions in the main() body of the program. There are limits to this:
1) You can't reuse these codes in different places, not without hardcoding additions. 
2) You can't just plug these into different applications as and when needed. 
This means writing for different uses may require rewrites of the code. 
Specific to this course, an **extra limitation** here is that it's hard to relate this code to real-world objects. 

*Object-oriented programming*, such as Python and C++, move you away from handling stuff at the bit-level and towards the object level - this makes it easier to abstract detail so as to focus on what functions need to be built to create the desired application. 

*Service-oriented software*, such as C# and Simple Object Access Protocol (SOAP), define *services* as opposed to objects. These are often complementary to object-oriented code - you first define a service at a high level, then develop the objects to map to the service, or use existing objects to build the service. 

*Component-based programming*, such as ASP.NET and Windows Forms, creates software by joining already available code snippets together. The new software has the ability to join these and add new functionality, and manage the smaller codes being able to work together. With this, a developer does not have to concern themselves with the inner workings of each component, only having to check how to plug them together. 

OOP is generally considered most supportive of developers, since they consider real-world objects, have shorter methods and have public and private properties (cf. private and public classes in C#). 

A program being "object-oriented" is a twofold definition:
1) the program is written in a language that relies on principles considering real-life objects in its design. C++ and Smalltalk are such examples. 
2) it has a certain style of writing, which is what will be discussed in this module. 



**Objects** are data structures with two core components:
1) STATES - think nouns and adjectives that describe the object; these are also referred to as data or attributes.
2) BEHAVIOURS - think verbs; these are processes to modify object states. 



OOP has FOUR core principles: 
- **Abstraction** - hide the internal workings of objects, and only show those relevant to the user
- **Encapsulation** - bundle the data and methods together
- **Inheritance** - base some objects on ancestors
- **Polymorphism** - allow objects to take many forms

