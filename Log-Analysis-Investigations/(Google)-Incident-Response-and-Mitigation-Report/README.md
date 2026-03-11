# 👾 Case 14: (Google) Incident Response and Mitigation (ICMP DoS Attack)

## ✅ 1) Incident Summary
**Organization:** Multimedia Company (Web Design & Marketing)  
**Event Type:** Denial of Service (DoS) via ICMP Flood  
**Duration:** 2 hours  
**Impact:** Total internal network paralysis; critical services became unresponsive to legitimate traffic.

A malicious actor exploited a misconfigured firewall to flood the network with ICMP packets. The Incident Management Team responded by blocking incoming ICMP traffic, offlining non-critical services, and gradually restoring the network perimeter.

## 📌 2) NIST Cybersecurity Framework Analysis

Following the National Institute of Standards and Technology (NIST) CSF, I analyzed the incident to improve the organization's security posture:

1. Identify
* **Attack Vector:** ICMP Flood (Ping Flood).
* **Vulnerability:** Unconfigured firewall allowing unrestricted inbound ICMP echo requests.
* **Affected Assets:** Internal network infrastructure, boundary firewall, and centralized network resources.

2. Protect
To prevent recurrence, the following controls were implemented:
* **Firewall Rate Limiting:** New rules to limit the volume of incoming ICMP packets.
* **Source Verfication:** Implementation of IP address validation to filter out spoofed ICMP packets.
* **Hardening:** Disabling unnecessary ICMP types at the network boundary.

3. Detect
* **Network Monitoring:** Deployment of monitoring software to identify abnormal traffic patterns and trigger real-time alerts.
* **IDS/IPS Implementation:** Configured an Intrusion Detection/Prevention System to drop ICMP traffic that exhibits suspicious characteristics (e.g., unusual packet size or frequency).

4. Respond
* **Containment:** Immediate blocking of the malicious ICMP flood at the firewall level.
* **Neutralization:** Isclating non-critical services to preserve bandwidth for emergency restoration.
* **Analysis:** Reviewing firewall logs and IDS signatures to determine the source and scope of the attack.

5. Recover
* **Service Restoration:** Gradual restoration of critical network services, followed by non-critical assets.
* **Data Integrity:** Verified that no data was exfiltrated during the flood (as DoS is primarily an availability attack).
* **Post-Incident Review:** Documented the event to update the "Incident Response Plan" for future readiness.
