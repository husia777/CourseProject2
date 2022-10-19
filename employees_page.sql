SELECT last_name, first_name, region, home_phone
FROM employees
WHERE region IS NULL; --1запрос

SELECT customers.country
FROM customers
INTERSECT
SELECT suppliers.country
FROM suppliers
EXCEPT
SELECT employees.country
FROM employees; --2запрос