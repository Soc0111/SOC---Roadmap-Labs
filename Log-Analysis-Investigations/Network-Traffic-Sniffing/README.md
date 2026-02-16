# Case Study 07: Credential Sniffing in Unencrypted Traffic (HTTP) 

## 1. Executive Summary
During a network traffic analysis exercise using Wireshark, I identified a critical security vulnerability: a user's login credentials (username and password) were transmitted over the network in cleartext via the unencrypted HTTP protocol. This exposure allows any attacker with network access to intercept and steal sensitive data.

## 2. Evidence (Packet Data Payload)
The following data was extracted from a TCP stream (Packet #46):


POST /login.php HTTP/1.1
Host: 192.168.1.5
Content-Type: application/x-www-form-urlencoded
user=admin&pass=12345678

## 3. Technical Analysis & Investigation
Phase 1: Identifying Unencrypted Protocols
Observation: The traffic is using Port 80 (HTTP) instead of Port 443 (HTTPS).
Conclusion: All data sent between the client and the server is visible to anyone performing a "Man-in-the-Middle" (MitM) attack.

Phase 2: Credential Exposure
Observation: The payload contains the raw string user=admin&pass=12345678.
Impact: The attacker does not need to crack the password; they simply read it. Even if the password were complex, it would still be fully exposed.

## 4. Security Recommendations
Decommission Legacy Protocols: Disable HTTP, FTP, and Telnet across the entire infrastructure. Replace them with HTTPS, SFTP, and SSH.
Encryption Everywhere: Ensure that all internal applications use TLS 1.2 or higher for data in transit.
MFA: Even if a password is stolen via sniffing, Multi-Factor Authentication would prevent the attacker from logging in.
