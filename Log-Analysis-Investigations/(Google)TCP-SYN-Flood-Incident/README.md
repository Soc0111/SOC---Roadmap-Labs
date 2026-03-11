# 🛡️ 11 Case Study : (Google)TCP SYN Flood Incident

Network Traffic Analysis: TCP SYN Flood Incident (Google Cybersecurity Professional Certificate)
### 📌 1) Project overview
This practical assignment was completed as part of the Google Cybersecurity Professional Certificate course. 
The goal of the project was to analyze abnormal network activity recorded in Wireshark logs, identify the type of attack, and compile a professional incident report.

### 🕵️ 2) Scenario
The company's website became unavailable to users, displaying a “Connection Timeout” error. 
As an information security specialist, I was tasked with examining the provided network logs (in .csv/.pcap format), identifying the cause of the failure, and describing the attack mechanism.

### 🛠 3) Tools and skills
Traffic analysis: Wireshark.

Data processing: Identification of malicious traffic patterns in TCP packets.

Documentation: Preparation of an incident report in accordance with SOC standards.

### 📊 4) Analysis results
The investigation revealed the following:

Attack type: TCP SYN Flood.

Attacker: IP address 203.0.113.0.

Target: Web server 192.0.2.1 (port 443).

Mechanism: Violation of the TCP Three-way Handshake process. The attacker overloaded the server's half-open connection queue, resulting in denial of service for legitimate users.

### 🧐 5) Project contents:
Wireshark_Log.csv — raw network activity data
Screenshots
