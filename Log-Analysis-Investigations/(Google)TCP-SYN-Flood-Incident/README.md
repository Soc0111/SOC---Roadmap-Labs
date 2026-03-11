# 🛡️ Case Study 11: (Google) TCP SYN Flood Incident

This case study focuses on analyzing and documenting a network-based TCP SYN Flood attack detected through traffic logs.

---

## 📌 1) Project overview

This practical assignment was completed as part of the Google Cybersecurity Professional Certificate course. The goal of the project was to analyze abnormal network activity recorded in Wireshark logs, identify the type of attack, and compile a professional incident report.

---

## 🕵️‍♂️ 2) Scenario

The company's website became unavailable to users, displaying a "Connection Timeout" error. As an information security specialist, I was tasked with examining the provided network logs (in .csv/.pcap format), identifying the cause of the failure, and describing the attack mechanism.

---

## 🛠️ 3) Tools and skills

* **Traffic analysis:** Wireshark.
* **Data processing:** Identification of malicious traffic patterns in TCP packets.
* **Documentation:** Preparation of an incident report in accordance with SOC standards.

---

## 📊 4) Analysis results

The investigation revealed the following:
* **Attack type:** TCP SYN Flood.
* **Attacker:** IP address 203.0.113.0.
* **Target:** Web server 192.0.2.1 (port 443).
* **Mechanism:** Violation of the TCP Three-way Handshake process. The attacker overloaded the server's half-open connection queue, resulting in denial of service for legitimate users.

---

## 🖼️ 5) Proof of Attack: WireShark Screenshot

Below is a capture from WireShark showing the high volume of incoming `[SYN]` packets from a single source, which are never completed with an `[ACK]`.

<img src="https://github.com/Sec0111/SOC---Roadmap-Labs/blob/main/Log-Analysis-Investigations/Google-TCP-SYN-Flood-Incident/photo_2026-02-23_21-59-43.jpg" alt="WireShark SYN Flood Screenshot" width="100%">

*Figure 1: High-volume SYN flood capture targeting web server port 443 from IP 203.0.113.0.*

---

## 📁 6) Project contents:

* **Wireshark_Logs.csv** — raw network activity data.
* **Screenshots** — embedded directly into this document for easier viewing.

---

**Status:** 🟢 Analysis Complete | **Focus:** DDoS & Network Forensics
