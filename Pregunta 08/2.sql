SELECT moneda, precio * 10 AS precio_total
FROM bitcoin
WHERE fecha = '2024-04-08'
AND (moneda = 'PEN' OR moneda = 'EUR');
