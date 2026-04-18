For **UNIT 3**

```
You should read Cifuentes & Bierman (2019) and then answer the questions below, adding them as evidence to your e-portfolio.

What factors determine whether a programming language is secure or not?
Could Python be classed as a secure language? Justify your answer.
"Python would be a better language to create operating systems than C." Discuss.
```

Cifuentes and Bierman (2019) suggest that one can split a programming language vulnerability into one of *three categories*: 

- ### Buffer errors
    ...referring to an attack that exploits overloading a predefined amount of memory storage. Most common are overflowing/underflowing, which either forces the section storing an input to hold a larger number than it's designed to handle, rolling over as a result, or inputting some kind of negative number in an attempt to max out the section of code.  
- ### Injection errors
    ...which include cross-site scripting (XSS), SQL injection, code injection and even OS command injection. Loosely, these have to do with inputting data of a type that is different than what is expected, such as text when numbers are expected. As an exploit, this is often _code_ where display-able text is expected instead. 
- ### Information leak errors
    ...i.e. the release of information to an untrusted environment. 

With these in mind: 
## Could Python be classed as a secure language?
### Buffer errors?
Python is generally considered **memory-safe** (Prossimo, n.d.), meaning it doesn't 




# References

Cifuentes, C., BIerman, G. M. (2019) *What is a Secure Programming Language?* Available at: https://doi.org/10.4230/LIPIcs.SNAPL.2019.3 

Prossimo (n.d.) https://www.memorysafety.org/docs/memory-safety



