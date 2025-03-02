CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

INSERT INTO departments (name) VALUES ('IT');
INSERT INTO departments (name) VALUES ('HR');
INSERT INTO departments (name) VALUES ('Marketing');

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    position VARCHAR(255),
    department_id INTEGER REFERENCES departments(id) ON DELETE SET NULL,
    manager_id INTEGER REFERENCES employees(id) ON DELETE SET NULL,
    birthday DATE,
    join_date DATE,
    is_manager BOOLEAN DEFAULT FALSE
);

-- Insert Employees (Managers)
INSERT INTO employees (name, email, position, department_id, birthday, join_date, is_manager)
VALUES ('John Doe', 'john.doe@example.com', 'CTO', 1, '1980-05-15', '2010-06-01', TRUE);

INSERT INTO employees (name, email, position, department_id, birthday, join_date, is_manager)
VALUES ('Alice Smith', 'alice.smith@example.com', 'HR Director', 2, '1985-09-22', '2012-08-15', TRUE);

INSERT INTO employees (name, email, position, department_id, birthday, join_date, is_manager)
VALUES ('Bob Johnson', 'bob.johnson@example.com', 'Marketing Director', 3, '1978-11-30', '2008-03-20', TRUE);

-- Insert Employees (Subordinates)
INSERT INTO employees (name, email, position, department_id, manager_id, birthday, join_date)
VALUES ('Jane Doe', 'jane.doe@example.com', 'Software Engineer', 1, 1, '1995-04-10', '2020-01-10');

INSERT INTO employees (name, email, position, department_id, manager_id, birthday, join_date)
VALUES ('Michael Brown', 'michael.brown@example.com', 'System Administrator', 1, 1, '1992-07-05', '2018-11-01');

INSERT INTO employees (name, email, position, department_id, manager_id, birthday, join_date)
VALUES ('Sara Wilson', 'sara.wilson@example.com', 'HR Specialist', 2, 2, '1990-12-15', '2015-09-30');

INSERT INTO employees (name, email, position, department_id, manager_id, birthday, join_date)
VALUES ('Tom Lee', 'tom.lee@example.com', 'Marketing Coordinator', 3, 3, '1993-06-25', '2019-05-20');

--CREATE TABLE IF NOT EXISTS employees (
--    id INT PRIMARY KEY,
--    name VARCHAR(100),
--    email VARCHAR(100),
--    position VARCHAR(100),
--    age INT
--);
--
--INSERT INTO employees (id, name, email, position, age) VALUES
--(1, 'John Doe', 'john.doe@gmail.com', 'Software Engineer', 30),
--(2, 'Jane Doe', 'jane.doe@gmail.com', 'Project Manager', 35),
--(3, 'John Smith', 'john.smith@gmail.com', 'Software Engineer', 25);