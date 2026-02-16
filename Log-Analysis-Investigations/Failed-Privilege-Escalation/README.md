# Case Study: Internal Threat — Failed Privilege Escalation Attempt 

## 1. Executive Summary
I detected an unauthorized attempt to access the system's password hash file (`/etc/shadow`) by a non-administrative user. Although the attempt was blocked by the system's security controls, it indicates a clear intent to escalate privileges.

## 2. Evidence (Raw Logs)
Events captured in the authentication logs:


Feb 16 15:45:10 forge-srv sudo: tech-priest : COMMAND=/usr/bin/cat /etc/shadow
Feb 16 15:45:11 forge-srv sudo: pam_unix(sudo:auth): authentication failure; logname= uid=1001 euid=0 user=tech-priest

## 3. Technical Analysis & Investigation
Phase 1: High-Risk Command Detection
Observation: User tech-priest attempted to use sudo cat on the /etc/shadow file.
Conclusion: This file contains encrypted user passwords. Accessing it is a primary goal for attackers looking to perform offline password cracking.

Phase 2: Authentication Failure
Observation: The command failed with an "authentication failure" message.
Conclusion: The system successfully prevented the unauthorized access because the user did not have the necessary sudo permissions or failed to provide the correct password.

## 4. Security Recommendations
Audit Sudoers File: Ensure that no regular users have even partial access to sensitive commands.
SIEM Alerting: Configure the SIEM to trigger a "High" severity alert whenever a user attempts to access /etc/shadow.
