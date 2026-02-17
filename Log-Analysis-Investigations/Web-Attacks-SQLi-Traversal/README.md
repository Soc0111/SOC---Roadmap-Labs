# Case Study 08: Web Application Attacks — SQLi & Path Traversal

## 1. Executive Summary
During a review of Nginx access logs, I identified a series of malicious web requests originating from a single source IP. The attacker attempted to perform a Path Traversal attack to read system files and successfully executed an SQL Injection (SQLi) attack, resulting in a significant data leak.

## 2. Evidence (Web Server Logs)
The following logs were extracted from `/var/log/nginx/access.log`:

1. 192.168.1.77 - - [16/Feb/2026:14:00:05] "GET /search.php?id=10 HTTP/1.1" 200 850
2. 192.168.1.77 - - [16/Feb/2026:14:00:10] "GET /search.php?id=10' OR '1'='1 HTTP/1.1" 200 12500
3. 192.168.1.77 - - [16/Feb/2026:14:00:15] "GET /etc/passwd HTTP/1.1" 404 230
4. 192.168.1.77 - - [16/Feb/2026:14:01:10] "GET /admin/config.php HTTP/1.1" 403 150

## 3. Technical Analysis & Investigation
Phase 1: Successful SQL Injection (Critical)
Observation (Row 2): The request contains the payload ' OR '1'='1. This is a classic SQLi technique to bypass database logic.
Success Indicator: The HTTP Status is 200 OK, and the response size increased from 850 bytes to 12,500 bytes.
Conclusion: The attack was successful. The database returned a large volume of unauthorized data (likely a full table dump).

Phase 2: Attempted Path Traversal & Admin Recon
Observation (Row 3 & 4): The attacker tried to access /etc/passwd (Linux system file) and /admin/config.php.
Success Indicator: Status 404 (Not Found) and 403 (Forbidden).
Conclusion: These attempts failed. However, they demonstrate clear malicious intent to escalate the attack by finding system credentials.

## 4. Security Recommendations
WAF (Web Application Firewall): Deploy a WAF to automatically block common SQLi payloads.
Input Sanitization: Never trust user-supplied input in URL parameters.
Principle of Least Privilege: Ensure the web server's database user has no permissions to read system-level tables or files.
