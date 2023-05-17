-- 2-create_read_user.sql
-- a script that creates the database hbtn_0d_2 and the user user_0d_2.
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If the database hbtn_0d_2 already exists, the script should not fail
-- If the user user_0d_2 already exists, the script should not fail

--Create databse if mot exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if not exists
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';

-- Grant Privileges to User
GRANT SELECT ON 'hbtn_0d_2'.* TO user_0d_2@localhost;

-- Clear cache
FLUSH PRIVILEGES;
