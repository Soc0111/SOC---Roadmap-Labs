# 🔍 Web Server Log Analysis & Threat Detection

This section focuses on using Linux CLI tools to parse, filter, and analyze web server logs to identify potential security threats and unauthorized access patterns.

---

## 🛠️ Tech Stack & Skills

* **Tools:** `Bash`, `awk`, `grep`, `cat`
* **Analysis:** Log Parsing, Data Isolation, Event Correlation.
* **Incident Response:** Reporting unauthorized access (403 Forbidden) and suspicious POST requests.
* **Log Format:** Standard Web Server Access Logs.

---

## 📂 Investigation Index

### Level 1: Data Isolation 🎯
**Task:** Extract only the IP addresses of all visitors to identify the unique sources of traffic.
* **Command:** `cat logs.txt | awk '{print $1}'`

### Level 2: Event Correlation 📊
**Task:** Display the IP address alongside the corresponding server response status code to find failed requests.
* **Command:** `cat logs.txt | awk '{print $1, $9}'`

### Level 3: Attack Vector Filtering ⚔️
**Task:** Identify all suspicious `POST` requests, which could indicate attempts to upload malicious files or bypass login forms.
* **Command:** `cat logs.txt | grep -i "post" | awk '{print $1}'`

### Level 4: Custom Notifications (Reporting) 📢
**Task:** Filter for `403 (Forbidden)` errors and generate a human-readable incident report for SOC monitoring.
* **Command:** `cat logs.txt | grep "403" | awk '{print "WARNING: IP " $1 " tried to access " $7 " - Access Denied"}'`

### Level 5: Deep Time Analysis (Advanced) ⏱️
**Task:** Extract the exact time of each request using double separators for precise forensic timeline creation.
* **Command:** `cat logs.txt | awk '{print $4}' | awk -F ":" '{print $2":"$3":"$4}'`

---

> [!TIP]
> **SOC Perspective:** Mastering `awk` and `grep` allows a SOC Analyst to quickly triage large log files during an active incident without relying on heavy GUI tools.

---

## 📝 Evidence & Analysis Sample

### Logs used for analysis:
```text
192.168.1.10 - - [03/Mar/2026:12:00:01] "GET /index.html" 200 1234
192.168.1.10 - - [03/Mar/2026:12:05:30] "POST /login" 401 532
192.168.1.20 - - [03/Mar/2026:12:10:15] "GET /admin" 403 231
192.168.1.10 - - [03/Mar/2026:12:15:00] "GET /favicon.ico" 200 450
192.168.1.10 - - [03/Mar/2026:12:20:45] "GET /style.css" 200 3200
192.168.1.10 - - [03/Mar/2026:12:25:12] "POST /login" 200 120
192.168.1.50 - - [03/Mar/2026:12:30:05] "GET /api/data" 500 999
192.168.1.10 - - [03/Mar/2026:12:35:00] "POST /upload" 403 0
