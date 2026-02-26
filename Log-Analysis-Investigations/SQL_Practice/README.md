Scenario 1: Logistics data analysis (Basic filters)
Task: Search for heavy parcels in specific regions to identify logistics anomalies.

Table: Packages (id, sender_name, receiver_name, weight, city, status)
Query: Search for packages weighing more than 100 kg sent to Kiev.

SELECT * FROM Packages 
WHERE city = 'Kyiv' AND weight > 100;

Scenario 2: Searching for attack patterns (LIKE & Templates)
Task: Identify suspicious users and anonymous senders.

Query: Search for all records where the sender's name begins with “An” (e.g., Anonymous) or the city contains “yo” (e.g., Tokyo, New York).

SELECT * FROM Packages 
WHERE sender_name LIKE 'An%' OR city LIKE '%yo%';

Scenario 3: Incident Investigation (JOIN / Table Merge)
Task: Match the type of attack with a specific user and their department to identify insider threats.

Tables: 1. Incidents (incident logs)
2. Users (employee data)
3. Departments (company structure)

Query: Display the incident type, user name, and department name.

SELECT Incidents.type, Users.username, Departments.dep_name 
FROM Incidents 
JOIN Users ON Incidents.user_id = Users.user_id
JOIN Departments ON Incidents.user_id = Departments.user_id;
