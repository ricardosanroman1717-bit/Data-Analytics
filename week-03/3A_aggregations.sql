
USE northwind;

-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to find the name of the product that has that price.

SELECT MIN(UnitPrice) AS CheapestPrice
FROM Products;

SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice = 2.50;
-- 2. Write a query to find the average price of all items that Northwind sells.

SELECT AVG(UnitPrice) AS AveragePrice
FROM Products;
-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then write a second query to find the name of the product with that price, plus the name of the supplier for that product.

SELECT MAX(UnitPrice) AS HighestPrice
FROM Products;

SELECT Products.ProductName, Products.UnitPrice,
       Suppliers.CompanyName AS SupplierName
FROM Products
INNER JOIN Suppliers
ON Products.SupplierID = Suppliers.SupplierID
WHERE Products.UnitPrice = 263.50;

-- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).

SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM Employees;

-- 5. Write a query to identify the highest salary and the lowest salary amounts which any employee makes. (Just the amounts, not the specific employees!)

SELECT MAX(Salary) AS HighestSalary,
       MIN(Salary) AS LowestSalary
FROM Employees;

-- 6. Write a query to find the name and supplier ID of each supplier and the number of items they supply. Hint: Join is your friend here.

SELECT Suppliers.CompanyName, Suppliers.SupplierID,
       COUNT(Products.ProductID) AS ProductCount
FROM Suppliers
LEFT JOIN Products
ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.SupplierID, Suppliers.CompanyName;


-- 7. Write a query to find the list of all category names and the average price for items in each category.

SELECT Categories.CategoryName,
       AVG(Products.UnitPrice) AS AveragePrice
FROM Categories
INNER JOIN Products
ON Categories.CategoryID = Products.CategoryID
GROUP BY Categories.CategoryName;

-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what is the name of each supplier and the number of items they supply.

SELECT Suppliers.CompanyName,
       COUNT(Products.ProductID) AS ProductCount
FROM Suppliers
INNER JOIN Products
ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.SupplierID, Suppliers.CompanyName
HAVING COUNT(Products.ProductID) >= 5;

-- 9. Write a query to list products currently in inventory by the product id, product name, and inventory value (calculated by multiplying unit price by the number of units on hand). Sort the results in descending order by value. If two or more have the same value, order by product name. If a product is not in stock, leave it off the list.

SELECT ProductID, ProductName,
       UnitPrice * UnitsInStock AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;
