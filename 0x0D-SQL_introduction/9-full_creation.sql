-- 9-full_creation.sql
-- a script that creates a table second_table in the database
-- hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(250), score INT);

INSERT INTO 
	second_table(id,name,score) 
	values
	(1, 'John', 10), 
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);
