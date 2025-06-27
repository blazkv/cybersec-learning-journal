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

This module started with **Offensive Security Intro** and **Defensive Security Intro** rooms, which I’ve already documented in [Pre Security – Linux Fundamentals](pre-security.md#4-linux-fundamentals).

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

I’ve already completed and documented **Linux Fundamentals Part 1** in [Pre Security](pre-security.md), with **Part 2** and **Part 3** being unlocked behind **TryHackMe Premium**.

---

## 3. Windows and AD Fundamentals

I’ve also already documented **Windows Fundamentals Parts 1–3** in [Pre Security – Windows Fundamentals](pre-security.md#3-windows-fundamentals).

---

## 4. Command Line

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
