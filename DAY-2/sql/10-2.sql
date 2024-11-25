INSERT INTO Products(ProductName, Company, ProductCount, Price) 
VALUES ('iPhone X', 'Apple', 2, 66000),
('iPhone 8', 'Apple', 2, 51000),
('iPhone 7', 'Apple', 5, 42000),
('Galaxy S9', 'Samsung', 2, 56000),
('Galaxy S8 Plus', 'Samsung', 1, 46000),
('Nokia 9', 'HDM Global', 2, 26000),
('Desire 12', 'HTC', 6, 38000);
  
INSERT INTO Customers(FirstName) 
VALUES ('Tom'), ('Bob'),('Sam');
  
INSERT INTO Orders(ProductId, CustomerId, CreatedAt, ProductCount, Price) 
VALUES
( 
    (SELECT Id FROM Products WHERE ProductName='Galaxy S9'), 
    (SELECT Id FROM Customers WHERE FirstName='Tom'),
    '2017-07-11',  
    2, 
    (SELECT Price FROM Products WHERE ProductName='Galaxy S9')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone 8'), 
    (SELECT Id FROM Customers WHERE FirstName='Tom'),
    '2017-07-13',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone 8')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone 8'), 
    (SELECT Id FROM Customers WHERE FirstName='Bob'),
    '2017-07-11',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone 8')
);