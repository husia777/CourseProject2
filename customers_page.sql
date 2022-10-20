SELECT COUNT(*) FROM  customers;  --1команда

SELECT  DISTINCT city ,  country FROM  customers    --2команда


SELECT customers.company_name, employees.first_name, employees.last_name
FROM employees
JOIN orders ON orders.employee_id = employees.employee_id
JOIN shippers ON shippers.shipper_id = orders.ship_via
JOIN customers ON customers.customer_id = orders.customer_id
WHERE customers.city = 'London' AND employees.city = 'London'
AND shippers.company_name = 'Speedy Express'; --3команда!



SELECT contact_name, order_id
FROM customers
LEFT JOIN orders USING (customer_id)
WHERE order_id IS NULL-- 4 ЗАПРОС

