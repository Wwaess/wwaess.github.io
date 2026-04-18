# Question 1: "Table"

```
Create a 2-column multi-line table. In the left-hand column, include the software development stages of the Scrum agile life cycle approach to project management. In the right-hand column, describe the processes which you recommend are applied at each stage to ensure that secure software is produced at the end of the development. To support the preparation of your response, you can refer to the following literature:

Sharma, A. & Bawa, R. K. (2020) Identification and Integration of Security Activities for Secure Agile Development. International Journal of Information Technology.
```

Sources appear to vary slightly on what specifically constitute the phases of the Scrum Agile project management framework. I've taken Donato's (2026) list as reference. 

| Software Development Stage | Recommended process(es) to apply |
|-|-|
| Initiation Phase | Identify CIA (confidentiality / integrity / availability) requirements; initial threat modelling; assess security failure impact|
| Planning & Estimates Phase | Outline what security actions are needed to be implemented; prioritise them based on risk; update Definitions-of-Done (DoD) |
| Implementation Phase | Enact security actions, applying secure coding standards e.g. OWASP; Static Application Security Testing (SAST); review peer code; scan 3rd-party libraries for known vulnerabilities | 
| Review & Retrospective Phase | Security testing; run a vulnerability assessment |
| Release Phase | Release security audit; run some penetration testing if possible; config+deploy securely |

# Question 2: "Blog Post"

```
Some say that people are the biggest risk of cyber security.

Select five terms from ISO/IEC Standard 27000 Section 3 Terms and Definitions and write a 300-word blog post on how people can be managed to overcome cyber security attacks from the inside.
```

The ISO/IEC Standard 27000:2018 defines an **attack** as any "attempt to destroy, expose, alter, disable, steal or gain unauthorised access" into a system. To this end, no matter how _(literally) technically_ secure a system or network may be, since there typically are people who need to access them, if those people can be exploited then they'll serve as the system's weakpoints a vast majority of the time. 

Certain people will need access to certain tools in the system depending on business and security requirements; management of such access is, unsurprisingly, called **access control**. Acess must be restricted as much as necessary and be kept updated on a regular basis, so as to mitigate the amount of damage an insider - accidentally or deliberately - may cause. 

Beyond that, human behaviour itself introduces **risk**, or an "effect of uncertainty on objectives" (ISO/IEC, 2018). Employees make mistakes or take shortcuts, or have to respond to social pressures such as time constraints or perceived urgency. Effective security management should plan for such issues and have safeguards, or **controls**, in place accordingly, such as multifactor authentification, enforced security policies and logging systems, so that human error - or indeed malicious insider action - doesn't immediately translate into a fully compromised network. 

Some failures are inevitable and they should be managed swiftly when possible; when it's over, the **event** should be logged and treated as an **incident** (McGoffin, Proctor and Zuber, 2024), whereby focus should be placed not on attributing blame on anyone, but on identifying the systemic weakpoints that led to the incident without discouraging those involved from giving honest reports. 

# References

ISO/IEC (2018) *Information technology — Security techniques — Information security management systems — Overview and vocabulary*. Available at: https://www.mn.uio.no/ifi/forskning/grupper/sec/sikkerhetsledelse/iso_iec_27000_2018.pdf [Accessed: 7th February 2026]

McGoffin, T., Proctor, J., Zuber, R. (2024) *The value of blameless culture — from IC to C-Suite*. Available at: https://circleci.com/blog/value-of-blameless-culture/ [Accessed: 8th February 2026]


Donato, H. (2026) *What Are The Phases Of Scrum?* Available at: https://www.workamajig.com/blog/scrum-methodology-guide/scrum-phases [Accessed: 29th January 2026]. 

