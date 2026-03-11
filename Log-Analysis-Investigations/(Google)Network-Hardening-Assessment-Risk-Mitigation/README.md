# 🛡️ Case 13: Network Hardening Assessment & Risk Mitigation

## 🔍 1) Project Overview
In this lab, I acted as a Security Analyst for a social media organization that recently experienced a major data breach. 
The incident exposed sensitive customer information, including names and addresses. 
My objective was to analyze the current network infrastructure, identify critical vulnerabilities, and recommend hardening strategies to prevent future compromises.

## 🧐 2) Identified Vulnerabilities
The post-incident audit revealed four primary security gaps:
1. **Broken Authentication:** Employees were frequently sharing passwords.
2. **Weak Defaults:** The database administrator password was set to a factory default.
3. **Insecure Network Perimeter:** Firewalls lacked basic traffic filtration rules.
4. **Lack of MFA:** Multi-factor authentication was not implemented across the organization.

---

## 🧱 3) Tech Stack & Hardening Tools
To address these risks, I selected the following methods from the hardening framework:

* **Multi-factor Authentication (MFA):** Requires users to verify identity through two or more methods (e.g., OTP, biometrics) to thwart brute force and credential sharing.
* **Network Access Privileges & Baseline Configurations:** Implementing "least privilege" and documented system specifications to ensure default passwords (like the DB admin) are changed immediately upon deployment.
* **Penetration Testing (Pen-Test):** Conducting simulated attacks to proactively identify hidden vulnerabilities and validate the effectiveness of new security controls.

---

## 📝 4) Security Recommendations

### 1. Firewall Maintenance & Port Filtering
* **Effectiveness:** Implementing strict firewall rules and filtering specific port numbers limits unauthorized communication and prevents attackers from entering the private network. 
This directly mitigates the risk of external actors scanning for open database ports.
* **Implementation Frequency:** Initial configuration is required immediately, with regular audits performed quarterly or after any major network change.

### 2. Password Policies & MFA Enforcement
* **Effectiveness:** Adopting NIST-standard password policies (salting and hashing) combined with mandatory MFA neutralizes the impact of password sharing. 
Even if a password is leaked, the attacker cannot gain access without the second authentication factor.
* **Implementation Frequency:** MFA is a one-time setup with continuous maintenance; password policies should be enforced globally and reviewed during regular security audits.

---

## ✅ 5) Conclusion
By transitioning from default configurations to a hardened security posture, the organization significantly reduces its attack surface. The combination of technical barriers (Firewalls, MFA) and administrative controls (Password Policies) ensures robust protection for user data in the future.
