## 🎯 Tasks
## Level 1: Data isolation
Task: Extract only the IP addresses of all visitors

## Level 2: Event correlation
Task: Display the IP address and corresponding server response status code

## Level 3: Attack vector filtering
Task: Find all suspicious POST requests and display the IP addresses of the senders.

## Level 4: Custom notifications (Reporting)
Task: Find requests with code 403 (Forbidden) and generate a readable incident report.

## Level 5: Deep Time Analysis (Advanced)
Task: Extract the exact time of each request using double processing (double separator).

## 📂 A typical web server log format was used for analysis.
## Logs used for work and analysis (example):

192.168.1.10 - - [03/Mar/2026:12:00:01] "GET /index.html" 200 1234
192.168.1.10 - - [03/Mar/2026:12:05:30] "POST /login" 401 532
192.168.1.20 - - [03/Mar/2026:12:10:15] "GET /admin" 403 231
192.168.1.10 - - [03/Mar/2026:12:15:00] "GET /favicon.ico" 200 450
192.168.1.10 - - [03/Mar/2026:12:20:45] "GET /style.css" 200 3200
192.168.1.10 - - [03/Mar/2026:12:25:12] "POST /login" 200 120
192.168.1.50 - - [03/Mar/2026:12:30:05] "GET /api/data" 500 999
192.168.1.10 - - [03/Mar/2026:12:35:00] "POST /upload" 403 0

## 🛠 Answers to the exercises
## Level 1: Data isolation:
cat logs.txt | awk '{print $1}'

## Level 2: Event correlation:
cat logs.txt | awk '{print $1, $9}'

## Level 3: Attack vector filtering:
cat logs.txt | grep -i "post" | awk '{print $1}'

## Level 4: Custom notifications (Reporting):
cat logs.txt | grep "403" | awk '{print "WARNING: IP " $1 " tried to access " $7 " - Access Denied"}'

## Level 5: Deep Time Analysis (Advanced):
cat logs.txt | awk '{print $4}' | awk -F ":" '{print $2":"$3":"$4}'


