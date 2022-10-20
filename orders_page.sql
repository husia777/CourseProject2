SELECT * FROM orders
ORDER BY required_date DESC, shipped_date --1команда

SELECT AVG(shipped_date - order_date) from orders
WHERE ship_country = 'USA' --2команда

SELECT product_name, SUM(unit_price * units_in_stock) as sum_product FROM products
where discontinued = 0 --3команда