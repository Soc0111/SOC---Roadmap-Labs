# Case Study 10: Automated Scanner Detection & Internal Reconnaissance

## 1. Executive Summary
During an analysis of HTTP User-Agent strings, I identified multiple automated security scanning tools targeting the web infrastructure. More critically, an internal IP address was detected using a specialized SQL injection tool, suggesting either a compromised internal host or a malicious insider.

## 2. Evidence (User-Agent Logs)

1. 192.168.1.50 - [17/Feb/2026:10:05:20] "GET /login.php HTTP/1.1" 200 2400 "sqlmap/1.4.11"
2. 80.92.32.11 - [17/Feb/2026:10:10:05] "GET /index.php HTTP/1.1" 200 1500 "Nikto/2.1.6"
3. 5.188.10.5 - [17/Feb/2026:10:15:00] "GET /admin/login.php HTTP/1.1" 403 150 "Nmap Scripting Engine"

## 3. Technical Analysis
Phase 1: Identifying Offensive Tools
Sqlmap (Internal IP): An internal host initiated a scan against the login portal. Sqlmap is designed to automate the exploitation of SQL injection vulnerabilities.
Nikto & Nmap: External IPs used automated vulnerability scanners to map the server's attack surface and look for misconfigurations.

Phase 2: Internal Threat Analysis
The use of sqlmap from an internal range (192.168.x.x) is a high-severity alert. It indicates Lateral Movement (an attacker moving inside the network) or an Insider Threat.

## 4. The User-Agent field provides critical evidence of Instrumentality. 
While IP addresses show who (roughly), the User-Agent shows what weapon was used. 
From a legal standpoint, using specialized hacking tools like sqlmap or Nikto demonstrates clear malicious intent, which is essential for escalating the case to legal authorities or internal HR.
