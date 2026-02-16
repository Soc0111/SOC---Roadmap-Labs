# Case Study 04: Compromised Account & Unauthorized User Creation 🛡️

## 1. Executive Summary
I identified a high-criticality incident involving the compromise of a management-level account. The attacker used the compromised credentials to create a new administrative user, establishing a persistent backdoor in the system.

## 2. Evidence (Raw Logs)
Critical events identified in `/var/log/auth.log`:


Feb 16 03:15:22 server sshd[202]: Accepted password for anya from 103.25.100.44
Feb 16 03:16:05 server sudo: anya : COMMAND=/usr/bin/useradd -m backup_admin
Feb 16 03:16:10 server sudo: anya : COMMAND=/usr/bin/passwd backup_admin

## 3.Technical Analysis & Investigation
Phase 1: Account Takeover (ATO)
Observation: A successful login for user anya from an unknown IP (103.25.100.44) at 03:15 AM.
Conclusion: Unusual login time and location indicate a compromised credential (likely via phishing or credential stuffing).

Phase 2: Backdoor Creation
Observation: The attacker used sudo to create a new user backup_admin.
Conclusion: This is a classic "Persistence" technique. Even if the anya account is secured, the attacker can still return using the newly created backup_admin.

## 4. Security Recommendations
Multi-Factor Authentication (MFA): Enforce MFA for all accounts, especially those with sudo privileges.
Geofencing: Block SSH logins from IP ranges outside of the company's operating regions.
