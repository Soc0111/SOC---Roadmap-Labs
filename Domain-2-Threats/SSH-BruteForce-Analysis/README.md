# Incident Report: SSH Brute-Force & Compromise

## 1. Scenario Overview
During a routine log review of a Linux-based server, I identified a series of suspicious authentication attempts followed by a successful unauthorized login. This report details the detection, analysis, and proposed response plan.

## 2. Evidence (Raw Logs)
The following logs were extracted from `/var/log/auth.log`:

Feb 16 10:45:10 server sshd[1234]: Invalid user admin from 192.168.1.55 port 56788
Feb 16 10:45:12 server sshd[1235]: Invalid user admin from 192.168.1.55 port 56790
Feb 16 10:45:14 server sshd[1236]: Invalid user user from 192.168.1.55 port 56792
Feb 16 10:45:16 server sshd[1237]: Invalid user guest from 192.168.1.55 port 56794
Feb 16 10:45:18 server sshd[1238]: Accepted password for kali from 192.168.1.55 port 56796 ssh2
Feb 16 10:45:19 server sshd[1238]: pam_unix(sshd:session): session opened for user kali by (uid=0)

3. Technical Analysis
Attack Type: Brute-force / Dictionary Attack.
Source IP: 192.168.1.55.
Target Account: Started with generic accounts (admin, user, guest) before targeting the real user kali.
Outcome: SUCCESSFUL COMPROMISE. The attacker successfully guessed the password for user kali at 10:45:18.
Impact: The attacker gained interactive shell access and successfully opened a session with root privileges (uid=0).

4. Incident Response Plan 
Phase 1: Containment 
Network Block: Immediately block IP 192.168.1.55 using a firewall.
sudo ufw deny from 192.168.1.55
Session Termination: Kill all active sessions for user kali.
sudo pkill -u kali -9
Phase 2: Eradication 
Credential Rotation: Force an immediate password change for the kali account.
Backdoor Search: Scan for persistence (crontab entries, unauthorized SSH keys in ~/.ssh/authorized_keys, or new sudoers).
Phase 3: Recovery 
Monitor logs for any further attempts from the same subnet.
Verify system integrity using tools like rkhunter or chkrootkit.

5. Security Recommendations
Disable password-based authentication and switch to SSH Keys.
Implement Fail2Ban to automatically block IPs after 3-5 failed attempts.
Change the default SSH port (22) to a non-standard port.
