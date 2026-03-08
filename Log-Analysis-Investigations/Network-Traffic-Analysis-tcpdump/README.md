## Network Traffic Analysis: tcpdump
## 🛡️ Project Overview
This laboratory work focuses on capturing and analyzing live network traffic using **tcpdump** in a Linux environment. As a SOC Analyst, the ability to intercept, filter, and inspect packets is fundamental for detecting anomalies, investigating incidents, and performing network forensics.

## 🛠️ Tools Used
* **Linux Terminal** (Ubuntu/Debian-based)
* **tcpdump**: Command-line packet analyzer.
* **curl**: Tool for generating HTTP traffic.
* **ifconfig / ip addr**: Network interface configuration tools.

---

## 🚀 Lab Workflow

### Phase 1: Network Interface Identification
The first step in any capture is identifying where the traffic flows.

Identify available interfaces
sudo tcpdump -D
Goal: Determine the active interface (e.g., eth0) for monitoring.

### Phase 2: Live Traffic Inspection
Inspecting traffic in real-time to understand the current network state.

Capture 5 packets from eth0 with verbose output
sudo tcpdump -i eth0 -v -c5
Key Flags:
-i: Specifies the interface.
-v: Enables verbose output (TTL, IP ID, Length).
-c5: Limits capture to 5 packets to prevent terminal overflow.

### Phase 3: Targeted Capture (HTTP)
Capturing specific traffic and saving it for offline analysis — a standard SOC procedure.

Capture 9 HTTP packets (port 80) and save to PCAP
sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap &
The Workflow:
Started tcpdump in the background (&).

### Phase 4: Forensic Analysis (Reading PCAP)Analyzing the "crime scene" (PCAP file) without affecting the live network.
1)Command tcpdump -nn -r capture.pcap -v;
Purpose Standard analysis of headers and protocols.

2)Command tcpdump -nn -r capture.pcap -X
Purpose Deep inspection: View payload in HEX and ASCII.
