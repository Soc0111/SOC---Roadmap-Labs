# 🎭 Cyber Threat Simulation & Analysis

### This section is dedicated to researching offensive security tactics, understanding how they impact systems, and developing effective defensive strategies.

---

## 🛠️ Tech Stack & Skills

* **Simulations:** Ransomware behavior, Crontab persistence, Brute-force attacks, **Denial-of-Service (DoS), TCP/UDP Flooding**.
* **Network Analysis:** DNS investigation, Typosquatting, **Packet fragmentation, Protocol flag manipulation, Stealth & Connect scanning**.
* **Incident Response:** Containment, Eradication, and Recovery (NIST Framework), **Playbook development**.
* **Tools:** Python 🐍, Bash, Linux Auth Logs, Wireshark 🦈, **Scapy, Nmap, SIEM Logic (Wazuh/ELK)**.

---

## 📑 Investigation Index

1. **[Case 01: SSH Brute Force & Compromise](./SSH-BruteForce-Analysis)** — Analyzing unauthorized access attempts and implementing a full Incident Response Plan.
2. **[Case 02: Persistence via Cron](./Lab-Persistence-Crontab)** — Simulating malicious scheduling to maintain long-term access to a Linux system.
3. **[Case 03: Phishing Domain Analysis](./Lab-Phishing-Analysis)** — Identifying typosquatting and suspicious DNS queries using network traffic analysis.
4. **[Case 04: Ransomware Simulation](./Lab-Ransomware-Simulation)** — Behavioral analysis of file encryption and renaming patterns on Linux.
5. **[Case 05: IP Fragmentation (frag_scan)](./Fragmented-Scan)** — Detecting IDS evasion techniques through fragmented packet analysis.
6. **[Case 06: UDP Flood DoS](./UDP-Flood-Denial-of-Service%20(DoS))** — Analyzing volumetric attacks and implementing rate-limiting defenses.
7. **[Case 07: TCP RST Flood](./TCP-RST-Flood-(Connection-Reset-Attack))** — Investigating session disruption via forced TCP termination and stateful hardening.
8. **[Case 08: TCP Connect Scan Detection](./TCP-Connect-Scan-Detection)** — Identifying active reconnaissance and full handshake discovery patterns.
9. **[Case 09: UDP Port Scanning & Recon](./UDP-Port-Scanning-and-Reconnaissance)** — Analyzing stateless scanning methods and service discovery on UDP ports.
10. **[Case 10: Service Fingerprinting](./Service-Fingerprinting-and-Banner-Grabbing)** — Detecting banner grabbing and preventing sensitive version disclosure.

---

> [!TIP]
> Each lab contains a detailed report, terminal evidence, and a **SOC Perspective** section on how to detect and mitigate these specific threats using modern security controls.

---

**Status:** 🟢 All Labs Completed | **Focus:** Advanced Threat Vectors & Mitigation
