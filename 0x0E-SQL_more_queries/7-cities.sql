-- 7-cities.sql
-- a script that creates the database hbtn_0d_usa and
-- the table cities (in the database hbtn_0d_usa) on your MySQL server.

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select database
USE hbtn_0d_usa;

-- Create table
CREATE TABLE
	IF NOT EXISTS 
		cities
		(
			id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
			state_id INT NOT NULL, FOREIGN KEY(id) REFERENCES states(id),
			name VARCHAR(256) NOT NULL
		);
