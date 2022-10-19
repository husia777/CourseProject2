SELECT *
FROM products
JOIN categories USING (category_id)
WHERE category_name IN ('Beverages', 'Seafood')
AND discontinued = 0 AND units_in_stock < 20 --запрос