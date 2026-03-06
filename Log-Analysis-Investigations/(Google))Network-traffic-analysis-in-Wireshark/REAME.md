## Network Traffic Analysis in Wireshark (Lab Report) (Images are included near README)
## 🎯 Project Overview
The purpose of this lab is to perform an in-depth analysis of pre-captured network traffic (.pcap) to identify protocols, 
filter suspicious activity, and study the structure of packets at different levels of the OSI model in detail.

## 🛠 Tools
Wireshark: The main traffic analysis tool.

OSI Model Knowledge: Applying theory in practice (L2-L7).

## 🚀 Main steps and skills
## 1. Traffic navigation and filtering
Display filters: Narrowed down the sample to specific hosts and protocols.

ip.addr == 142.250.1.139 — isolation of target server traffic.
dns — search for name resolution requests.
tcp.port == 80 — analysis of unprotected HTTP traffic.

## 2. Detailed analysis of packet structure (Deep Packet Inspection)
Inspected encapsulation levels:

Ethernet II (L2): Analysis of source and destination MAC addresses.
IPv4 (L3): IP header verification, sender identification.
TCP/UDP (L4): Analysis of ports and flags.
Application Layer (L7): Extraction of payload from HTTP and DNS requests.

## 3. Protocol analysis
DNS (Domain Name System): Investigated the domain name resolution process for google.com. Identified requests (Standard query) and server responses.
TCP Handshake: Analyzed the connection establishment process (SYN, SYN-ACK, ACK).
ICMP: Investigated echo requests (Echo (ping) requests) to check node availability.

## 4. Working with Payload
Studied the contents of data segments in hexadecimal (Hex) and ASCII formats.
Demonstrated the ability to find specific text strings within network packets, which is critical for SOC analysts when searching for indicators of compromise (IoC).

## 💡 Conclusion
During the lab, I reinforced my skills in working with Wireshark as a primary security tool. 
I learned how to quickly find the necessary packets among thousands of records, analyze protocol handshakes, and understand how data is encapsulated when transmitted over a network.
