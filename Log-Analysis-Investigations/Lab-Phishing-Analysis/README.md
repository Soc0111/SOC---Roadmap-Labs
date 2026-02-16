# Case Study 03: Phishing Domain Analysis — Identifying Typosquatting 

## 1. Executive Summary
A user reported a suspicious email requesting an urgent password reset for the corporate banking portal. Upon investigation of the DNS logs, I identified a query to a malicious domain designed to look like the legitimate "my-bank.com". This case demonstrates a "Typosquatting" attack intended to harvest user credentials.

## 2. Evidence (Raw DNS Logs)
The following logs were extracted from the internal DNS server:


Feb 16 10:20:15 dns-srv: query: user-pc-01.local IN A my-bannk.com
Feb 16 10:20:15 dns-srv: response: my-bannk.com is 45.33.22.11
Feb 16 10:20:16 dns-srv: query: user-pc-01.local IN A google.com
Feb 16 10:20:16 dns-srv: response: google.com is 142.250.190.46

## 3. Technical Analysis & Investigation
Phase 1: Identifying Typosquatting
Observation: The legitimate domain is my-bank.com. The logs show a request for my-bannk.com (note the double 'n').
Conclusion: This is a classic Typosquatting (or URL hijacking) attack. The attacker registered a similar-looking domain to deceive users who may not notice a small spelling error.

Phase 2: Domain Intelligence
Observation: The malicious domain resolves to IP 45.33.22.11.
Investigation: Using OSINT tools (VirusTotal/Whois), the IP was found to be located in a high-risk jurisdiction and has been previously flagged for hosting phishing pages.
Conclusion: The site is a cloned version of the bank's login page, designed to steal login/password combinations and MFA tokens.

Phase 3: Scope of Impact
Outcome: Only one host (user-pc-01) was found to have contacted the malicious domain. No further internal propagation was detected.

## 4. Security Recommendations
Email Filtering: Enhance the "Anti-Phishing" rules on the mail gateway to flag domains with high similarity to corporate assets.
Security Awareness Training: Conduct a simulation to teach employees how to hover over links and check for spelling anomalies.
DNS Filtering: Implement a protective DNS service (like Cisco Umbrella or Cloudflare Gateway) to block known malicious domains automatically.
