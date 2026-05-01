For **Unit 8**
Discussion
```
TrueCrypt was a popular and well-respected operating system add-on that could create encrypted volumes on a Windows and/or Linux system. In addition, it was also designed to create a complete, bootable volume that could encrypt the entire operating system and data for a Windows XP system. It was discontinued in 2014 and a variation VeraCrypt has been developed.

Case Study: Read the article by Tan et al (2020) (link is in the reading list), and complete further research if necessary, then answer the following question:
```

Tan, Zhang and Bao's (2020) paper on "A Deep Exploration of BitLocker Encryption and Security Analysis" explores the function of the keys and recovery systems of Microsoft BitLocker's encryption software, including potential vulnerabilities. It notes that BitLocker relies on an Advanced Encryption Standard (AES) with either CBC (cipher block chaining, which is where how a block of data is encrypted depends on the previous one's encryption) (Portnox, 2026) or XTS (more disk specific and uses two keys instead of one?) (Xilinx, 2019). 

There are two key layers: 
- **Full Volume Encyption Key (FVEK)** - which encrypts disk sectors, and
- **Volume Master Key (VMK)** - which encrypts the FVEK itself (protected by a password or similar). 

Strengths: 
- Hardware-based protection (via TPM)
- Integrates w/ Windows authentication
- Resists offline attacks well (i.e. gaining physical access doesn't necesarily mean compromise)

Weaknesses:
- Cold-boot attacks (recovering keys from the RAM)
- Physical access can be bypassed if there's no TPM in use
- Insecure key storage might expose data
- Windows-only

```
Would you be prepared to recommend BitLocker or VeraCrypt to a friend as a secure storage environment? What caveats (if any) would you add?
Present an ontology design which captures the weaknesses of VeraCrypt, and organise them according to their severity. Expand the ontology design by considering the factors which will cause each weakness to become an issue from a user's perspective. For example, if a user wishes to encrypt a disk storing bank details using VeraCrypt, which weakness of the software might cause this specific user goal to be negatively impacted?
``` 

The article by Tan, Zhang and Bao (2020) examines BitLocker's internal design and how Windows uses a layered key hierarchy (VMK on top of FVEK), AES-based encryption modes and TPM integration to protect data when a computer is not in use. The authors suggest it is generally robust when well configured, but the system itself still requires physical security and good key-management practices. 

For recommending a secure storage environment to a friend, for most people I'd suggest BitLocker. As it's built directly into Windows, the configuration decisions aren't complex and the seamless integration reduces the likelihood of user error - a common source of security failure. To this end, if someone's goal is just to have their laptop data encrypted, without any need to understand bootloader behaviour or cipher modes, BitLocker should be sufficient. 

On the other hand, VeraCrypt may be the better choice in more specialised scenarios. It's open-source, employs hidden volumes, a variety of hash functions for key deviation, and multi-iteration hashing (Tam et al., 2020) - and while those are very useful, they introduce complexity for the user, which impacts psychological acceptability, one of Saltzer's and Schroeder's principles (No Complexity, 2026). While an independent audit highlights VeraCrypt's security, it also notes that misconfiguration is a realistic risk for non-technical users (OSTIF, 2016). 

Below is an ontology of VeraCrypt's weaknesses in order of severity: 
- **High severity** 
    - key management risks, e.g. poor passwords
    - no hardware-bound key protection, which would allow for coldbooting
- **Medium severity** 
    - usability conplexity, from misconfigured or incorrect encryption settings
    - compatibility issues (e.g. with the OS and conflicts with UEFI/Secure Boot)
- **Low severity**
    - Possible slowdowns from cascaded algorithms (such as from its key hashing)

If a user wished to store bank details in a drive to be encrypted, these weaknesses become serious problems if mishandled. If they choose a weak password, their account could be compromised; if their header backup is misplaced, they could lose access to their bank details altogether. For these reasons, VeraScrypt ideally should be recommended only to those who can manage the technical requirements involved. 

References
---
Portnox (2026) *What is Cipher Block Chaining?* Available at: https://www.portnox.com/cybersecurity-101/general-security/what-is-cipher-block-chaining/
https://xilinx.github.io/Vitis_Libraries/security/2019.2/guide_L1/internals/xts.html

No Complexity (2026) *Saltzer and Schroeder's design principles*. Available at: https://nocomplexity.com/documents/securityarchitecture/architecture/saltzer_designprinciples.html
OSTIF (2016) *The VeraCrypt Audit Results*. Available at: https://ostif.org/the-veracrypt-audit-results/

Tan, C., Zhang, L., Bao, L. (2020) *A deep exploration of BitLocker encryption and security analysis*, IEEE. Available at: https://ieeexplore-ieee-org.uniessexlib.idm.oclc.org/document/9295908/