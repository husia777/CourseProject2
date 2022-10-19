SELECT COUNT(*) FROM  customers;  --1команда

SELECT  DISTINCT city ,  country FROM  customers    --2команда
SELECT  orders.ship_name, employees.last_name, employees.first_name
FROM  employees;

JOIN orders ON orders.employee_id = employees.employee_id
JOIN shippers ON shippers.shipper_id = orders.ship_via
WHERE orders.ship_city = 'London' AND employees.city = 'London' AND shippers.company_name = 'Speedy Express'; --2команда!

 -- 4 ЗАПРОС ПРОПУЩЕН

--страны из кастомера пересечение с саплаер потом экзепт стран в эмплоерс