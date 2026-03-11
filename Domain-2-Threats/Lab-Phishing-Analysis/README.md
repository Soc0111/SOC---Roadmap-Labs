# 🎣 Phishing Domain Analysis & DNS Investigation

## 🎯 Project Objective
The goal of this lab is to identify suspicious DNS activity and differentiate between generic phishing and targeted spear-phishing attempts. I focused on analyzing **Typosquatting** techniques used by attackers to deceive users and bypass visual inspection.

---

## 🛠️ Tech Stack & Tools
| Component | Details |
| :--- | :--- |
| **Tool** | 🦈 Wireshark (Network Protocol Analyzer) |
| **Protocol** | 🌐 DNS, HTTP |
| **Focus** | 🔍 Threat Hunting / Traffic Analysis |

---

## 📂 Attack Scenarios: Typosquatting Analysis
During the investigation, I analyzed how attackers manipulate domains to mimic a legitimate organization (e.g., "GlobalBank"):

1.  **Subdomain Trick:** `global-bank-support.com` — Using hyphens and keywords to create a sense of legitimacy.
2.  **Character Substitution:** `g1obalbank.com` — Replacing letters with similar-looking numbers (Homoglyph attack).
3.  **Look-alike Domain:** `global-bank.ua.security-check.in` — Using a complex structure to hide the actual top-level domain.

---

## 🔍 Detection Methodology (Wireshark)
To identify these threats in a corporate network environment, I utilized specific **Display Filters** to isolate suspicious traffic:

* `dns.qry.name contains "bank"` — Filters all DNS queries related to bank-related keywords.
* `http.host contains "bank"` — Identifies unencrypted HTTP traffic directed to suspicious hosts.

> [!TIP]
> **Key Takeaway:** Attackers often use **Urgency** and **Authority** as psychological triggers. From a technical standpoint, spear-phishing is significantly more dangerous as it targets specific roles like SOC Analysts or HR.

---

## 🛡️ SOC Analyst Perspective: Prevention & Defense

### 1. Technical Controls
* **DNS Filtering:** Implement DNS protection services (e.g., Cisco Umbrella, NextDNS) to block known malicious and newly registered domains.
* **Email Security:** Use SPF, DKIM, and DMARC records to verify sender identity and filter spoofed emails.

### 2. Behavioral Analysis
* Monitor for "Newly Registered Domains" (NRDs) in organization logs, as many phishing sites are live for less than 24 hours.

### 3. Awareness
* Conduct regular phishing simulations to train employees on spotting visual discrepancies in URLs.

---
**Status:** 🟢 Completed | **Focus:** Social Engineering & Traffic Analysis
