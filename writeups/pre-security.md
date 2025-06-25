# TryHackMe – Pre Security

The **Pre Security** path on **TryHackMe** is designed to build foundational knowledge in cybersecurity. It covers essential topics such as networking, operating systems, and web technologies — all crucial for anyone starting out in the field.

I’m working through this path to reinforce my understanding, fill any gaps, and prepare myself for a career in cybersecurity. This write-up documents my progress and key takeaways primarily for my own reference, though I’m sharing it publicly in case it helps others on a similar journey.

---

## Table of Contents

1. [🛡️ Introduction to Cyber Security](#%EF%B8%8F-1-introduction-to-cyber-security)
2. [📡 Network Fundamentals](#-2-network-fundamentals)  
3. [🌐 How the Web Works](#-3-how-the-web-works)  
4. [🐧 Linux Fundamentals](#-4-linux-fundamentals)  
5. [🏢 Windows Fundamentals](#-5-windows-fundamentals)  

---

## 🛡️ 1. Introduction to Cyber Security

### Offensive Security Intro

This section introduced **Offensive Security**, which focuses on simulating cyberattacks to find and exploit system vulnerabilities before attackers do.

- Completed a mock **online banking simulation** using a Linux terminal environment.
- Used the `derb` command-line tool for **directory enumeration**, scanning accessible directories and files on a web server.
- Discovered two vulnerable URLs and manipulated account balances, demonstrating how web application flaws can be exploited.
- Although I was familiar with basic terminal commands, this was my first time using `derb`, broadening my exposure to penetration testing tools.

### Defensive Security Intro

This section covered **Defensive Security**, aligned with **Blue Team** activities like monitoring, detection, analysis, and incident response.

- Learned the role of a **Security Operations Center (SOC)**:
  - A centralized team responsible for monitoring systems for vulnerabilities, policy violations, and indicators of compromise (IOCs).
  - Utilizes a **Security Information and Event Management (SIEM)** platform to aggregate and analyze logs.
- Explored **Threat Intelligence**: gathering and analyzing internal and external data to identify adversary tactics, techniques, and procedures (TTPs).
- Covered key concepts of **Digital Forensics and Incident Response (DFIR)**:
  - **Digital Forensics**: Analyzing logs, memory dumps, file systems, and network traffic to reconstruct attack events.
  - **Incident Response**: Minimizing damage and downtime through preparation, detection, containment, and post-incident review.
  - **Malware Analysis**: Includes **static analysis** (code examination without execution) and **dynamic analysis** (running malware in a sandbox to observe behavior).
- Completed a simulated SOC workflow:
  - Investigated suspicious log entries within a mock SIEM.
  - Used a threat intelligence platform (inspired by **AbuseIPDB** and **Cisco Talos Intelligence**) to analyze suspicious IP addresses.
  - Escalated incidents and blocked malicious IPs, simulating a full incident response cycle.

---

## 📡 2. Network Fundamentals

### What is Networking?

Explored the basics of **computer networks**, which are interconnected devices that share data.

- Used a visual analogy of individuals forming a network to explain how data flows between devices.
- Scaled this concept up to the **Internet**, a global network composed of many smaller public and private networks.

Key device identifiers:

- **IP Address (Internet Protocol)**:
  - **Private IPs**: Used within local networks to identify devices internally.
  - **Public IPs**: Assigned by the **Internet Service Provider (ISP)** to enable communication outside the local network.
  - Discussed differences between **IPv4** (32-bit) and **IPv6** (128-bit), noting IPv6’s adoption due to IPv4 address exhaustion.

- **MAC Address (Media Access Control)**:
  - A unique hardware identifier assigned to network interfaces (e.g., `a4:c3:f0:85:ac:2d`).
  - Covered **MAC spoofing**, a technique to impersonate hardware addresses and bypass weak security controls.

Networking tools:

- **Ping**:
  - Sends **Internet Control Message Protocol (ICMP)** packets to test device reachability and measure latency.
  - Practiced using `ping 8.8.8.8` to verify network connectivity.

### Premium-Only Content

Remaining topics in this module are locked behind a **TryHackMe Premium** subscription:

- **Introduction to LAN**
- **OSI Model**
- **Packets & Frames**
- **Extending Your Network**

There is additional locked content throughout this course, which I will note under each relevant section. I plan to **revisit these important topics** later through independent research.

---

## 🌐 3. How the Web Works

### DNS in Detail

Studied the **Domain Name System (DNS)**, which translates domain names into IP addresses.

- Domains are structured hierarchically: **Top-Level Domain (TLD)**, **Second-Level Domain**, and optional **subdomains**.
- Key **DNS record types** include:
  - `A` (IPv4 address), `AAAA` (IPv6 address), `CNAME` (canonical name/alias), `MX` (mail exchange), and `TXT` (text/verifications).
- DNS resolution flow:
  - Query follows this path: local cache → ISP recursive DNS → root servers → TLD servers → authoritative servers.
  - Responses are cached based on the **TTL (Time To Live)** value to improve efficiency.
- Practiced DNS queries using the `nslookup` command to retrieve different DNS record types.

### HTTP in Detail

Covered the basics of **HTTP (HyperText Transfer Protocol)** and **HTTPS (HTTP Secure)**.

- HTTP transmits data in plaintext, while HTTPS encrypts data using **Transport Layer Security (TLS)** to secure communications.
- Reviewed common HTTP methods:
  - `GET`, `POST`, `PUT`, and `DELETE` specify the action a client requests from the server.
- Analyzed common HTTP status codes:
  - `200 OK` (success), `404 Not Found` (resource missing), `403 Forbidden` (access denied), `301/302 Redirect` (URL redirection), and `500 Internal Server Error` (server fault).
- Compared request and response headers:
  - Requests typically include `Host`, `User-Agent`, and `Cookie`.
  - Responses commonly include `Set-Cookie`, `Content-Type`, and `Cache-Control`.

### How Websites Work

Browsers interact with web servers by sending **requests**. The server processes these requests and sends back **data** that the browser uses to render the webpage.

Websites consist of two main components:

- **Front End (Client-side):** The user interface displayed in the browser.
- **Back End (Server-side):** Handles application logic and processes requests.

Web content mainly uses **HTML (HyperText Markup Language)**, **CSS**, and **JavaScript**. HTML provides the page structure using tags like `<!DOCTYPE html>`, `<html>`, `<body>`, and `<p>`. Tags can include attributes, for example, `<p attribute1="value1" attribute2="value2">`. CSS styles the page, while JavaScript adds interactivity.

I have experience with the **MERN stack** and have worked with HTML, CSS, and JavaScript in previous projects. In this module, I practiced viewing page source code using browser tools like “View Page Source” to better understand website construction.

JavaScript can be included in two ways:

- Embedded directly in HTML using `<script>` tags.
- Linked externally via `<script src="/path/to/file.js"></script>`.

For example, JavaScript can dynamically change page content: `document.getElementById("demo").innerHTML`.

Security considerations emphasized avoiding **exposure of sensitive data**, such as credentials or tokens, in the source code.

I inspected a mock website to find exposed credentials, which I then used to log into the **TryHackMe** platform.

I also learned about **HTML injection**, a client-side vulnerability where unsanitized user input can inject malicious HTML or JavaScript into the DOM. To demonstrate this risk, I simulated an injection attack by submitting an `<a>` tag that redirected users to a malicious site, showing the danger of improper input validation.

### Putting it all together

When requesting a website, the computer first resolves the domain name to an IP address using **DNS**. Then it establishes a connection and communicates with the web server using **HTTP**, following these steps:

- The DNS resolution process translates a human-readable domain into an IP address.
- Once the IP is resolved, the browser sends an HTTP request to the server.
- The server responds with resources such as **HTML**, **CSS**, **JavaScript**, and images.
- The browser renders these to display the website.

Modern web applications rely on additional infrastructure to enhance performance, scalability, and security:

- **Load Balancers** distribute incoming traffic across multiple servers using algorithms like **round-robin** or **least connections**. They ensure **high availability** and automatic **failover** through health checks.
- **Content Delivery Networks (CDNs)** cache and serve static assets (e.g., JavaScript, CSS, images) from geographically distributed nodes to reduce latency and server load.
- **Databases** store and retrieve user and application data, ranging from simple files to systems like **MySQL**, **PostgreSQL**, or **MongoDB**, supporting both performance and redundancy.
- **Web Application Firewalls (WAFs)** protect web servers by filtering malicious traffic using methods like **rate limiting**, **signature-based detection**, and **bot filtering**.

A **web server** (e.g., **Apache**, **Nginx**, **IIS**, **NodeJS**) listens for incoming requests on ports **80** (HTTP) or **443** (HTTPS) and serves content from a configured **root directory** (e.g., `/var/www/html` or `C:\inetpub\wwwroot`).

- **Virtual Hosts** allow one server to host multiple domain names by matching the requested hostname to different configuration files and root directories.
- **Static content** (images, CSS, HTML) is served directly.
- **Dynamic content** is generated on-demand by backend scripts interacting with databases or user inputs.

Common backend languages include **PHP**, **Python**, **NodeJS**, and **Ruby**, enabling features like user authentication, data processing, and dynamic page generation.

For the final exercise, I ordered the steps of a website request:

**Request DNS** → check **local cache** for IP → query **recursive DNS server** → ask **root server** → query **authoritative DNS server** → authoritative server returns IP → request passes through **WAF** → then through **load balancer** → connect to **web server** on port **80/443** → web server receives **GET request** → **web application** queries **database** → browser renders the webpage.

---

## 🐧 4. Linux Fundamentals

### Linux Fundamentals Part 1

Before starting this module, I had some exposure to **Linux**. I had used **Ubuntu** to learn basic commands and set up a Linux environment. I also experimented with **Kali Linux** via **Windows Subsystem for Linux (WSL)** on Windows to explore some specialized tools. I’ve always enjoyed working with Linux, so this module felt engaging and familiar.

**Linux** powers a wide range of systems—from websites and control panels to **Point of Sale (PoS)** systems and critical infrastructure like lighting controllers.

Linux is built on the **UNIX operating system (OS)** and refers broadly to many different distributions such as **Ubuntu**, **Kali**, and **Debian**. Ubuntu is popular for servers and can run efficiently on as little as **512MB of RAM**.

The **TryHackMe** platform provided a browser-based Ubuntu machine for hands-on practice. This lightweight environment uses the **Terminal** rather than a **Graphical User Interface (GUI)**, so interaction happens through commands.

Commands I practiced include:

- `echo` — outputs any text you type
- `whoami` — displays the current logged-in user
- `ls` — lists files and directories in the current folder  
  - `ls file-name` — shows contents of a specific file  
- `cd` — changes directory
- `cat` — displays the contents of a file
- `pwd` — prints the current working directory path

I used these commands to explore directory structures, read files, and verify my location within the filesystem.

Linux offers efficient command-line tools to save time:

- `find` — searches files or folders by name  
  - Example: `find -name folder-name`  
  - Example: `find -name "*.txt"` finds all `.txt` files
- `grep` — searches within files for matching text  
  - Example: `grep keyword filename` finds occurrences of “keyword” inside “filename”

Basic command operators I learned:

- `&` — runs a command in the background  
  - Example: `cp largefile.txt backup.txt &`
- `&&` — chains commands, running the second only if the first succeeds  
  - Example: `mkdir new && cd new`
- `>` — redirects output, overwriting file content  
  - Example: `echo hey > welcome`
- `>>` — appends output to a file without overwriting  
  - Example: `echo more >> welcome`

These fundamentals are critical for efficient navigation and file manipulation in Linux environments, which are common in cybersecurity operations.

### Premium-Only Content

- **Linux Fundamentals Part 2**
- **Linux Fundamentals Part 3**

---

## 🏢 5. Windows Fundamentals

### Windows Fundamentals Part 1

This module section started with a brief history of Windows OS, highlighting important differences between **Windows Home** and **Pro** editions. Here’s a summary table of key differences relevant to SOC and networking:

| Feature                            | Windows 11 Home | Windows 11 Pro  | Why It Matters for Cybersecurity Professionals                  |
|------------------------------------|:---------------:|:---------------:|-----------------------------------------------------------------|
| **BitLocker Encryption**           | ❌              | ✅             | Ensures disk security and supports forensic data protection     |
| **Domain Join / Azure AD**         | ❌              | ✅             | Enables centralized access control and policy enforcement       |
| **Group Policy Editor**            | ❌              | ✅             | Critical for pushing security configurations across devices     |
| **Windows Update for Business**    | ❌              | ✅             | Allows controlled update rollouts and patch management          |
| **Remote Desktop Host**            | ❌              | ✅             | Supports remote incident response and administrative tasks      |
| **Hyper-V & Windows Sandbox**      | ❌              | ✅             | Enables safe malware analysis and isolated testing environments |
| **Windows Information Protection** | ❌              | ✅             | Helps prevent data leaks on enterprise systems                  |

The current Windows Server OS is **Windows Server 2025**.

Unlike Linux terminals, Windows provides a **Graphical User Interface (GUI)**, which is briefly introduced here but not covered in detail.

Windows uses the **NTFS (New Technology File System)** for its file system, which supports features not available in older systems like FAT16/FAT32 or HPFS:
- NTFS is a **journaling file system**, meaning it maintains logs that help automatically repair corrupted files/folders after a crash.
- It supports granular **file/folder permissions**, **compression**, and **Encryption File System (EFS)**.

File/Folder permissions define what users can do:

| **Permission**           | **Folders**                                   | **Files**                                |
|--------------------------|-----------------------------------------------|------------------------------------------|
| **Read**                 | View/list files and subfolders                | View/access file contents                |
| **Write**                | Add files/subfolders                          | Write to the file                        |
| **Read & Execute**       | View, list, and execute files (inherited)     | View, access, and execute the file       |
| **List Folder Contents** | View, list, and execute files (folders only)  | N/A                                      |
| **Modify**               | Read, write, delete files/folders             | Read, write, and delete file             |
| **Full Control**         | Read, write, modify, and delete files/folders | Read, write, modify, and delete the file |

**Alternate Data Streams (ADS)** in NTFS allow a file to contain multiple streams of data, not just the main `\$DATA` stream. ADS can be used to hide data (often by malware), and they do not affect file checksums. However, ADS are lost if files are compressed (ZIP, RAR), Base64 encoded, or moved to FAT32 drives.

The system environment variable `%windir%` points to the Windows installation directory (typically `C:\Windows`), ensuring scripts and programs work regardless of where Windows is installed.

The **System32** folder inside the Windows directory holds critical OS files:
- **EXEs** (executable programs like Task Manager, `taskmgr.exe`)
- **DLLs** (shared libraries)
- **Drivers** (hardware communication)
- The **Windows Registry** (stores system/app settings)

Windows local user accounts typically fall into two categories:
- **Administrator**: Full system management rights
- **Standard User**: Limited to modifying their own files and settings

To manage users/groups, run `lusrmgr.msc`. Users inherit permissions from groups and can belong to multiple groups.

To reduce malware impact, **User Account Control (UAC)** was introduced (since Windows Vista). It runs admins with standard privileges by default and prompts for consent when elevated permissions are needed (e.g., installing software).

The **Control Panel** and **Task Manager** are key tools:
- **Settings** (introduced in Windows 8) offers a user-friendly interface for configuration.
- **Task Manager** (`Ctrl + Shift + Esc`) shows running apps/processes and resource usage (CPU, RAM).

---

### Windows Fundamentals Part 2

The **System Configuration** tool (`msconfig`) helps with advanced troubleshooting and startup diagnostics:
- **General**: Choose between Normal, Diagnostic, or Selective startup.
- **Boot**: Configure OS boot options.
- **Services**: View/enable/disable system background services.
- **Startup**: Redirects to Task Manager in newer Windows versions for managing startup apps.

**Computer Management** (`compmgmt.msc`) consolidates many admin tools:

- **System Tools**:
  - **Task Scheduler**: Automate tasks triggered by events or schedules.
  - **Event Viewer**: Logs detailed system, security, and application events:

| Event Type       | Description                                     |
|------------------|-------------------------------------------------|
| **Error**        | Critical failures causing loss of function/data |
| **Warning**      | Potential issues, e.g., low disk space          |
| **Information**  | Successful operations, e.g., driver loaded      |
| **Success Audit**| Successful security access, e.g., user logon    |
| **Failure Audit**| Failed security access attempts                 |

  - **Shared Folders**: Manage network shares and sessions.
  - **Local Users and Groups**: User/group management.
  - **Performance Monitor** (`perfmon`): Track system resource use; **Resource Monitor** (`resmon`) available here too.
  - **Device Manager** (`devmgmt.msc`): View/configure hardware devices.

- **Storage**:
  - **Disk Management** (`diskmgmt.msc`): Manage drives, partitions, and drive letters.

- **Services and Applications**:
  - Manage background services and their properties.
  - **WMI Control**: Configure Windows Management Instrumentation.  
  - **WMIC** is deprecated; use **PowerShell** for WMI tasks.

**System Information** (`msinfo32.exe`) provides detailed system specs in categories:
- **Hardware Resources**
- **Components** (e.g., storage, display devices)
- **Software Environment** (drivers, running tasks, services, environment variables)

The **System Summary** shows OS version, manufacturer, CPU, BIOS, and other key info.

---

### Windows  Fundamentals Part 3

---

[🔝 Back to **top**](#tryhackme--pre-security)

[🔙 Back to **Writeups Overview**](README.md)
