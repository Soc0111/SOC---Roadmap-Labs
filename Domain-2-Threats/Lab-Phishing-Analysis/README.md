Lab: Analyzing Phishing Domain Queries

Objective
To identify suspicious DNS activity and differentiate between generic phishing and spear-phishing attempts.

Scenarios
I analyzed how attackers use Typosquatting to deceive users. 
Example targets for "GlobalBank":
1. `global-bank-support.com` (Subdomain trick)
2. `g1obalbank.com` (Character substitution)
3. `global-bank.ua.security-check.in` (Look-alike domain)

Tools
* Wireshark 

Detection Method (Wireshark Filters)
To find these threats in a corporate network, I use the following display filters:
* `dns.qry.name contains "bank"` — to find any DNS requests for bank-related domains.
* `http.host contains "bank"` — to catch unencrypted HTTP traffic to suspicious hosts.

Key Takeaways
* Attackers use Urgency and Authority as psychological triggers.
* Spear-phishing is more dangerous as it targets specific roles (e.g., SOC analysts or HR).
