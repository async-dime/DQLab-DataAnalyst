/*
Overall Performance by Year

Buatlah Query dengan menggunakan SQL untuk mendapatkan total penjualan (sales) dan jumlah order (number_of_order) dari tahun 2009 sampai 2012 (years). 
*/

SELECT YEAR(order_date) as years, SUM(sales) as sales, COUNT(order_quantity) as number_of_order
FROM dqlab_sales_store
WHERE order_status = 'Order Finished'
GROUP BY YEAR(order_date)

/*
output:

+-------+------------+-----------------+
| years | sales      | number_of_order |
+-------+------------+-----------------+
|  2009 | 4613872681 |            1244 |
|  2010 | 4059100607 |            1248 |
|  2011 | 4112036186 |            1178 |
|  2012 | 4482983158 |            1254 |
+-------+------------+-----------------+
*/


---------------------------------------------------------------------------------------------------------


/*
Overall Performance by Product Sub Category

Buatlah Query dengan menggunakan SQL untuk mendapatkan total penjualan (sales) berdasarkan sub category dari produk (product_sub_category) pada tahun 2011 dan 2012 saja (years) 
*/

SELECT YEAR(order_date) as years, product_sub_category, SUM(sales) as sales
FROM dqlab_sales_store
WHERE order_status = 'Order Finished' and YEAR(order_date) in (2011, 2012)
GROUP BY YEAR(order_date), product_sub_category
ORDER BY YEAR(order_date),SUM(sales) DESC

/*
output:

+-------+--------------------------------+------------+
| years | product_sub_category           | SUM(sales) |
+-------+--------------------------------+------------+
|  2011 | Chairs & Chairmats             |  622962720 |
|  2011 | Office Machines                |  545856280 |
|  2011 | Tables                         |  505875008 |
|  2011 | Copiers and Fax                |  404074080 |
|  2011 | Telephones and Communication   |  392194658 |
|  2011 | Binders and Binder Accessories |  298023200 |
|  2011 | Storage & Organization         |  285991820 |
|  2011 | Appliances                     |  272630020 |
|  2011 | Computer Peripherals           |  232677960 |
|  2011 | Bookcases                      |  169304620 |
|  2011 | Office Furnishings             |  160471500 |
|  2011 | Paper                          |  111080380 |
|  2011 | Pens & Art Supplies            |   43093800 |
|  2011 | Envelopes                      |   36463900 |
|  2011 | Labels                         |   15607780 |
|  2011 | Scissors, Rulers and Trimmers  |   12638340 |
|  2011 | Rubber Bands                   |    3090120 |
|  2012 | Office Machines                |  811427140 |
|  2012 | Chairs & Chairmats             |  654168740 |
|  2012 | Telephones and Communication   |  422287514 |
|  2012 | Tables                         |  388993784 |
|  2012 | Binders and Binder Accessories |  363879200 |
|  2012 | Storage & Organization         |  356714140 |
|  2012 | Computer Peripherals           |  308014340 |
|  2012 | Copiers and Fax                |  292489800 |
|  2012 | Appliances                     |  266131100 |
|  2012 | Office Furnishings             |  178927480 |
|  2012 | Bookcases                      |  159984680 |
|  2012 | Paper                          |  126896160 |
|  2012 | Envelopes                      |   58629280 |
|  2012 | Pens & Art Supplies            |   43818480 |
|  2012 | Scissors, Rulers and Trimmers  |   36776400 |
|  2012 | Labels                         |   10007040 |
|  2012 | Rubber Bands                   |    3837880 |
+-------+--------------------------------+------------+
*/