
USE northwind;

-- 1. Create a single query to list the product id, product name, unit price and category name of all products. Order by category name and within that, by product name.

SELECT Products.ProductID, Products.ProductName,
       Products.UnitPrice, Categories.CategoryName
FROM Products
INNER JOIN Categories
ON Products.CategoryID = Categories.CategoryID
ORDER BY Categories.CategoryName ASC, Products.ProductName ASC;
-- 2. Create a single query to list the product id, product name, unit price and supplier name of all products that cost more than $75. Order by product name.

SELECT Products.ProductID, Products.ProductName,
       Products.UnitPrice, Suppliers.CompanyName AS SupplierName
FROM Products
INNER JOIN Suppliers
ON Products.SupplierID = Suppliers.SupplierID
WHERE Products.UnitPrice > 75
ORDER BY Products.ProductName ASC;
-- 3. Create a single query to list the product id, product name, unit price, category name, and supplier name of every product. Order by product name.

SELECT Products.ProductID, Products.ProductName,
       Products.UnitPrice, Categories.CategoryName,
       Suppliers.CompanyName AS SupplierName
FROM Products
INNER JOIN Categories
ON Products.CategoryID = Categories.CategoryID
INNER JOIN Suppliers
ON Products.SupplierID = Suppliers.SupplierID
ORDER BY Products.ProductName ASC;
-- 4. Create a single query to list the order id, ship name, ship address, and shipping company name of every order that shipped to Germany. Assign the shipping company name the alias 'Shipper.' Order by the name of the shipper, then the name of who it shipped to.

SELECT Orders.OrderID, Orders.ShipName,
       Orders.ShipAddress, Shippers.CompanyName AS Shipper
FROM Orders
INNER JOIN Shippers
ON Orders.ShipVia = Shippers.ShipperID
WHERE Orders.ShipCountry = 'Germany'
ORDER BY Shipper ASC, Orders.ShipName ASC;
-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, with a count of how many orders were shipped for that ship name.

SELECT Orders.ShipName, Orders.ShipAddress,
       Shippers.CompanyName AS Shipper,
       COUNT(Orders.OrderID) AS OrderCount
FROM Orders
INNER JOIN Shippers
ON Orders.ShipVia = Shippers.ShipperID
WHERE Orders.ShipCountry = 'Germany'
GROUP BY Orders.ShipName, Orders.ShipAddress, Shippers.CompanyName
ORDER BY Shipper ASC, Orders.ShipName ASC;
-- 6. Create a single query to list the order id, order date, ship name, ship address of all orders that included Sasquatch Ale.

SELECT Orders.OrderID, Orders.OrderDate,
       Orders.ShipName, Orders.ShipAddress
FROM Orders
INNER JOIN `Order Details`
ON Orders.OrderID = `Order Details`.OrderID
INNER JOIN Products
ON `Order Details`.ProductID = Products.ProductID
WHERE Products.ProductName = 'Sasquatch Ale';
