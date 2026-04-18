For **Unit 1**
Discussion

OWASP (2025), the Open Worldwide Application Security Project, is an online group that publishes open-source information on software and application security. They frequently publish the OWASP Top 10, a "standard awareness document for developers" which lists the 10 "most critical security risks to web applications". 

The A05:2025, "Injection", refers to an application flaw where a user's input is insufficiently filtered and can be (knowingly or otherwise) sent to an interpreter that may execute parts of that input as code - often in SQL or JavaScript, though the specific language depends on where the input is validated in the program.  

The following UML diagram, created via Sequence Diagram, is a flowchart depicting the steps that may cause unsanitised inputs to execute as code, resulting in the OWASP AO5: Injection (2025) vulnerability: 

![UML Sequence Diagram - demonstrating how code injection works](<OWASP A05 Injection - UML Sequence Diagram.png>)

I've chosen a sequence diagram (GeeksforGeeks, 2026) for this to show the steps through which the user input flows through the system, where validation should occur (before returning the unvalidated input) and where unsafe behaviour - such as a SQL injection - can be introduced to the system. This highlights clearly where a developer should add the necessary controls to mitigate against the AO3: Injection vulnerability. 



References:
GeeksforGeeks (2026) Unified Modeling Language (UML) Diagrams. Available at: https://www.geeksforgeeks.org/system-design/unified-modeling-language-uml-introduction/
OWASP (2025) A05 Injection - OWASP Top 10:2025. Available at: https://owasp.org/Top10/2025/A05_2025-Injection/