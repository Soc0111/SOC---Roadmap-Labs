Project Title:
Compromised Web Host: Brute Force Attack & Malware Redirection Analysis

Overview:
This project is dedicated to investigating a security incident involving the web resource yummyrecipesforme.com. During the course of the work, a full cycle of analysis was carried out: from detecting anomalies to developing recommendations for strengthening protection (hardening).

Key Objectives:
Incident Investigation: Analysis of the actions of an attacker who gained access through a brute force attack on the administrator account with the default password.

Traffic Analysis: Use of tcpdump in an isolated environment (sandbox) to track the chain of events: from the DNS query to the download of malicious software and redirection to a phishing domain.

Protocol Identification: Analysis of network interaction at the TCP/IP model levels (DNS, HTTP, TCP).

Remediation: Develop a defense strategy to prevent repeat attacks, including the implementation of MFA and login attempt restriction policies.

Tools Used:
tcpdump (Network Packet Analysis)
Sandbox Environment (Safe Malware Execution)
