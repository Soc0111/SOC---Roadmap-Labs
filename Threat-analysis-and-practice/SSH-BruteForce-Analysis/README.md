# 🛡️ Incident Report: SSH Brute-Force & System Compromise

## 📝 Scenario Overview
During a routine log review of a Linux-based server, I identified a high-volume series of suspicious authentication attempts. This investigation details the transition from a distributed brute-force attack to a **successful unauthorized login**, followed by the implemented incident response plan.

---

## 🛠️ Investigation Details
| Component | Details |
| :--- | :--- |
| **Log Source** | 📄 `/var/log/auth.log` |
| **Attack Type** | 🔑 Brute-Force / Dictionary Attack |
| **Attacker IP** | 🕵️ `192.168.1.55` |
| **Target Account**| `kali` (Targeted after failed attempts on `admin`, `user`, `guest`) |
| **Outcome** | 🔴 **SUCCESSFUL COMPROMISE** (Root Access Gained) |

---

## 🔍 Evidence & Technical Analysis

### 1. Attack Pattern
The attacker used a dictionary attack, cycling through common usernames before identifying the valid user `kali`.
* **Timeline:** Feb 16, 10:45:10 – 10:45:18.
* **Volume:** Multiple failed attempts per second from the same source IP.

### 2. The Compromise
At **10:45:19**, the attacker successfully guessed the password for user `kali`.
* **Impact:** The attacker gained an interactive shell and immediately escalated privileges to **root (uid=0)**.

> [!CAUTION]
> **Critical Finding:** A successful login following hundreds of failed attempts is a high-fidelity indicator of a password compromise. Immediate containment was required.

---

## 🚀 Incident Response Plan (IRP)

### Phase 1: Containment 🚧
* **Network Block:** Immediately blocked IP `192.168.1.55` using `iptables` and `ufw deny`.
* **Session Termination:** Identified and killed all active sessions for user `kali` (`sudo pkill -u kali -9`).

### Phase 2: Eradication 🧹
* **Credential Rotation:** Forced an immediate password change for all administrative accounts.
* **Backdoor Search:** * Scanned for unauthorized persistence (Checking `crontab`, `~/.ssh/authorized_keys`).
    * Inspected `/etc/sudoers` for unauthorized modifications.

### Phase 3: Recovery 🔄
* **Integrity Check:** Used tools like `rkhunter` and `chkrootkit` to ensure no rootkits were installed.
* **Continuous Monitoring:** Configured SIEM alerts for any further attempts from the `192.168.x.x` subnet.

---

## 🛡️ Strategic Recommendations

To prevent future compromises, the following hardening measures are recommended:

1.  **MFA/SSH Keys:** Disable password-based authentication entirely and switch to SSH Key pairs.
2.  **Fail2Ban:** Implement `Fail2Ban` to automatically block IPs after 3-5 failed login attempts.
3.  **Port Obfuscation:** Move SSH from the default port (22) to a non-standard port to reduce automated "noise" attacks.
4.  **Least Privilege:** Ensure that users do not have global `sudo` permissions without explicit necessity.

---
**Status:** 🔴 Resolved | **Severity:** High | **Focus:** Incident Response & Hardening
