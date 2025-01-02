INSERT INTO Customers (CustomerID, Name, Age, Gender, Location)
VALUES 
(1, 'Alice', 30, 'Female', 'New York'),
(2, 'Bob', 25, 'Male', 'San Francisco'),
(3, 'Charlie', 35, 'Male', 'Chicago');

INSERT INTO Products (ProductID, Name, Category, Price)
VALUES 
(1, 'Laptop', 'Electronics', 800),
(2, 'Headphones', 'Electronics', 50),
(3, 'Book', 'Books', 20);


INSERT INTO Orders (OrderID, CustomerID, ProductID, OrderDate, Quantity, TotalPrice)
VALUES
(1, 1, 1, '2025-01-01', 1, 800),
(2, 2, 2, '2025-01-02', 2, 100),
(3, 3, 3, '2025-01-03', 3, 60);

