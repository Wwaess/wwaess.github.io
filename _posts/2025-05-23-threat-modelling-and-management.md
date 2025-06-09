---
title: "Threat Modelling and Management"
date: 2025-05-23 00:00:00 +0000
categories: [ISM]
tags: [ISM]
---

# Threat Modelling and Management

The following work is an assessment on a fictional business called Pampered Pets, a bricks-and-mortar pet food shop planning on digitalisation. Specifically this is on some regulation standards and whether they meet them. 


| Standard | Does this apply to Pampered Pets here? | Why?                                                                                                                                                                                                                                                                                                                     |
| -------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GDPR     | Yes                                    | Especially the UK GDPR - "Hashington-on-the-Water" though fictional sounds like it is an English town, so UK laws apply; as it's handling personal data (e.g. customer details, transactions, emails, etc), the "UK GDPR" i.e. the Data Protection Act 2018 in particular applies from 31st Dec. 2020 (DLA Piper, 2019). |
| PCI-DSS  | Yes?                                   | Pampered Pets currently only processes in-person payments. Nothing is mentioned about card payments - though if customers do pay by card and the card payments are stored digitally even in-store, then PCI-DSS could apply.                                                                                             |
| HIPAA    | No                                     | HIPAA is a US set of regulations about human patient health data. Pampered Pets is (likely) based in the UK, and sells pet food (which wouldn't be covered under HIPAA anyway).                                                                                                                                          |


Evaluation against GDPR:
- Lawfulness, Fairness and Transparency:
	- Unclear: no privacy policy mentioned especially for email orders or sales data
- Purpose Limitation
	- Compliant: data is collected only for order fulfilment
- Data Minimisation
	- Compliant: the only data collected are clients' names and email  addresses
- Accuracy
	- Mostly compliant: Relies on data given by the clients. Might not be a huge issue if for short-term purchases
- Storage Limitation
	- Unclear: email inboxes may be holding data indefinitely - as there is no privacy policy mentioned, unknown whether old emails are being kept
- Integrity and Confidentiality
	- Not compliant: wireless network is shared between personal and business devices; outdated computer is in use; no mention of encryption and other security measures
- Accountability
	- Unclear: no formal documentation, such as aforementioned privacy policy, available for review

Evaluation against DCI-PSS:
- The only device relevant from the brief is a POS payment device - though it's unclear whether Pampered Pets actually has one. 
	- There are also physical access items for onsite personnel that need to be checked - such as keys, access cards and name tags
- This POS device needs to be frequently audited to ensure it is not tampered with. Otherwise compliant. 

Recommendations to meet standards: 
- Create and clearly display a privacy policy (e.g. as a poster in-store, in email correspondences), including what data is collected, for how long, and by whom
- Implement data retention policies like deleting old emails (e.g. after a year) - this could be automated, but should still be explicitly written up
- Train staff on these policies
- Update security protection measures:
	- Replace the outdated warehouse computer (also, install antivirus software and use admin privileges)
	- Set up separate networks for work devices and personal devices

Assumptions made here:
- That Pampered Pets does not sell online at the moment - so there's no e-commerce data to consider. 
- That Pampered Pets is based in the UK (so EU GDPR before Dec 2020 and the Data Protection Act 2018 are applicable). 
- That card payments are made in-store (unclear from the brief whether these are made/stored digitally). 
- That emails for pick-up orders contain minimal personal information, and just the information about what people want to buy
- That the staff have had no or insufficient IT training