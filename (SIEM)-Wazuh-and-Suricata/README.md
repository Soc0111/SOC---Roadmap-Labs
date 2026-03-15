# 🛡️ Network Detection & SIEM Operations (Suricata & Wazuh)

## 📖 Project Overview
Welcome to the **Network Detection & SIEM** module! 🚀 This section of my portfolio is dedicated to advanced network security monitoring (NSM) and centralized log analysis. 

The primary goal of this directory is to demonstrate a full-cycle SOC workflow: from detecting raw network threats with **Suricata IDS** to aggregating, correlating, and alerting on those events within the **Wazuh SIEM** ecosystem.

Here, I perform:
* 📡 **Traffic Analysis:** Monitoring network interfaces for suspicious patterns and known attack signatures.
* 🧩 **SIEM Integration:** Forwarding IDS alerts to Wazuh for centralized visibility.
* 🔍 **Threat Hunting:** Using automated rules and manual log queries to identify advanced persistent threats (APT).

---

## 🛠️ Tech Stack & Skills

| Category | Tools & Technologies |
| :--- | :--- |
| **Intrusion Detection** | 🛡️ Suricata IDS (Signature-based & Protocol Detection) |
| **SIEM / XDR** | 🐺 Wazuh (Manager, Indexer, Dashboard) |
| **Traffic Source** | 🌐 Live Network Traffic, PCAP Replay |
| **Analysis** | 📊 JSON Parsing (`jq`), Regular Expressions, SIEM Dashboards |
| **Operating Systems** | 🐧 Kali Linux, Ubuntu Server (Wazuh Manager) |

---

## 📂 Investigation Index

This list will grow as I progress through the integration of IDS and SIEM components.

1. **[Case 01: Investigating Network Anomalies using Suricata IDS](./Investigating-Network-Anomalies-using-Suricata-IDS)** — 🚨 Initial setup of Suricata and first captured logs analyzing network reconnaissance and Kali Linux presence.
2. **[Case 02: (SIEM)-Wazuh-Lab](/((SIEM)-Wazuh)) 🏗️ Setting up the SIEM core to receive logs from remote agents.


---

## 💡 SOC Perspective
> **Why this matters:** In a modern SOC environment, standalone logs are not enough. By combining **Suricata's** deep packet inspection with **Wazuh's** correlation engine, we transform raw data into actionable intelligence, significantly reducing the Mean Time to Detect (MTTD).

---

**Status:** 🏗️ Under Active Development | **Focus:** Network Security & Monitoring
