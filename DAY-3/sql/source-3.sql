CREATE TABLE Customers
(
    Id SERIAL PRIMARY KEY,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    AccountSum NUMERIC DEFAULT 0
);
CREATE TABLE Employees
(
    Id SERIAL PRIMARY KEY,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL
);
  
INSERT INTO Customers(FirstName, LastName, AccountSum) VALUES
('Ольга', 'Александровна', 2000),
('Дарья', 'Павловна', 3000),
('Мария', 'Александровна', 4200),
('Наталья', 'Михайловна', 2800),
('Николай', 'Евгеньевич', 2500),
('Игорь', 'Михайлович', 2800);
  
INSERT INTO Employees(FirstName, LastName) VALUES
('Ольга', 'Александровна'),
('Дарья', 'Павловна'),
('Надежда', 'Юрьевна'),
('Николай', 'Евгеньевич'),
('Елена', 'Вячеславовна');