# Confidentiality, Integrity & Availability (CIA) Triad

## 📝 Definition

The **CIA Triad** is the foundational model for information security, representing the three core principles essential to protecting data and systems:
- **Confidentiality**: Ensuring information is accessible only to authorized users and processes, **preventing unauthorized disclosure**.
- **Integrity**: Guaranteeing the accuracy, consistency, and trustworthiness of data over its lifecycle; **preventing unauthorized modification or corruption**.
- **Availability**: Ensuring that information and critical systems are **accessible and operational when needed** by **authorized users**.

As defined by the **National Institute of Standards and Technology (NIST)** in **[Special Publication 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)**, these principles guide the implementation of security controls and risk management strategies.

---

## ❗ Why It Matters

In cybersecurity operations, failing to uphold any component of the CIA triad leads to **operational risk** and **potential business impact**:
- **Breaches of Confidentiality** can cause data leaks, intellectual property loss, and regulatory non-compliance (e.g., GDPR, HIPAA).
- **Violations of Integrity** can undermine decision-making and trust in systems, causing corrupted transactions or fraudulent activity.
- **Compromises in Availability** result in downtime, impacting business continuity and potentially causing severe financial and reputational damage (e.g., denial-of-service attacks).

The triad forms the basis of designing **secure architectures**, **incident response strategies**, and **compliance frameworks**.

---

## ⚙️ How It Works / Key Components

- **Confidentiality controls**: Access control mechanisms such as **RBAC (Role-Based Access Control)** and attribute-based models, encryption standards like **AES (Advanced Encryption Standard)** for data at rest and **TLS (Transport Layer Security)** for data in transit, plus data classification schemes. 
- **Integrity controls**: Use of cryptographic hashes from the **SHA-2** family, digital signatures, checksums, and version control. Integrity validation is critical in environments vulnerable to software supply chain risks or insider threats. 
- **Availability controls**: Redundancy methods including failover systems and disk arrays, backup and disaster recovery plans, network resilience technologies such as protection against Distributed Denial of Service (DDoS) attacks and load balancers, and monitoring tools like **SIEM (Security Information and Event Management)** for real-time incident detection. 

Together, these controls must align with standards such as [ISO/IEC 27001](https://www.iso.org/standard/27001), [NIST Cybersecurity Framework (CSF)](https://www.nist.gov/cyberframework), etc.

---

## 🔍 Real-World Examples

In the **November 2023 Holding Slovenske elektrarne** ransomware attack, attackers compromised the availability of critical energy infrastructure by encrypting systems and demanding ransom. This not only disrupted operations but also threatened integrity, as tampered data could mislead grid management systems. The incident underscored the importance of:
- **Robust backup** strategies and offline recovery points (to restore availability).
- **Strict access controls** and network segmentation (to preserve confidentiality and limit attacker lateral movement).
- **Integrity monitoring** (to detect unauthorized file changes before system restoration).

This case also highlighted the need for incident response plans to quickly restore availability while ensuring integrity and confidentiality during recovery.

---

## ⚠️ Challenges / Common Pitfalls

- Overemphasis on one component (e.g., availability) at the expense of confidentiality or integrity, leading to imbalanced risk exposure.
- Misconfiguration of access controls, such as excessive permissions or failure to revoke access, undermining confidentiality.
- Lack of encryption for sensitive data, increasing exposure to breaches.
- Insufficient backup testing or recovery plans, resulting in extended downtime and data loss when incidents occur.
- Failure to monitor integrity continuously, which delays detection of data tampering or malware infections.
- Underestimating advanced threats (e.g., supply chain attacks, insider threats) that simultaneously target all three triad aspects.

---

[🔝 Back to **top**](#confidentiality-integrity--availability-cia-triad)

[🔙 Back to **Miscellaneous Overview**](README.md)
