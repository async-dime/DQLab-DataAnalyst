# Total Penjualan dan Revenue pada Quarter-1 (Jan, Feb, Mar) dan Quarter-2 (Apr,Mei,Jun)

  - Dari tabel orders_1 lakukan penjumlahan pada kolom quantity dengan fungsi aggregate sum() dan beri nama “total_penjualan”, 
  - Kalikan kolom quantity dengan kolom priceEach kemudian jumlahkan hasil perkalian kedua kolom tersebut dan beri nama “revenue”
  - Perusahaan hanya ingin menghitung penjualan dari produk yang terkirim saja, jadi kita perlu mem-filter kolom ‘status’ sehingga hanya menampilkan order dengan status “Shipped”.
  - Lakukan Langkah 1 & 2, untuk tabel orders_2.

### answer: 
```sh
SELECT SUM(quantity) as total_penjualan, SUM(quantity*priceEach) as revenue
FROM orders_1
WHERE status = 'Shipped';
SELECT SUM(quantity) as total_penjualan, SUM(quantity*priceEach) as revenue
FROM orders_2
WHERE status = 'Shipped';
```

### output:
```sh
+-----------------+-----------+
| total_penjualan | revenue   |
+-----------------+-----------+
|            8694 | 799579310 |
+-----------------+-----------+
+-----------------+-----------+
| total_penjualan | revenue   |
+-----------------+-----------+
|            6717 | 607548320 |
+-----------------+-----------+
```


---------------------------------------------------------------------------------------------------------


# Menghitung persentasi keseluruhan penjualan

Kedua tabel orders_1 dan orders_2 masih terpisah, untuk menghitung persentasi keseluruhan penjualan dari kedua tabel tersebut perlu digabungkan :
  - Pilihlah kolom “orderNumber”, “status”, “quantity”, “priceEach” pada tabel orders_1, dan tambahkan kolom baru dengan nama “quarter” dan isi dengan value “1”. 
    Lakukan yang sama dengan tabel orders_2, dan isi dengan value “2”, kemudian gabungkan kedua tabel tersebut.
  - Gunakan statement dari Langkah 1 sebagai subquery dan beri alias “tabel_a”.
  - Dari “tabel_a”, lakukan penjumlahan pada kolom “quantity” dengan fungsi aggregate sum() dan beri nama “total_penjualan”, dan kalikan kolom quantity dengan kolom priceEach kemudian jumlahkan hasil perkalian kedua kolom tersebut dan beri nama “revenue”
  - Filter kolom ‘status’ sehingga hanya menampilkan order dengan status “Shipped”.
  - Kelompokkan total_penjualan berdasarkan kolom “quarter”, dan jangan lupa menambahkan kolom ini pada bagian select.

### answer:
```sh
SELECT quarter, SUM(quantity) as total_penjualan, SUM(quantity*priceEach) as revenue
FROM (SELECT orderNumber, status, quantity, priceEach, '1' as quarter
FROM orders_1
UNION
SELECT orderNumber, status, quantity, priceEach, '2' as quarter
FROM orders_2) as tabel_a
WHERE status = 'Shipped'
GROUP BY quarter;
```

### output:
```sh
+---------+-----------------+-----------+
| quarter | total_penjualan | revenue   |
+---------+-----------------+-----------+
| 1       |            8694 | 799579310 |
| 2       |            6717 | 607548320 |
+---------+-----------------+-----------+
```