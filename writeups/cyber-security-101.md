# TryHackMe Cyber Security 101

**Cyber Security 101** provides a solid introduction to key areas of cyber security. It covers foundational topics like system protection, vulnerability awareness, and practical security skills essential for newcomers.

I’m progressing through this path to build a strong base, sharpen my hands-on abilities, and track my learning journey. While this write-up mainly supports my own growth, I hope it can also offer value to others exploring the field.

---

## Table of Contents

1. [Start Your Cyber Security Journey](#1-start-your-cyber-security-journey)
2. [Linux Fundamentals](#2-linux-fundamentals)
3. [Windows and AD Fundamentals](#3-windows-and-ad-fundamentals)
4. [Command Line](#4-command-line)
5. [Networking](#5-networking)
6. [Cryptography](#6-cryptography)
7. [Exploitation Basics](#7-exploitation-basics)
8. [Web Hacking](#8-web-hacking)
9. [Offensive Security Tooling](#9-offensive-security-tooling)
10. [Defensive Security](#10-defensive-security)
11. [Security Solutions](#11-security-solutions)
12. [Defensive Security Tooling](#12-defensive-security-tooling)
13. [Build Your Cyber Security Career](#13-build-your-cyber-security-career)

---

## 1. Start Your Cyber Security Journey

### Offensive Security Intro and Defensive Security Intro

This module started with **Offensive Security Intro** and **Defensive Security Intro** rooms, which I’ve already documented in [Pre Security – Introduction to Cyber Security](pre-security.md#1-introduction-to-cyber-security).

### Search Skills

The goal of this room was to strengthen how I **find, evaluate, and read information** using various **browsing tools**. Since anyone can publish information online, it’s up to us to critically assess what we find. Key points I focused on:

- **Source** – identify the author or publisher and consider whether they’re reputable.
- **Evidence and reasoning** – check that claims are supported by credible evidence and logical arguments.
- **Objectivity and bias** – information should be presented impartially, showing multiple perspectives where relevant.
- **Corroboration and consistency** – verify information by comparing it with multiple independent sources.

Each **internet search engine** (Google, Bing, DuckDuckGo, etc.) supports **advanced search**. **Google**, for example, offers these common **search operators**:

- `"exact phrase"` – using double quotes returns pages with the **exact word or phrase**.
- `site:` – limits results to a specific domain, e.g., `site:tryhackme.com success stories`.
- `-` – the minus sign excludes terms, e.g., `pyramids -tourism` to avoid tourism results.
- `filetype:` – searches for specific file types, e.g., `filetype:pdf nist csf` returns PDF files related to the NIST Cybersecurity Framework.

I also bookmarked this useful list of [advanced search operators](https://github.com/cipher387/Advanced-search-operators-list) for future reference.

There are **specialized search engines** that help find specific types of information:

- **Shodan** – searches for **servers**, **networking gear**, **industrial control systems**, and **IoT devices** by type and version. For example, I can look up how many servers still run Apache 2.4.1 and where they’re located by searching for `apache 2.4.1`.
- **Censys** – focuses on **Internet-connected hosts**, **websites**, **certificates**, and other assets. It’s useful for tasks like enumerating domains, **auditing open ports**, and spotting **rogue assets**.
- **VirusTotal** – scans **files** or **URLs** with multiple antivirus engines at once. It’s also possible to input file hashes to see previous scan results.
- **Have I Been Pwned** (HIBP) – checks if an **email address** has appeared in a **known data breach**, which helps identify leaked personal data and passwords.

Besides HIBP, this was my first time trying out Shodan, Censys, and VirusTotal — and they already feel invaluable for both offensive and defensive research.

I also explored **Common Vulnerabilities and Exposures** (CVE), which is a **standardized dictionary of known vulnerabilities** with unique **CVE IDs**. I can find CVEs through the [CVE Program Mission](https://www.cve.org/) or the [NIST National Vulnerability Database](https://nvd.nist.gov/).

**Exploit Database** is a go-to for finding working exploit code — for example, a company’s red team might use it to locate proofs of concept for known CVEs. **GitHub** can also host repositories with tools, **PoC** scripts, or exploit code for the same purpose.

It’s just as important to find **official documentation**. On **Linux** and other Unix-like systems, the `man` command provides **manual pages** for commands, system calls, libraries, and configuration files. **Microsoft** maintains an extensive [Technical Documentation page](https://learn.microsoft.com/en-us/) for its products.

The room wraps up with advice on **social media investigation**. It’s wise to use **temporary email addresses** for accounts you’ll only need briefly. Social media can be a goldmine for cybersecurity professionals — whether researching people or technical details. Staying active on relevant channels is also one of the best ways to keep up with **new threats, tools, and techniques**, helping me grow my technical skills and awareness over time.

---

## 2. Linux Fundamentals

I’ve already completed and documented **Linux Fundamentals Part 1** in [Pre Security – Linux Fundamentals](pre-security.md#4-linux-fundamentals), with **Part 2** and **Part 3** being unlocked behind **TryHackMe Premium**.

---

## 3. Windows and AD Fundamentals

### Windows Fundamentals Parts 1–3

I’ve also already documented **Windows Fundamentals Parts 1–3** in [Pre Security – Windows Fundamentals](pre-security.md#5-windows-fundamentals).

### Active Directory Basics

In a corporate environment, managing devices and users at scale is handled through **Active Directory** (AD).

For a small office with a handful of computers, it’s manageable to configure and troubleshoot each machine individually. But as an organization grows into hundreds or thousands of endpoints, a **Windows domain** becomes essential for scalability and centralized control.

A **Windows domain** is a collection of **users** and **computers** managed from a central location. This is possible because of **Active Directory** (AD), which acts as a single, authoritative directory for all domain objects. AD services run on a dedicated server called a **Domain Controller** (DC).

Key benefits of a properly configured **Windows domain**:
- **Centralized identity management** — Administrators handle all user accounts, passwords, and permissions in one place, reducing manual overhead.
- **Policy enforcement** — Security policies can be pushed from AD and automatically applied to any user or device that joins the domain.

A simple example is a corporate or school network login: your username and password work on any domain-joined device because each machine **authenticates** you through **Active Directory**. AD verifies your **credentials**, then applies any required **policies**, like restricting Control Panel access or enforcing screen lock settings.

At the heart of a **Windows domain** is **Active Directory Domain Services** (AD DS). AD DS holds detailed records about all **objects** — the building blocks of a domain — including users, groups, computers, printers, and shared resources.

- **Users** — The most common **security principal**. A user can be:
  - A real person in the organization who needs network access.
  - A service account used by software (like IIS or SQL Server) to run with only the required permissions.

- **Machines** — Any computer added to AD becomes a **machine object**, which is also a **security principal**. Machine accounts have local admin rights on themselves but shouldn’t be used like regular user accounts. By convention, machine account names end with a dollar sign (`$`), like `DC01$`.

- **Security groups** — These simplify access control. Adding a user to a group grants them that group’s permissions. Groups can contain **users**, **machines**, or even other groups. Security groups themselves are security principals too. Every domain comes with some default groups for common tasks.

To manage these objects, we log in to the **Domain Controller** and open **Active Directory Users and Computers** (ADUC) from the start menu.

In ADUC, objects appear in **Organizational Units** (OUs). OUs are **container objects** that help classify users and computers into manageable sections. They allow administrators to apply **Group Policies** to specific sets of objects. Each user or machine can only belong to one OU at a time.

Common default containers and OUs include:
- **Builtin** — Default Windows groups.
- **Computers** — The default container for new machines joining the domain.
- **Domain Controllers** — The default OU for Security Operations Center (SOC) domain controllers.
- **Users** — Stores default domain-wide users and groups.
- **Managed Service Accounts** — Holds accounts used by services within the domain.

Both **OUs** and **Security Groups** organize users and computers, but their roles differ:
- OUs apply **Group Policies** to configure or restrict devices and users. Because conflicting policies can cause issues, an object can only sit in one OU.
- **Security Groups** grant or deny access to resources like shared drives or printers. A user can be in multiple groups at once to handle various permissions.

To build practical experience, I tested creating a few Group Policy Objects (GPOs) to enforce security baselines. One GPO blocked non-IT users from accessing the **Control Panel**. Another enforced an auto-lock for all **workstations** and **servers** after 5 minutes of inactivity.

To restrict the Control Panel, I created a GPO named **Restrict Control Panel Access**. Under **User Configuration**, I enabled `Prohibit Access to Control Panel and PC settings`. I linked this GPO to the **Marketing**, **Management**, and **Sales** OUs so only those users are restricted, while IT keeps full access for support and maintenance.

For the auto-lock, I set up a GPO called **Auto Lock Screen**. Under **Computer Configuration**, I configured the inactivity timeout to 5 minutes. I linked it at the root domain level so that all **child OUs** inherit it automatically. Because this GPO only targets computers, it doesn’t interfere with user-only OUs like Sales or Marketing.

To confirm everything worked, I connected through RDP as a test user (`THM\Mark`). When Mark tried to open the Control Panel, access was denied as expected. After 5 minutes idle, the session locked automatically. This lab reinforced how GPO inheritance and filtering work for managing different security baselines across AD.

In a **Windows domain**, all credentials live on the **Domain Controllers**. When a user signs in, their credentials are verified by the DC using one of two protocols:
- **Kerberos** — The standard protocol for modern Windows authentication.
- **NetNTLM** — An older protocol still used in legacy cases.

When a user authenticates with **Kerberos**, they send their username and a timestamp (encrypted with a key derived from their password) to the **Key Distribution Center (KDC)**, which runs on a **Domain Controller**.

The KDC responds with a **Ticket Granting Ticket (TGT)** and a **Session Key**. The TGT is encrypted with the `krbtgt` account’s password hash, so the user can’t read it. This design lets the KDC recover the session information by decrypting the TGT later.

When the user wants to access a service, they present the TGT, an encrypted timestamp, and the **Service Principal Name (SPN)** to the KDC to get a **Ticket Granting Service (TGS)** ticket. The KDC returns a TGS and a **Service Session Key**. The service decrypts the TGS, verifies the session key, and grants access.

As organizations expand, one domain often isn’t enough. Managing multiple offices, compliance zones, or IT teams can make a single large domain difficult to maintain. **Active Directory** solves this with **trees** — multiple domains that share the same **namespace**. For example, `thm.local` might split into `uk.thm.local` and `us.thm.local`, forming a tree with one **root** and separate **subdomains**, each with its own DCs, users, and machines.

Each domain has its own **Domain Admins**, while the **Enterprise Admins** group has full authority across all domains in the tree. This keeps local teams independent while enabling centralized oversight.

Multiple **trees** with different namespaces form a **forest** — the top-level structure in AD for managing connected but separate domains.

To share access across domains, AD uses **trust relationships**:
- A **one-way trust** allows Domain BBB users to access Domain AAA’s resources (not the other way around). The trust direction is the opposite of the access direction.
- A **two-way trust** allows both domains to grant each other’s users permissions. Domains in the same **tree** or **forest** automatically share a two-way trust.

A trust doesn’t grant **automatic access** — it only enables permissions to be assigned across domains when needed.

---

## 4. Command Line

The **Command-line interface** (CLI) has several advantages over a GUI. It uses fewer system resources, supports robust **automation**, and enables straightforward **remote management**. These strengths make the CLI an essential tool for any Security Operations Center (SOC) analyst who needs to manage multiple systems efficiently and repeat tasks reliably.

---

## 5. Networking

---

## 6. Cryptography

---

## 7. Exploitation Basics

---

## 8. Web Hacking

---

## 9. Offensive Security Tooling

---

## 10. Defensive Security

---

## 11. Security Solutions

---

## 12. Defensive Security Tooling

---

## 13. Build Your Cyber Security Career

---

[🔝 Back to **top**](#tryhackme-cyber-security-101)

[🔙 Back to **Writeups Overview**](README.md)
