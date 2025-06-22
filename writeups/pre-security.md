# TryHackMe - Pre Security

Today I started my journey on the TryHackMe (THM) learning paths, beginning with **Pre Security**. I've already encountered much of the content covered in this and the Cyber Security 101 paths, but I’m treating this as a refresher to reinforce my knowledge and fill in any gaps I may have missed during my Information Security studies.

The **Pre Security** path is made up of five modules:
1. Introduction to Cyber Security
2. Network Fundamentals
3. How the Web Works
4. Linux Fundamentals
5. Windows Fundamentals

In this write-up, I’ll describe my journey through this learning path, starting with the first module.

---

## 1. Introduction to Cybersecurity

This module is divided into two parts: **Offensive Security** and **Defensive Security**.

### Offensive Security

The first section explores offensive concepts, introduced through a fake online bank scenario. My initial task was to hack into a mock bank account. Using the `derb` command in the Ubuntu terminal (part of the simulation), I was able to enumerate directories and discover two vulnerable URLs. These were exploited to deposit money into our fake bank account.

Since I’ve worked in the terminal before, the task wasn’t intimidating. However, it was my first time using the `derb` command, which sparked my curiosity and motivated me to learn more about similar tools.

### Defensive Security

The second part focuses on **Defensive Security**, which is part of what’s known as the **Blue Team**.

The module outlines two major components of defensive security:
- **Security Operations Center (SOC)**
- **Digital Forensics and Incident Response (DFIR)**

The SOC primarily deals with identifying vulnerabilities, policy violations, unauthorized activities, and network intrusions. One of its critical tasks is **Threat Intelligence**.

Threat Intelligence aims to enable **threat-informed defense** by gathering information about potential adversaries and any actions that may disrupt or negatively impact systems. Depending on the type of organization being protected, different attackers may target different assets. The intelligence collected is supported by data that must be gathered, processed, and analyzed. This can come from internal sources (e.g., network logs) and public sources (e.g., forums, open-source feeds).

Digital Forensics and Incident Response includes:
- **Digital Forensics**, which focuses on investigating evidence of attacks and their perpetrators. This is done by analyzing:
  - File systems
  - System memory
  - System logs
  - Network logs
- **Incident Response**, which aims to reduce damage and ensure recovery as quickly as possible. Ideally, an organization will already have a response plan in place. The four phases of the incident response process are:
  1. Preparation
  2. Detection and Analysis
  3. Containment, Eradication, and Recovery
  4. Post-Incident Activity
- **Malware Analysis**, which involves identifying and studying different types of malware (e.g., viruses, trojan horses, ransomware). This can be done using:
  - **Static Analysis** (inspecting malware without executing it)
  - **Dynamic Analysis** (executing the malware in a controlled environment)

Finally, the module concludes with a **practical SOC-based simulation**. Using a simplified Security Information and Event Management (SIEM) system, I was tasked with identifying a malicious log, investigating the IP address using a fake IP scanner site (they referenced real ones like AbuseIPDB and Cisco Talos Intelligence), escalating the incident to the SOC Analyst Lead, and finally blocking the malicious IP address.

---

## 2. What is Networking?

---

## 3. How the Web Works

---

## 4. Linux Fundamentals

---

## 5. Windows Fundamentals

---

🔙 Back to [Writeups Overview](writeups/README.md)
