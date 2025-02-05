CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    position VARCHAR(100),
    age INT
);

INSERT INTO employees (id, name, email, position, age) VALUES
(1, 'John Doe', 'john.doe@gmail.com', 'Software Engineer', 30),
(2, 'Jane Doe', 'jane.doe@gmail.com', 'Project Manager', 35),
(3, 'John Smith', 'john.smith@gmail.com', 'Software Engineer', 25);