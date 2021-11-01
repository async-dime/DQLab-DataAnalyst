# Apakah jumlah customers `xyz.com` semakin bertambah?
Penambahan jumlah customers dapat diukur dengan membandingkan total jumlah customers yang registrasi di periode saat ini dengan total jumlah customers yang registrasi diakhir periode sebelumnya.

  1. Dari tabel customer, pilihlah kolom customerID, createDate dan tambahkan kolom baru dengan menggunakan fungsi QUARTER(…) untuk mengekstrak nilai quarter dari CreateDate dan beri nama “quarter”
  2. Filter kolom “createDate” sehingga hanya menampilkan baris dengan createDate antara 1 Januari 2004 dan 30 Juni 2004
  3. Gunakan statement Langkah 1 & 2 sebagai subquery dengan alias tabel_b
  4. Hitunglah jumlah unik customers à tidak ada duplikasi customers dan beri nama “total_customers”
  5. Kelompokkan total_customer berdasarkan kolom “quarter”, dan jangan lupa menambahkan kolom ini pada bagian select.

### answer: 
```sh
SELECT quarter, COUNT(customerID) as total_customers 
FROM (
  SELECT customerID, createDate, '1' as quarter
  FROM customer WHERE createDate between '2004-01-01' and '2004-03-31'
  UNION
  SELECT customerID, createDate, '2' as quarter
  FROM customer WHERE createDate BETWEEN '2004-04-01' and '2004-06-31'
	) as tabel_b
GROUP BY quarter;
```

### output:
```sh
+---------+-----------------+
| quarter | total_customers |
+---------+-----------------+
| 1       |              43 |
| 2       |              35 |
+---------+-----------------+
```


---------------------------------------------------------------------------------------------------------


# Seberapa banyak customers tersebut yang sudah melakukan transaksi?
Problem ini merupakan kelanjutan dari problem sebelumnya yaitu dari sejumlah customer yang registrasi di periode quarter-1 dan quarter-2, berapa banyak yang sudah melakukan transaksi

  1. Dari tabel customer, pilihlah kolom customerID, createDate dan tambahkan kolom baru dengan menggunakan fungsi QUARTER(…) untuk mengekstrak nilai quarter dari CreateDate dan beri nama “quarter”
  2. Filter kolom “createDate” sehingga hanya menampilkan baris dengan createDate antara 1 Januari 2004 dan 30 Juni 2004
  3. Gunakan statement Langkah A&B sebagai subquery dengan alias tabel_b
  4. Dari tabel orders_1 dan orders_2, pilihlah kolom customerID, gunakan DISTINCT untuk menghilangkan duplikasi, kemudian gabungkan dengan kedua tabel tersebut dengan UNION.
  5. Filter tabel_b dengan operator IN() menggunakan 'Select statement langkah 4' , sehingga hanya customerID yang pernah bertransaksi (customerID tercatat di tabel orders) yang diperhitungkan.
  6. Hitunglah jumlah unik customers (tidak ada duplikasi customers) di statement SELECT dan beri nama “total_customers”
  7. Kelompokkan total_customer berdasarkan kolom “quarter”, dan jangan lupa menambahkan kolom ini pada bagian select.

### answer: 
```sh
SELECT quarter, COUNT(DISTINCT customerID) as total_customers 
FROM (
  SELECT customerID, createDate, QUARTER(createDate) as quarter
  FROM customer
  WHERE createDate BETWEEN '2004-01-01' AND '2004-06-30'
  ) as tabel_b
WHERE customerID IN (
  SELECT DISTINCT customerID FROM orders_1
  UNION
  SELECT DISTINCT customerID FROM orders_2
  )
GROUP BY quarter;
```

### output:
```sh
+---------+-----------------+
| quarter | total_customers |
+---------+-----------------+
|       1 |              25 |
|       2 |              19 |
+---------+-----------------+
```


---------------------------------------------------------------------------------------------------------


# Category produk apa saja yang paling banyak di-order oleh customers di Quarter-2?
Untuk mengetahui kategori produk yang paling banyak dibeli, maka dapat dilakukan dengan menghitung total order dan jumlah penjualan dari setiap kategori produk.

  1. Dari kolom orders_2, pilih productCode, orderNumber, quantity, status
  2. Tambahkan kolom baru dengan mengekstrak 3 karakter awal dari productCode yang merupakan ID untuk kategori produk; dan beri nama categoryID
  3. Filter kolom “status” sehingga hanya produk dengan status “Shipped” yang diperhitungkan
  4. Gunakan statement Langkah 1, 2, dan 3 sebagai subquery dengan alias tabel_c
  5. Hitunglah total order dari kolom “orderNumber” dan beri nama “total_order”, dan jumlah penjualan dari kolom “quantity” dan beri nama “total_penjualan”
  6. Kelompokkan berdasarkan categoryID, dan jangan lupa menambahkan kolom ini pada bagian select.
  7. Urutkan berdasarkan “total_order” dari terbesar ke terkecil

### answer:
```sh
SELECT * FROM (
  SELECT categoryID, COUNT(DISTINCT orderNumber) AS total_order, SUM(quantity) AS total_penjualan
  FROM (
	SELECT productCode, orderNumber, quantity, status, LEFT(productCode, 3) as categoryID
	FROM orders_2
	WHERE status = 'Shipped'
	) as tabel_c
  GROUP BY categoryID 
) a ORDER BY total_order DESC
```

### output:
```sh
+------------+-------------+-----------------+
| categoryID | total_order | total_penjualan |
+------------+-------------+-----------------+
| S18        |          25 |            2264 |
| S24        |          21 |            1826 |
| S32        |          11 |             616 |
| S12        |          10 |             491 |
| S50        |           8 |             292 |
| S10        |           8 |             492 |
| S70        |           7 |             675 |
| S72        |           2 |              61 |
+------------+-------------+-----------------+
```


---------------------------------------------------------------------------------------------------------


# Seberapa banyak customers yang tetap aktif bertransaksi setelah transaksi pertamanya?
Mengetahui seberapa banyak customers yang tetap aktif menunjukkan apakah `xyz.com` tetap digemari oleh customers untuk memesan kebutuhan bisnis mereka. Hal ini juga dapat menjadi dasar bagi tim product dan business untuk pengembangan product dan business kedepannya. Adapun metrik yang digunakan disebut retention cohort. Untuk project ini, kita akan menghitung retention dengan query SQL sederhana, sedangkan cara lain yaitu JOIN dan SELF JOIN akan dibahas dimateri selanjutnya :
 
Oleh karena baru terdapat 2 periode yang Quarter 1 dan Quarter 2, maka retention yang dapat dihitung adalah retention dari customers yang berbelanja di Quarter 1 dan kembali berbelanja di Quarter 2, sedangkan untuk customers yang berbelanja di Quarter 2 baru bisa dihitung retentionnya di Quarter 3.

  1. Dari tabel orders_1, tambahkan kolom baru dengan value “1” dan beri nama “quarter”
  2. Dari tabel orders_2, pilihlah kolom customerID, gunakan distinct untuk menghilangkan duplikasi
  3. Filter tabel orders_1 dengan operator IN() menggunakan 'Select statement langkah 2', sehingga hanya customerID yang pernah bertransaksi di quarter 2 (customerID tercatat di tabel orders_2) yang diperhitungkan.
  4. Hitunglah jumlah unik customers (tidak ada duplikasi customers) dibagi dengan total_ customers dalam percentage, pada Select statement dan beri nama “Q2”

### answer:
```sh
#Menghitung total unik customers yang transaksi di quarter_1
SELECT COUNT(DISTINCT customerID) as total_customers FROM orders_1;
#output = 25
SELECT 1 as quarter, (COUNT(DISTINCT customerID)*100)/25 as Q2 
FROM orders_1 
WHERE customerID IN (SELECT DISTINCT customerID FROM orders_2);
```

### output:
```sh
+-----------------+
| total_customers |
+-----------------+
|              25 |
+-----------------+
+---------+---------+
| quarter | Q2      |
+---------+---------+
|       1 | 24.0000 |
+---------+---------+
```


---------------------------------------------------------------------------------------------------------


# Kesimpulan
Berdasarkan data yang telah kita peroleh melalui query SQL, Kita dapat menarik kesimpulan bahwa :

  1. Performance `xyz.com` menurun signifikan di quarter ke-2, terlihat dari nilai penjualan dan revenue yang drop hingga 20% dan 24%,
  2. Perolehan customer baru juga tidak terlalu baik, dan sedikit menurun dibandingkan quarter sebelumnya.
  3. Ketertarikan customer baru untuk berbelanja di `xyz.com` masih kurang, hanya sekitar 56% saja yang sudah bertransaksi. Disarankan tim Produk untuk perlu mempelajari behaviour customer dan melakukan product improvement, sehingga conversion rate (register to transaction) dapat meningkat.
  4. Produk kategori S18 dan S24 berkontribusi sekitar 50% dari total order dan 60% dari total penjualan, sehingga ``xyz.com`` sebaiknya fokus untuk pengembangan category S18 dan S24.
  5. Retention rate customer `xyz.com` juga sangat rendah yaitu hanya 24%, artinya banyak customer yang sudah bertransaksi di quarter-1 tidak kembali melakukan order di quarter ke-2 (no repeat order).
  6.`xyz.com` mengalami pertumbuhan negatif di quarter ke-2 dan perlu melakukan banyak improvement baik itu di sisi produk dan bisnis marketing, jika ingin mencapai target dan positif growth di quarter ke-3. Rendahnya retention rate dan conversion rate bisa menjadi diagnosa awal bahwa customer tidak tertarik/kurang puas/kecewa berbelanja di `xyz.com`.