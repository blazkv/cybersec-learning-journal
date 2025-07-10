# Principle of Least Privilege

## Definition

The **Principle of Least Privilege (POLP)** is a security concept that restricts user, application, and process permissions to the minimum necessary to perform their tasks. By applying POLP, organizations limit potential attack paths and reduce the impact if an account or process is compromised. This principle applies to both physical and logical access controls, ensuring every identity has just enough permissions — and no more — to function as intended.

---

## Why It Matters

Implementing POLP is essential for reducing risk and limiting damage from compromised accounts or processes. By granting users and applications only the access they need — and nothing more — organizations shrink the attack surface available to threat actors.

POLP is more than a best practice; it is required by frameworks like the **National Institute of Standards and Technology (NIST)** SP 800-53 and SP 800-171. It also supports security models such as **Zero Trust**, where constant verification and minimal permissions are fundamental.

Without least privilege, attackers who gain access to one account can move laterally, escalate privileges, and access sensitive data. Enforcing POLP helps contain breaches and aligns with industry standards like PCI DSS and HIPAA, which mandate strict access controls for compliance.

---

## How It Works / Core Components

Applying POLP involves practical controls to keep access tightly managed. The most important components include:

- **Role-Based Access Control (RBAC)**  
  - Permissions are assigned based on clearly defined job roles rather than individuals. This makes access consistent and easier to manage at scale.

- **Privilege Separation**  
  - Users and processes run with the lowest level of access needed. High-risk tasks require separate credentials or higher-level accounts.

- **Separation of Duties (SoD)**  
  - Critical tasks are divided among multiple people to prevent abuse. For example, development and deployment responsibilities are separated to reduce insider risks.

- **Just-In-Time (JIT) Access**  
  - Elevated privileges are granted only when necessary and automatically revoked afterward. This limits the exposure time of powerful accounts.

- **Regular Auditing and Reviews**  
  - Permissions and accounts are reviewed routinely to remove unnecessary access and detect privilege creep.

Additional measures like **Multi-Factor Authentication (MFA)**, **Default Deny**, and time-based restrictions further strengthen POLP and should be implemented when appropriate for the organization’s environment and risk level.

---

## Real-World Applications

A clear example of POLP is how cloud providers like **Amazon Web Services (AWS)** recommend managing Identity and Access Management (IAM). AWS best practices start with zero permissions and grant only the specific rights each user, role, or service requires ([AWS IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)).

For example, AWS IAM policies typically:

- Create distinct IAM roles for tasks such as read-only access, billing management, or instance deployment.
- Use service roles to limit what applications can do — for instance, allowing an EC2 instance to write logs to an S3 bucket but nothing else.
- Combine POLP with **Multi-Factor Authentication (MFA)** and regular access reviews to prevent privilege creep.

The 2017 **Equifax breach** illustrates the dangers of ignoring POLP. Attackers exploited a web application vulnerability and moved laterally due to weak privilege separation and excessive access rights, exposing massive sensitive data.

In practice, organizations enforce POLP by restricting admin accounts, using separate standard user accounts for daily activities, and limiting script or API permissions strictly to necessary actions.

---

## Challenges

Enforcing POLP can be challenging. Balancing security with usability is difficult — overly strict permissions may disrupt workflows and lead to risky workarounds.

**Privilege creep** is common: users accumulate permissions over time through role changes or temporary access that isn’t revoked. Without regular audits or automation, this often goes unnoticed.

Legacy systems may lack support for granular permissions or modern access controls, forcing broader rights than ideal.

Maintaining POLP requires continuous effort: clear policies, technical enforcement via tools like RBAC and JIT access, and an organizational culture that treats access management as an ongoing responsibility rather than a one-time setup.

---

🔝 Back to [top](#principle-of-least-privilege)

🔙 Back to [Miscellaneous Overview](README.md)
