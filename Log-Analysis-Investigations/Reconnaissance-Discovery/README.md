# Case Study 03: Reconnaissance & System Enumeration 

## 1. Executive Summary
During log analysis, I detected suspicious activity from a restricted `guest` account. The user performed system enumeration, checking for installed network tools and OS version details. This is a typical reconnaissance phase preceding a targeted attack.

## 2. Evidence (Raw Logs)
Logs captured from the bash history and system events:


Feb 16 18:10:05 srv-web sshd[9001]: Accepted password for guest from 192.168.1.100
Feb 16 18:11:10 srv-web bash[9005]: nmap: command not found
Feb 16 18:11:15 srv-web bash[9006]: nc: command not found
Feb 16 18:11:20 srv-web bash[9007]: whoami: user=guest
Feb 16 18:11:30 srv-web bash[9008]: cat /etc/issue: Ubuntu 22.04.1 LTS

## 3 Technical Analysis & Investigation
Phase 1: Tool Discovery
Observation: The user tried to execute nmap and nc (netcat).
Conclusion: The attacker was looking for pre-installed tools to scan the internal network or establish a connection. The "command not found" errors indicate these tools were missing.

Phase 2: System Fingerprinting
Observation: The execution of whoami and cat /etc/issue.
Conclusion: The attacker confirmed their current low-privilege status and identified the exact OS version to search for specific kernel exploits (Privilege Escalation).

## 4 Security Recommendations
Restrict Access: Implement a restricted shell (rbash) for temporary or guest accounts.
Logging: Enable detailed command logging (Auditd) to monitor all user actions in real-time.
