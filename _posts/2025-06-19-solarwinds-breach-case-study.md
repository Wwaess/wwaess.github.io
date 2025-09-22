---
title: "The Solar Winds Breach - a case study"
date: 2025-06-19 00:00:00 +0000
categories: [NS]
tags: [NS]
---

# Cyber Kill Chain exploit analysis
...on the SolarWinds attack, 2020. 

|PHASE|INDICATORS|MITIGATION?|TOOLS to use to combat threat?|
|RECONNAISSANCE|Researched infrastructure + supply chain|Monitor for suspicious domain lookups? **esp. from newly discovered end users**|Threat intelligence platforms to find signs of attacker interests|
|WEAPONISATION|SUNBURST malware, embedded as a .dll file into Orion software|Stricter code reviews; **static+dynamic code analysis tools (bc. some code might be humanly invisible)**|Static code analysis software to find unusual patterns, used before sending updates|
|DELIVERY|Trojan virus, delivered as a “security” update|Verify software update integrity|
|EXPLOITATION|SUNBURST activated after a delay, post-update|Endpoint (end user) protection, behaviour analytics; **check events called if they’re high-risk**|Digital signature tools, to check authenticity|Endpoint Detection + Response (EDR) tools, to spot abnormal activity on endpoints (end users)|
|INSTALLATION|Backdoor created, established persistence|Application scanning; **centralised network updates (e.g. virtualised system as a mini-updater cf. MS)**|Some installer-checking software? Confirm the application being made is legitimate|
|COMMAND AND CONTROL|Sent data to attackers’ servers, the traffic messages disguised as update checks|Screen outbound network traffic for anomalous requests|Some network screening software? To verify whether the “update checks” are needed/real|
|ACTIONS ON OBJECTIVES|Data exfiltration, credential theft|Zero-trust models, privileged access controls **(e.g. one session for one user, at a time)**|...|


## Notes made during seminar
Less information on website; stricter password management; a fuller zero-trust model employed site-wide; threat protection tools e.g. on firewalls and servers
This table has limitations – it’s missing some steps to consider e.g. MFA bypassing; it’s also too linear (cf. ethical hacking methodologies – dynamically jumping from phases as and when relevant)
Honeypots may help trap *some* hackers – but someone might notice where the honeypots *are*. Consider other facets of defence
