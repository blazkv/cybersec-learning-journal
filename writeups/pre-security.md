# TryHackMe – Pre Security

The **Pre Security** path on TryHackMe provides a solid foundation in cybersecurity fundamentals. While I’ve studied much of this content before through formal Information Security courses and the Cyber Security 101 path, I’m revisiting it to strengthen core knowledge and close any remaining gaps, especially in areas relevant to a Security Operations Center role. This write-up is a minimal but informative summary of my progress and does not reflect my full set of notes.

---

## 🛡️ 1. Introduction to Cyber Security

### **Offensive Security Intro**

This section introduced **Offensive Security**, which involves simulating cyberattacks to identify and exploit system vulnerabilities before malicious actors do.

- Worked through a mock **online banking simulation** using a Linux terminal.
- Learned to use the `derb` command-line tool for **directory enumeration**, scanning accessible directories and files on a web server.
- Identified two vulnerable URLs and manipulated account balances, illustrating exploitation of web application flaws.
- Although familiar with terminal navigation, this was my first experience with `derb`, expanding my awareness of penetration testing tools.

### **Defensive Security Intro**

This section focused on **Defensive Security**, aligned with **Blue Team** functions such as monitoring, detection, analysis, and incident response.

- Introduced the structure and function of a **Security Operations Center (SOC)**:
 - Centralized team monitoring systems for vulnerabilities, policy violations, and indicators of compromise (IOCs).
 - Uses a **SIEM (Security Information and Event Management)** platform for log aggregation and analysis.
- Learned about **Threat Intelligence** — collecting and analyzing internal and external data to identify adversary tactics, techniques, and procedures (TTPs).
- Covered fundamentals of **DFIR (Digital Forensics and Incident Response)**:
 - **Digital Forensics**: Examining logs, memory dumps, file systems, and network traffic to reconstruct attacks.
 - **Incident Response**: Minimizing damage and recovery time via preparation, detection, containment, and post-incident review.
 - **Malware Analysis**: Both **static analysis** (code review without execution) and **dynamic analysis** (sandboxed execution to observe behavior).
- Completed a simulated SOC workflow:
 - Investigated malicious log entries in a mock SIEM.
 - Used a threat intel platform (modeled after **AbuseIPDB** and **Cisco Talos Intelligence**) to analyze suspicious IPs.
 - Escalated incidents and blocked malicious IPs, simulating full response procedures.

---

## 📡 2. Network Fundamentals

### **What is Networking?**

Explored the fundamentals of **computer networks** — interconnected devices sharing data.
- Visual analogy of individuals forming a network to illustrate data flow.
- Scaled to the **Internet**, a global network made of smaller public and private networks.

Key device identifiers:
- **IP Address (Internet Protocol)**:
 - **Private IPs**: Used within local networks.
 - **Public IPs**: Assigned by the **ISP (Internet Service Provider)** for external communication.
 - Covered differences between **IPv4** (32-bit) and **IPv6** (128-bit), with IPv6 adoption due to IPv4 exhaustion.
- **MAC Address (Media Access Control)**:
 - Unique hardware identifier for network interfaces (e.g., `a4:c3:f0:85:ac:2d`).
 - Explored **MAC spoofing** as a technique to bypass weak security controls.

Networking tools:
- **Ping**:
 - Sends **ICMP (Internet Control Message Protocol)** packets to test reachability and latency.
 - Practiced with `ping 8.8.8.8` to verify connectivity.

### Premium-Only Content

Remaining topics are locked behind a **TryHackMe Premium** subscription:

- **Intro to LAN**
- **OSI Model**
- **Packets & Frames**
- **Extending Your Network**

There is additional locked content within this course, which I will list under each relevant section. I plan to **revisit these important topics** later through my own research.

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

This section explained how web browsers interact with servers. When **visiting a website**, your **browser** sends a **request** to a **web server** (a remote computer that processes these requests). The server responds with **data** that the browser uses to **render the website**.

Websites consist of two major components:
- **Front End** (Client-side): What the user sees — how the browser displays content.
- **Back End** (Server-side): Handles logic, processes requests, and delivers responses.

Web content is primarily built using **HTML (HyperText Markup Language)**, **CSS**, and **JavaScript**:
- HTML provides structure using elements like `<html>`, `<body>`, and `<p>`. It begins with a `<!DOCTYPE html>` declaration to define the document type.
- HTML elements can include attributes — for example: `<p attribute1="value1" attribute2="value2">`.
- **CSS** styles these elements, while **JavaScript** adds interactivity.

I’ve already taught myself the fundamentals of the **MERN stack** and used HTML, CSS, and JavaScript in previous projects. I also practiced viewing the **HTML source code** of web pages using browser tools like “View Page Source.”

JavaScript can be included directly within HTML using the `<script>` tag, or externally via: `<script src="/path/to/file.js"></script>`.

In this task, I practiced modifying content dynamically using JavaScript and the `document.getElementById("demo").innerHTML` method.

Security was also a key focus:
- Emphasized avoiding **sensitive data exposure** — credentials or tokens should never appear in the page source.
- I inspected a mock website to locate exposed credentials and used them to log into the **TryHackMe** platform.

Finally, the task introduced **HTML injection** — a **client-side vulnerability** where unvalidated user input is rendered directly into the page’s DOM. If input isn't sanitized, attackers can inject HTML or JavaScript to alter behavior or steal data. The exercise concluded with simulating an injection attack by submitting an `<a>` tag that redirected to a malicious site instead of entering credentials.

### **Putting it all together**

When you **request a website**, your computer must determine the **IP address** of the web server it needs to communicate with. This is handled by the **DNS**, which translates human-readable domain names into numerical IP addresses. Once the IP is resolved, your computer establishes a connection and communicates with the web server using the **HTTP** — a standardized set of rules for data exchange. The server responds by sending resources such as **HTML**, **CSS**, **JavaScript**, and **images**, which the **browser** uses to properly **render and display the website** to the user.

To support scalability, performance, and security, modern web applications often use additional infrastructure:
* **Load Balancers** distribute incoming traffic across multiple servers using algorithms like **round-robin** or **least connections**, ensuring **high availability** and automatic **failover** through periodic **health checks**.
* **CDNs (Content Delivery Networks)** cache and serve static assets (e.g., JavaScript, CSS, images) from geographically distributed nodes to reduce latency and server load.
* **Databases** store and retrieve user and application data, ranging from simple flat files to complex systems like **MySQL**, **Postgres**, or **MongoDB**, supporting both performance and redundancy.
* **WAFs (Web Application Firewalls)** act as a protective layer between users and web servers, filtering out malicious traffic using **rate limiting**, **signature-based detection**, and **bot filtering**.

A **web server** is software (e.g., **Apache**, **Nginx**, **IIS**, **NodeJS**) that listens for incoming connections and serves content over **HTTP** from a defined **root directory** (e.g., `/var/www/html` or `C:\inetpub\wwwroot`). When a client requests a file, the server maps the URL path to a local file and returns it.
* **Virtual Hosts** allow one server to host multiple domain names by matching the requested hostname to configuration files, each with its own root directory.
* **Static content** (e.g., images, CSS, HTML) is delivered directly without changes.
* **Dynamic content** is generated on request via **backend scripts** that can interact with databases or user input, returning different results based on context.

Common **backend languages** include **PHP**, **Python**, **NodeJS**, and **Ruby**, enabling features like user interaction, data processing, and content generation.

As my last task, I had to place in order how a request to a website works. The answer was:
**Request DNS** → check **local cache** for IP address → check your **recursive DNS server** for the address → query **root server** to find the **authoritative DNS server** → authoritative server returns the IP address for the website → request passes through a **Web Application Firewall** → then through a **load balancer** → connect to the **web server** on port **80** or **443** → web server receives the **GET request** → **web application** queries the **database** → your **browser renders** the HTML into a viewable website.

---

## 🐧 4. Linux Fundamentals
   
### Linux Fundamentals Part 1

I had some exposure to **Linux** before starting this module. I’d used **Ubuntu** before to learn the basics and get comfortable setting up a Linux OS. I also tried **Kali** via **WSL** on Windows to explore some features. I've always enjoyed working with Linux, so this was exciting.

**Linux** powers websites, control panels, **Point of Sale (PoS)** systems, critical infrastructure like light controllers, and more.

Linux is based on the **UNIX OS** and is an umbrella term for many operating systems — like **Ubuntu**, **Kali**, **Debian**, and others. Ubuntu is commonly used for servers and only needs around **512MB of RAM**.

**TryHackMe** provided a browser-based Ubuntu machine to learn with. Since it's lightweight, navigation isn't done through a **GUI (Graphical User Interface)**, but through the **Terminal**, where we use commands. The module had me try:
- `echo` — outputs any text you provide
- `whoami` — shows the current user
- `ls` — lists files in the working directory
	- `ls file-name` — shows the contents of a specific file
- `cd` — changes directory
- `cat` — displays file contents
- `pwd` — prints the current working directory

For the task, I used these commands to explore folders, read their content, and confirm my current location in the file system.

Linux is great for efficiency — commands like `find` save time and effort:
- `find -name folder-name` — searches for a folder or file by name
- `find -name *.txt` — finds all `.txt` files
- `grep` — searches inside files for specific text
	- Example: `grep keyword filename`

**Basic operators** include:
- `&` — runs a command in the background
	- Example: `cp largefile.txt backup.txt &`
- `&&` — chains commands (the second only runs if the first succeeds)
	- Example: `mkdir new && cd new`
- `>` — redirects output and replaces file content
	- Example: `echo hey > welcome`
- `>>` — appends output without overwriting
	- Example: `echo more >> welcome`

### Premium-Only Content

- **Linux Fundamentals Part 2**
- **Linux Fundamentals Part 3**

---

## 🏢 5. Windows Fundamentals

### Windows Fundamentals Part 1

This part of module kicks off with a brief history of Windows OS, most notably it urges you to learn about difference between Home and Pro versions. I created this table to show the most relevant differences:
| Feature                            | Windows 11 Home                 | Windows 11 Pro                            | Why It Matters for SOC/Networking                             |
|------------------------------------|----------------------------------|--------------------------------------------|---------------------------------------------------------------|
| **BitLocker Encryption**           | ❌ Not available (only Device Encryption) | ✅ Full BitLocker with management tools      | Ensures disk security and supports forensic data protection   |
| **Domain Join / Azure AD**         | ❌ Not supported                | ✅ Join Active Directory & Azure AD         | Enables centralized access control and policy enforcement     |
| **Group Policy Editor**            | ❌ Not available                | ✅ Full access                              | Critical for pushing security configs across multiple devices |
| **Windows Update for Business**    | ❌ Not available                | ✅ Supported                                | Allows controlled update rollouts and patch management        |
| **Remote Desktop Host**            | ❌ Cannot host RDP sessions     | ✅ Can host Remote Desktop connections      | Supports remote incident response and admin tasks             |
| **Hyper-V & Windows Sandbox**      | ❌ Not available                | ✅ Both supported                           | Enables safe malware analysis and isolated test environments  |
| **Windows Information Protection** | ❌ Not available                | ✅ Included                                 | Helps prevent data leaks on enterprise systems                |

The current version of the Windows operating system for servers is [Windows Server 2025](https://www.microsoft.com/en-us/windows-server/).

In contrast to Linux Terminal, Windows has a GUI, which is briefly explained in this part of the module (I will not go over this here, as this is pretty surfice level information about Windows UI).

Windows uses a **file system** called **New Technology File System (NTFS)**. Before that, it used **FAT16/FAT32 (File Allocation Table)** and **HPFS (High Performance File System)**. USB devices, MicroSD cards, and more still use **FAT** today, but not personal machines.

**NTFS** is known as a **journaling** file system, which can, in case of failure, automatically repair folders/files by using information stored in a **log file** — something not possible with FAT.

NTFS supports specific **permissions** and **compression** for folders and files. It also uses **Encryption File System (EFS)**.

The module outlines how to check or **change permissions** for files, folders, or users, and explains what each permission means:
| **Permission**           | **Meaning for Folders**                                                         | **Meaning for Files**                                     |
| ------------------------ | ------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Read**                 | Permits viewing and listing of files and subfolders                             | Permits viewing or accessing the file’s contents          |
| **Write**                | Permits adding files and subfolders                                             | Permits writing to a file                                 |
| **Read & Execute**       | Permits viewing, listing, and executing files; inherited by files and folders   | Permits viewing, accessing, and executing the file        |
| **List Folder Contents** | Permits viewing, listing, and executing files; inherited by folders only        | N/A                                                       |
| **Modify**               | Permits reading and writing files and subfolders; allows deletion of the folder | Permits reading, writing, and deletion of the file        |
| **Full Control**         | Permits reading, writing, changing, and deleting files and subfolders           | Permits reading, writing, changing, and deleting the file |

NTFS also has a Windows-specific **Alternate Data Streams (ADS)** file attribute feature. Every file has at least one stream:
- Data stream named `\$DATA`,
- ADS allows files to contain multiple streams of data

**Windows Explorer** does not natively display ADS to users, but **PowerShell** lets you view ADS for files.

ADS is commonly used by **malware writers** to **hide data**, but not all uses are malicious. ADS do not affect a file’s **checksum** and are lost when the file is **compressed** (e.g., via ZIP or RAR), **Base64 encoded** (such as when sent via email), or transferred to a **FAT32**-formatted drive.
- **checksum** verifies a file’s integrity by generating a unique digital fingerprint based on its contents.

The **system environment variable** for the Windows directory is `%windir%`. According to Microsoft:
> *Environment variables store information about the operating system environment. This information includes details such as the operating system path, the number of processors used by the operating system, and the location of temporary folders.*

Typically, the Windows folder is located at `C:\Windows`, but not necessarily — `%windir%` ensures the correct path is used regardless of installation location.

One of the key folders inside the Windows directory is **System32**, which contains critical files required for the operating system to function properly. These include:
- **EXEs (Executable files):** Programs that run when opened, such as Task Manager (`taskmgr.exe`)
- **DLLs (Dynamic Link Libraries):** Shared code libraries used by multiple programs to perform common functions
- **Drivers:** Software components that allow the OS to communicate with hardware devices
- **Windows Registry:** A central database that stores system and application settings and configurations

### Windows  Fundamentals Part 2
### Windows  Fundamentals Part 3

---

## 📌 6. Key Takeaways

*To be completed at the end of the learning path.*

---

🔙 Back to [Writeups Overview](README.md)
