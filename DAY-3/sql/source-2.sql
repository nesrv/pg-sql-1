INSERT INTO Products(ProductName, Company, ProductCount, Price) 
VALUES 
    ('iPhone X', 'Apple', 2, 66000),
    ('iPhone 15', 'Apple', 2, 62000),
    ('iPhone 16 Pro', 'Apple', 5, 12000),
    ('Galaxy A35', 'Samsung', 2, 24000),
    ('Galaxy M15', 'Samsung', 1, 18000),
    ('Nokia G21', 'Nokia', 2, 26000),
    ('HTC U24', 'HTC', 6, 38000);
  
INSERT INTO Customers(FirstName) 
VALUES 
    ('Ольга'), 
    ('Дарья'),
    ('Мария'),
    ('Наталья'),
    ('Надежда'),
    ('Елена');
  
INSERT INTO Orders(ProductId, CustomerId, CreatedAt, ProductCount, Price) 
VALUES
( 
    (SELECT Id FROM Products WHERE ProductName='Galaxy A35'), 
    (SELECT Id FROM Customers WHERE FirstName='Ольга'),
    '2024-07-11',  
    2, 
    (SELECT Price FROM Products WHERE ProductName='Galaxy A35')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone 15'), 
    (SELECT Id FROM Customers WHERE FirstName='Ольга'),
    '2024-07-13',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone 15')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone 15'), 
    (SELECT Id FROM Customers WHERE FirstName='Дарья'),
    '2024-07-11',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone 15')
),
( 
    (SELECT Id FROM Products WHERE ProductName='Nokia G21'), 
    (SELECT Id FROM Customers WHERE FirstName='Мария'),
    '2024-07-11',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='Nokia G21')
);