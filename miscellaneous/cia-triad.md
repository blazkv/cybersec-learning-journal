# Confidentiality, Integrity & Availability (CIA) Triad

## 📝 Definition

This summary is based on the [NIST Cybersecurity Practice Guide SP 1800-26A](https://csrc.nist.gov/pubs/sp/800/12/r1/final). The **CIA Triad** is a foundational model in cybersecurity representing three critical principles:

* **Confidentiality**: Ensuring information is only accessible to authorized individuals.
* **Integrity**: Protecting information from unauthorized alteration to maintain its accuracy and trustworthiness.
* **Availability**: Ensuring that authorized users can access information and resources when needed.

NIST guidance particularly emphasizes data integrity as a key focus area, stressing the importance of preserving data accuracy throughout its lifecycle.

---

## ❗ Why It Matters

Maintaining **data integrity** is essential because unauthorized changes can undermine trust in information, leading to operational disruptions and reputational damage. Attacks like **ransomware** specifically target integrity by encrypting or corrupting files, which can halt critical services such as email, financial processing, or customer data management. Detecting and responding to these threats promptly is crucial for minimizing impact.

---

## ⚙️ How It Works / Key Components

NIST’s [Cybersecurity Framework (CSF)](https://www.nist.gov/cyberframework) organizes protections around five core functions:

* **Identify**: Understand risks to systems, assets, and data.
* **Protect**: Implement safeguards to limit the impact of potential incidents.
* **Detect**: Recognize cybersecurity events in a timely manner.
* **Respond**: Contain and mitigate the effects of detected incidents.
* **Recover**: Restore affected capabilities and services to normal operation.

The CIA Triad supports and underpins each of these functions, ensuring that security controls align with core organizational needs.

---

## 🔍 Real-World Examples

In **November 2023**, Holding Slovenske elektrarne (HSE) was struck by a **ransomware attack** that encrypted files across its IT infrastructure. Although **power production** and core plant operations remained functional, internal systems, websites, and employee access were **compromised**.

This incident clearly illustrates the CIA Triad in action:

* **Confidentiality** was threatened by the potential exposure of sensitive internal data.
* **Integrity** was impacted as encrypted and potentially altered files raised doubts about their trustworthiness.
* **Availability** suffered as internal workflows were interrupted, reducing employee productivity and public service access.

From a **security operations perspective**, this case highlights the importance of real-time monitoring for encryption patterns, enforcing strong access controls, and segmenting critical infrastructure. Quick containment and recovery measures are essential to maintain availability while assessing any compromise to data integrity or confidentiality.

---

## ⚠️ Challenges / Common Pitfalls

A key challenge in applying the CIA Triad is maintaining an appropriate **balance** between its components. Overemphasizing one aspect can inadvertently weaken the others. For example, focusing too heavily on **confidentiality** through restrictive access controls can limit **availability** for legitimate users. Likewise, enforcing strict **data integrity** checks may slow down system responsiveness—an issue in time-critical environments.

A frequent **misconception** is treating confidentiality, integrity, and availability as independent goals. In reality, they are deeply **interconnected**: a disruption in availability can make it impossible to verify integrity, while a breach of integrity can compromise confidentiality and trust.

Another pitfall is viewing the triad purely from a **technical standpoint**, ignoring human and organizational factors. Security policies, user awareness, and physical safeguards are all essential to upholding the triad in real-world environments. Even the most secure infrastructure can fail due to weak credentials or poor configuration.

Finally, in **modern architectures** like cloud computing, IoT, and hybrid work environments, the traditional boundaries around data and control shift. Security teams must continuously reassess how the CIA principles apply in these evolving contexts to ensure they remain enforceable and effective.

---

🔙 Back to [Miscellaneous Overview](README.md)
