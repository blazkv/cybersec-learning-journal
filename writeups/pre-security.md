# TryHackMe - Pre Security

The **Pre Security** path on TryHackMe covers essential technical knowledge to get started in cyber security. While I'm already familiar with much of the content from my Information Security studies and the Cyber Security 101 path, I'm using this as a refresher to reinforce my knowledge and catch any gaps I may have missed.

---

## 📌 1. Introduction to Cybersecurity

This module introduced me to the core concepts of **cybersecurity**, divided into two main areas: **Offensive Security** and **Defensive Security**.

It began with **Offensive Security**, explored through a mock online bank simulation. I was challenged to compromise a fake bank account by working in a simulated Ubuntu terminal. I used the **derb** command to perform **directory enumeration**, which revealed two vulnerable URLs. I then exploited those URLs to deposit money into the account. While I was already comfortable using the terminal, this was my first time using **derb**, and it sparked an interest in learning more about similar tools used in real-world penetration testing.

The second part focused on **Defensive Security**, which is commonly associated with the **Blue Team**. This section introduced two key components of defensive work: the **Security Operations Center** and **Digital Forensics and Incident Response**.

The **Security Operations Center**, or **SOC**, is responsible for monitoring and defending systems against vulnerabilities, unauthorized activity, policy violations, and network intrusions. One of the SOC’s essential functions is **Threat Intelligence**, which involves gathering and analyzing information about potential adversaries and their tactics. This intelligence helps teams build **threat-informed defenses**. Data for this analysis comes from both internal sources like logs and external sources such as public feeds and forums.

**Digital Forensics and Incident Response**, or **DFIR**, is made up of several key areas. **Digital Forensics** involves investigating evidence from attacks and identifying the attackers by analyzing file systems, system memory, system logs, and network traffic. **Incident Response** focuses on reducing damage and ensuring fast recovery when an attack happens. This process typically includes four phases: preparation, detection and analysis, containment and recovery, and post-incident review. The final area, **Malware Analysis**, involves studying malicious software using either **static analysis**, where the code is reviewed without running it, or **dynamic analysis**, where it is executed in a controlled environment to observe its behavior.

The module concluded with a practical SOC simulation. I worked within a simplified **SIEM platform** to detect a malicious log entry. After identifying the threat, I investigated the IP address using a fake scanner site modeled after real tools like **AbuseIPDB** and **Cisco Talos Intelligence**. The final steps were to escalate the incident to a SOC analyst lead and block the IP address, simulating a complete response cycle.

---

## 📌 2. What is Networking?

The first task introduced the concept of a **network**. In computing, a network can consist of as few as two devices or scale up to billions. This was demonstrated through a visual example showing three people forming their own connected network to represent how devices share information.

From there, I moved on to the **internet**, which was described as one massive network made up of countless smaller networks. The concept was reinforced using another illustration, where two individuals could only talk to each other through a third person, reflecting how **public networks** can serve as bridges between **private networks**.

The next task focused on **identifying devices on a network**, which is done using two main identifiers: the **IP address** and the **MAC address**.

An **IP address** is a numerical label assigned to each device. There are **private IPs** used within local networks and **public IPs** used for communication over the internet. Devices on the same private network share a public IP when going online, usually provided by the **ISP**. I learned that while **IPv4** is still widely used, the internet is shifting to **IPv6** due to limited available IPv4 addresses.

A **MAC address** is a hardware-based identifier tied to a device’s network interface. It is a 12-character hexadecimal value that is unique to each device, like **a4\:c3\:f0:85\:ac:2d**. While factory-assigned, **MAC spoofing** can be used to imitate another device, which could be used to bypass poorly implemented security measures.

This task included a **spoofing simulation**, where I changed one device's MAC address to impersonate another, providing hands-on practice with how spoofing can work in a real-world scenario.

After that, I learned about **Ping and ICMP**, two fundamental tools for checking network connectivity. **Ping** sends **ICMP packets** between devices to determine whether they are reachable and how responsive they are. This is one of the most commonly used commands in networking. I practiced using the **ping** command to check connectivity with both local and public devices. For example, I ran `ping 8.8.8.8` on a simulated website provided within the module to see how long it took for packets to travel and return.

The final task was meant to introduce **LANs**, or **Local Area Networks**, but I was unable to complete it since it is part of the **premium content**. Other related rooms, including **OSI Model**, **Packets and Frames**, and **Extending Your Work**, are also locked behind a subscription.

---

## 📌 3. How the Web Works

This part of the module helped me build a clear picture of how DNS and HTTP work together to power everyday browsing.

I began with **DNS (Domain Name System)**, learning that it’s like the internet’s phonebook, turning hard-to-remember **IP addresses** into human-readable **domain names** like `tryhackme.com`. This translation allows users to access websites without needing to remember numeric addresses.

Digging deeper, I explored the makeup of domain names. A **Top-Level Domain (TLD)** like `.com` or `.org` comes at the end. Just before that is the **Second-Level Domain**, which is the main name of the site (e.g., “tryhackme”). I also learned about **subdomains**, which allow for organization within a domain, like `admin.tryhackme.com`.

Next, I got familiar with different **DNS record types** and what they’re used for. **A Records** point domain names to **IPv4 addresses**, while **AAAA Records** do the same for **IPv6**. **CNAME Records** redirect one domain to another, and **MX Records** route email to the correct server. **TXT Records** store text information, often used for domain verification or email security.

Understanding how a **DNS request** works helped connect everything. My computer first checks a local cache. If the answer isn’t there, it asks a **recursive DNS server**, usually from my ISP. That server contacts **root servers**, then the **TLD servers**, and finally the **authoritative server**, which provides the final answer. That result gets cached for a time defined by **TTL (Time To Live)** to speed up future lookups.

To apply all this, I used **nslookup** in the terminal to query different record types like **A**, **CNAME**, **MX**, and **TXT**. It was a hands-on way to see how these concepts play out in real time.

Moving into **HTTP and HTTPS**, I saw how browsers communicate with web servers. **HTTP (HyperText Transfer Protocol)** is the standard for sending and receiving data online. **HTTPS** adds encryption, making it safer by protecting the data from being intercepted.

To access any content on a website, a browser uses a **URL (Uniform Resource Locator)** to find it. I learned that a URL can contain several elements: the **scheme** (like HTTP or HTTPS), **user** credentials if needed, the **host** (domain name or IP), **port** number, the **path** to the resource, a **query string** with extra info, and a **fragment** pointing to a specific part of the page.

When a request is made, the browser usually uses the **GET** method, and it includes **headers** to provide extra context. Since I have a bit of backend web development experience, this part felt familiar. I’d used methods like GET and POST while building and testing routes, so understanding how browsers and servers “talk” in structured requests and responses tied in nicely with what I’ve seen in practice.

I then looked into **HTTP methods**, which define what the client wants the server to do. **GET** is for retrieving data, **POST** is used to send data (like filling out a form), **PUT** updates existing data, and **DELETE** removes data. While there are many methods, GET and POST are by far the most commonly used in everyday browsing and development.

I also explored **HTTP status codes**, which the server sends back to tell the browser what happened with the request. The most familiar ones were **200 OK** (success), **404 Not Found** (the page doesn’t exist), **301** and **302** for redirects, **400** for bad requests, **403 Forbidden**, and **500 Internal Server Error**. Knowing these codes helps a lot with debugging issues in web development.

Finally, I wrapped up with **HTTP headers**, which are extra pieces of information exchanged between the browser and server. On the client side, **request headers** include **Host**, **User-Agent**, **Content-Length**, **Accept-Encoding**, and **Cookie**. These tell the server what website you're trying to reach, what browser you’re using, what data is being sent, how it’s compressed, and session info.

On the server side, **response headers** like **Set-Cookie**, **Cache-Control**, **Content-Type**, and **Content-Encoding** manage browser behavior. This includes everything from saving login sessions to telling the browser how long to cache content and what kind of file is being returned.

---

## 📌 4. Linux Fundamentals

---

## 📌 5. Windows Fundamentals

---

🔙 Back to [Writeups Overview](README.md)
