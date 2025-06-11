CREATE DATABASE my_database;                   -- Create a new database
USE my_database;                               -- Switch to a database
DROP DATABASE my_database;                     -- Delete a database
SHOW DATABASES;                                -- List all databases



CREATE TABLE employees (                       -- Create a table
  id INT PRIMARY KEY,
  name VARCHAR(100),
  age INT,
  salary DECIMAL(10, 2)
);

DROP TABLE employees;                          -- Delete table
ALTER TABLE employees ADD dept VARCHAR(50);    -- Add a column
ALTER TABLE employees DROP COLUMN dept;        -- Drop a column
ALTER TABLE employees RENAME TO staff;         -- Rename table


INSERT INTO employees (id, name, age, salary)
VALUES (1, 'Alice', 30, 50000.00);
INSERT INTO employees VALUES (2, 'Bob', 25, 45000.00); -- All columns


UPDATE employees SET salary = 55000 WHERE id = 1;     -- Update value
DELETE FROM employees WHERE age < 25;                 -- Delete rows
TRUNCATE TABLE employees;                             -- Delete all rows (fast)


SELECT * FROM employees;                              -- All columns
SELECT name, age FROM employees;                      -- Specific columns
SELECT DISTINCT age FROM employees;                   -- Unique values
SELECT * FROM employees WHERE age > 30;               -- Filter
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 60000;
SELECT * FROM employees WHERE name LIKE 'A%';         -- Pattern matching
SELECT * FROM employees WHERE dept IS NULL;           -- NULL check


SELECT COUNT(*) FROM employees;                       -- Count rows
SELECT MAX(salary), MIN(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT SUM(salary) FROM employees;


SELECT dept, AVG(salary) FROM employees
GROUP BY dept;
SELECT dept, COUNT(*) FROM employees
GROUP BY dept
HAVING COUNT(*) > 5;                                   -- Filter groups



SELECT * FROM employees ORDER BY salary ASC;
SELECT * FROM employees ORDER BY age DESC, salary ASC;



-- INNER JOIN (common in both)
SELECT e.name, d.name
FROM employees e
JOIN departments d ON e.dept_id = d.id;

-- LEFT JOIN
SELECT e.name, d.name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;

-- RIGHT JOIN
SELECT e.name, d.name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.id;

-- FULL OUTER JOIN (some DBs)
SELECT e.name, d.name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.id;



SELECT name FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- In WHERE
SELECT name FROM employees
WHERE dept_id IN (SELECT id FROM departments WHERE location = 'NY');



SELECT name FROM table1
UNION
SELECT name FROM table2;

SELECT name FROM table1
INTERSECT
SELECT name FROM table2;

SELECT name FROM table1
EXCEPT
SELECT name FROM table2;



CREATE TABLE users (
  id INT PRIMARY KEY,
  email VARCHAR(100) UNIQUE,
  age INT CHECK (age >= 18),
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES departments(id)
);



CREATE INDEX idx_name ON employees(name);      -- Create index
DROP INDEX idx_name;                           -- Drop index
EXPLAIN SELECT * FROM employees;               -- Execution plan



CREATE VIEW senior_employees AS
SELECT * FROM employees WHERE age > 40;

-- Stored Procedure (MySQL-style)
DELIMITER //
CREATE PROCEDURE GetAll()
BEGIN
  SELECT * FROM employees;
END;
//
DELIMITER ;


SHOW TABLES;                                    -- List tables
DESCRIBE employees;                             -- Describe table structure
SELECT NOW();                                   -- Current date/time
