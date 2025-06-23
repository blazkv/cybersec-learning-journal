# TryHackMe – Pre Security

The **Pre Security** path on TryHackMe provides a solid foundation in cybersecurity fundamentals. While I’ve studied much of this content before through formal Information Security courses and the Cyber Security 101 path, I’m revisiting it to strengthen core knowledge and close any remaining gaps, especially in areas relevant to a Security Operations Center role. This write-up is a minimal but informative summary of my progress and does not reflect my full set of notes.

---

## 🛡️ 1. Introduction to Cyber Security

### **Offensive Security Intro**

This section introduced **Offensive Security**, which involves simulating cyberattacks to identify and exploit system vulnerabilities before malicious actors do.

* Worked through a mock **online banking simulation** using a Linux terminal.
* Learned to use the `derb` command-line tool for **directory enumeration**, scanning accessible directories and files on a web server.
* Identified two vulnerable URLs and manipulated account balances, illustrating exploitation of web application flaws.
* Although familiar with terminal navigation, this was my first experience with `derb`, expanding my awareness of penetration testing tools.

### **Defensive Security Intro**

This section focused on **Defensive Security**, aligned with **Blue Team** functions such as monitoring, detection, analysis, and incident response.

* Introduced the structure and function of a **Security Operations Center (SOC)**:

  * Centralized team monitoring systems for vulnerabilities, policy violations, and indicators of compromise (IOCs).
  * Uses a **SIEM (Security Information and Event Management)** platform for log aggregation and analysis.
* Learned about **Threat Intelligence** — collecting and analyzing internal and external data to identify adversary tactics, techniques, and procedures (TTPs).
* Covered fundamentals of **DFIR (Digital Forensics and Incident Response)**:

  * **Digital Forensics**: Examining logs, memory dumps, file systems, and network traffic to reconstruct attacks.
  * **Incident Response**: Minimizing damage and recovery time via preparation, detection, containment, and post-incident review.
  * **Malware Analysis**: Both **static analysis** (code review without execution) and **dynamic analysis** (sandboxed execution to observe behavior).
* Completed a simulated SOC workflow:

  * Investigated malicious log entries in a mock SIEM.
  * Used a threat intel platform (modeled after **AbuseIPDB** and **Cisco Talos Intelligence**) to analyze suspicious IPs.
  * Escalated incidents and blocked malicious IPs, simulating full response procedures.

---

## 📡 2. Network Fundamentals

### **What is Networking?**

Explored the fundamentals of **computer networks** — interconnected devices sharing data.

* Visual analogy of individuals forming a network to illustrate data flow.
* Scaled to the **Internet**, a global network made of smaller public and private networks.

Key device identifiers:

* **IP Address (Internet Protocol)**:

  * **Private IPs**: Used within local networks.
  * **Public IPs**: Assigned by the **ISP (Internet Service Provider)** for external communication.
  * Covered differences between **IPv4** (32-bit) and **IPv6** (128-bit), with IPv6 adoption due to IPv4 exhaustion.
* **MAC Address (Media Access Control)**:

  * Unique hardware identifier for network interfaces (e.g., `a4:c3:f0:85:ac:2d`).
  * Explored **MAC spoofing** as a technique to bypass weak security controls.

Networking tools:

* **Ping**:

  * Sends **ICMP (Internet Control Message Protocol)** packets to test reachability and latency.
  * Practiced with `ping 8.8.8.8` to verify connectivity.

### Premium-Only Content

Remaining topics are locked behind a **TryHackMe Premium** subscription:

* **Intro to LAN**
* **OSI Model**
* **Packets & Frames**
* **Extending Your Network**

I plan to revisit these critical networking topics once accessible.

---

## 🌐 3. How the Web Works

### **DNS in Detail**

Studied the **Domain Name System (DNS)**, which translates domain names into IP addresses.

* Domains structured as **Top-Level Domain (TLD)**, **Second-Level Domain**, and optional **subdomains**.
* Key **DNS record types**:

  * `A` (IPv4), `AAAA` (IPv6), `CNAME` (alias), `MX` (mail), and `TXT` (text, verification).
* DNS resolution flow:

  * Local cache → ISP recursive DNS → Root servers → TLD servers → Authoritative servers.
  * Results cached according to **TTL (Time To Live)**.
* Hands-on practice using `nslookup` to query DNS records.

### **HTTP in Detail**

Covered **HTTP (HyperText Transfer Protocol)** and **HTTPS (HTTP Secure)** protocols.

* HTTP transmits data in plaintext; HTTPS secures data using **TLS (Transport Layer Security)** encryption.
* Reviewed HTTP methods:

  * `GET`, `POST`, `PUT`, `DELETE` specify client-server actions.
* Analyzed common HTTP status codes:

  * `200 OK`, `404 Not Found`, `403 Forbidden`, `301/302 Redirect`, `500 Internal Server Error`.
* Compared request and response headers:

  * Requests include `Host`, `User-Agent`, `Cookie`.
  * Responses include `Set-Cookie`, `Content-Type`, `Cache-Control`.

### **How Websites Work**



### **Putting it all together**



---

## 🐧 4. Linux Fundamentals
   
### Linux Fundamentals Part 1
### Linux Fundamentals Part 2
### Linux Fundamentals Part 3

---

## 🏢 5. Windows Fundamentals
### Windows Fundamentals Part 1
### Windows  Fundamentals Part 2
### Windows  Fundamentals Part 3

---

## 📌 6. Key Takeaways

*To be completed at the end of the learning path.*

---

🔙 Back to [Writeups Overview](README.md)
