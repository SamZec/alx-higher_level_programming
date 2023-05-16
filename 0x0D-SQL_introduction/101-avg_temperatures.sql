-- 101-avg_temperatures.sql
-- a script that displays the average temperature (Fahrenheit) by city
-- ordered by temperature (descending).
-- displays the top 3 of cities temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC;
