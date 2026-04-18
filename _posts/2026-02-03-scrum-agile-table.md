---
title: "The Scrum Agile SDLC"
date: 2025-02-01 00:00:00 +0000
categories: [SSDCS]
tags: [SSDCS]
---

For **Unit 2**

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