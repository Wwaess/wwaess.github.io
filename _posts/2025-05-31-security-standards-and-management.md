---
title: "Security Standards and Frameworks"
date: 2025-05-31 00:00:00 +0000
categories: [ISM]
tags: [ISM]
---

# Security Standards and Frameworks

Kirvan (2023) refers to *twelve* (not *ten*) IT security frameworks/standards - collections of regulations and otherwise conventions that should be adhered to whenever applicable, either by law (regulation) or for cross-comparability/compatibility (convention). 

For each of three organisation types, I'll state which frameworks would apply and the tests/recommendations I'd suggest for the organisation to use them / to comply with standards. 

| **Organisation**               | **Framework** | **Why It Applies**                                                        | **Key Tests & Recommendations**                                                                        |
| ------------------------------ | ------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **International Bank**         | ISO 27001     | Global standard for ISMS                                                  | Conduct ISMS analysis, prepare for certification audits.                                               |
|                                | NIST CSF      | Risk-based framework suited to critical financial infrastructure          | Assess maturity tier; build roadmap.                                                                   |
|                                | CIS Controls  | Prioritised best practices for cybersecurity hygiene                      | Check secure configs, MFA, endpoint security; test regularly.                                          |
|                                | PCI-DSS       | Handling card payments                                                    | Annual audits, encryption, run regular vulnerability scans.                                            |
|                                | COBIT         | Aligns IT governance with strategic business goals                        | Maturity models to evaluate governance; improve processes for risk                                     |
|                                | GDPR          | For processing EU citizens’ personal data                                 | Check lawful processing basis, prepare for access-and-breach response.                                 |
|                                |               |                                                                           |                                                                                                        |
| **Large Hospital**             | HIPAA         | For protecting U.S. patient health info (if US patients are there)        | Risk assessments, encrypt data, train staff, review breach response plans.                             |
|                                | ISO 27001     | Global standard for ISMS                                                  | Define ISMS for PHI/PII, run internal audits, manage access and incident response procedures.          |
|                                | NIST CSF      | Structured approach to managing cyber risk in critical services           | Align with CSF functions (Identify–Recover); do risk mapping and tabletop exercises.                   |
|                                | HITRUST CSF   | Certifiable framework combining HIPAA, NIST, ISO etc.                     | Assess using MyCSF tool, identify gaps, implement controls, prepare for external validation.           |
|                                | GDPR          | Required if processing EU patients’ data                                  | Ensure consent, maintain privacy notices, assess cross-border data transfers, enable rights access.    |
|                                |               |                                                                           |                                                                                                        |
| **Food Manufacturing Factory** | ISO 27001     | Global standard for ISMS                                                  | Implement ISMS, assess risks to industrial processes, train key staff.                                 |
|                                | NIST CSF      | Risk-based framework suited to critical financial infrastructure          | Assess response capability; test resilience planning.                                                  |
|                                | COBIT         | Ensures business–IT alignment in tech and automation systems              | Evaluate IT governance; define roles/responsibilities; document policies for procurement and vendors.  |
|                                | NIS 2         | Applies if considered essential to EU critical food supply infrastructure | Identify security gaps, implement incident reporting procedures, test supply chain risk protocols.     |
|                                | GDPR          | Applies if handling EU employee or customer personal data                 | Audit personal data uses, document legal basis, enable data subject rights, and ensure secure storage. |

## References
Kirvan, P. (2021). Top 12 IT security frameworks and standards explained. TechTarget SearchSecurity. Available at: https://www.techtarget.com/searchsecurity/tip/IT-security frameworks-and-standards-Choosing-the-right-one (Accessed: 24 May 2025).