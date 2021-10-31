# Promotion Effectiveness and Efficiency by Years

Pada bagian ini kita akan melakukan analisa terhadap efektifitas dan efisiensi dari promosi yang sudah dilakukan selama ini  

Efektifitas dan efisiensi dari promosi yang dilakukan akan dianalisa berdasarkan Burn Rate yaitu dengan membandigkan total value promosi yang dikeluarkan terhadap total sales yang diperoleh  

DQLab berharap bahwa burn rate tetap berada diangka maskimum 4.5%  

Formula untuk burn rate : `(total discount / total sales) * 100`

Buatkan Derived Tables untuk menghitung total sales (sales) dan total discount (promotion_value) berdasarkan tahun(years) dan formulasikan persentase burn rate nya (burn_rate_percentage).

### answer:
```sh
SELECT YEAR(order_date) as years, SUM(sales) as sales, SUM(discount_value) as promotion_value, ROUND((SUM(discount_value)/SUM(sales))*100,2) as burn_rate_percentage
FROM dqlab_sales_store
WHERE order_status = 'Order Finished'
GROUP BY YEAR(order_date)
```

### output:
```sh
+-------+------------+-----------------+----------------------+
| years | sales      | promotion_value | burn_rate_percentage |
+-------+------------+-----------------+----------------------+
|  2009 | 4613872681 |       214330327 |                 4.65 |
|  2010 | 4059100607 |       197506939 |                 4.87 |
|  2011 | 4112036186 |       214611556 |                 5.22 |
|  2012 | 4482983158 |       225867642 |                 5.04 |
+-------+------------+-----------------+----------------------+
```


---------------------------------------------------------------------------------------------------------


# Promotion Effectiveness and Efficiency by Product Sub Category

Pada bagian ini kita akan melakukan analisa terhadap efektifitas dan efisiensi dari promosi yang sudah dilakukan selama ini seperti pada bagian sebelumnya.  

Akan tetapi, ada kolom yang harus ditambahkan, yaitu : product_sub_category dan product_category  

Data yang ditampilkan hanya untuk tahun 2012

### answer:
```sh
SELECT 
  YEAR(order_date) as years, 
  product_sub_category, 
  product_category, 
  SUM(sales) as sales, 
  SUM(discount_value) as promotion_value, 
  ROUND((SUM(discount_value)/SUM(sales))*100,2) as burn_rate_percentage
FROM dqlab_sales_store
WHERE order_status = 'Order Finished' and YEAR(order_date) in ('2012')
GROUP BY YEAR(order_date), product_sub_category, product_category
ORDER BY YEAR(order_date),SUM(sales) DESC
```

### output:
```sh
+-------+--------------------------------+------------------+-----------+-----------------+----------------------+
| years | product_sub_category           | product_category | sales     | promotion_value | burn_rate_percentage |
+-------+--------------------------------+------------------+-----------+-----------------+----------------------+
|  2012 | Office Machines                | Technology       | 811427140 |        46616695 |                 5.75 |
|  2012 | Chairs & Chairmats             | Furniture        | 654168740 |        26623882 |                 4.07 |
|  2012 | Telephones and Communication   | Technology       | 422287514 |        18800188 |                 4.45 |
|  2012 | Tables                         | Furniture        | 388993784 |        16348689 |                 4.20 |
|  2012 | Binders and Binder Accessories | Office Supplies  | 363879200 |        22338980 |                 6.14 |
|  2012 | Storage & Organization         | Office Supplies  | 356714140 |        18802166 |                 5.27 |
|  2012 | Computer Peripherals           | Technology       | 308014340 |        15333293 |                 4.98 |
|  2012 | Copiers and Fax                | Technology       | 292489800 |        14530870 |                 4.97 |
|  2012 | Appliances                     | Office Supplies  | 266131100 |        14393300 |                 5.41 |
|  2012 | Office Furnishings             | Furniture        | 178927480 |         8233849 |                 4.60 |
|  2012 | Bookcases                      | Furniture        | 159984680 |        10024365 |                 6.27 |
|  2012 | Paper                          | Office Supplies  | 126896160 |         6224694 |                 4.91 |
|  2012 | Envelopes                      | Office Supplies  |  58629280 |         2334321 |                 3.98 |
|  2012 | Pens & Art Supplies            | Office Supplies  |  43818480 |         2343501 |                 5.35 |
|  2012 | Scissors, Rulers and Trimmers  | Office Supplies  |  36776400 |         2349280 |                 6.39 |
|  2012 | Labels                         | Office Supplies  |  10007040 |          452245 |                 4.52 |
|  2012 | Rubber Bands                   | Office Supplies  |   3837880 |          117324 |                 3.06 |
+-------+--------------------------------+------------------+-----------+-----------------+----------------------+
```