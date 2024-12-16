SELECT signup_date, COUNT(*) AS user_count
FROM users
GROUP BY signup_date
ORDER BY signup_date;


SELECT DISTINCT domain
FROM users;


SELECT *
FROM users
WHERE signup_date >= (CURRENT_DATE - INTERVAL '7 days');


SELECT domain, COUNT(*) AS domain_count
FROM users
GROUP BY domain
ORDER BY domain_count DESC
LIMIT 1;


DELETE FROM users
WHERE domain NOT IN ('gmail.com', 'yahoo.com', 'outlook.com');
