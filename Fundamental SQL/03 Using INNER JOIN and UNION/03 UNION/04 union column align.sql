SELECT CustomerName, ContactName, City, PostalCode
FROM Customers
UNION
SELECT SupplierName, ContactName, City, PostalCode
FROM Suppliers;


/*
output:

+-----------------+-------------+----------+------------+
| CustomerName    | ContactName | City     | PostalCode |
+-----------------+-------------+----------+------------+
| Fransiska Maria | Maria       | Jakarta  |      14450 |
| Ana Helena      | Ana Helena  | Surabaya |       5021 |
| Lily Subari     | Lili        | Makassar |       5023 |
| Yulius Syrup    | Yulius      | Jakarta  |      14450 |
| Bandung Bakery  | Sherly Ani  | Bandung  |      70117 |
| Tara Pastry     | Regina Tara | Semarang |      48104 |
+-----------------+-------------+----------+------------+
*/