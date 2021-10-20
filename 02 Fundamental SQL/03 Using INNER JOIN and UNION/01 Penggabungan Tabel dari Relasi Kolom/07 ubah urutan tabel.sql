/*
Mengganti query sebelumnya, dari:

SELECT * FROM ms_item_warna, ms_item_kategori
WHERE nama_barang = nama_item;
*/


-- menjadi:
SELECT * FROM ms_item_warna, ms_item_kategori
WHERE nama_barang = nama_item;


/*
output:

+-------------+--------------+-----------+----------+
| nama_barang | warna        | nama_item | kategori |
+-------------+--------------+-----------+----------+
| bayam       | hijau        | bayam     | sayuran  |
| duku        | kuning pekat | duku      | buah     |
| durian      | kuning       | durian    | buah     |
| gandum      | coklat       | gandum    | buah     |
| jambu air   | merah        | jambu air | buah     |
| jeruk       | oranye       | jeruk     | buah     |
+-------------+--------------+-----------+----------+


Terlihat jumlah data yang dihasilkan tetap 6 baris data, namun dengan urutan kolom yang berbeda.
Dimana dua kolom pertama adalah dari tabel ms_item_warna, dan dua kolom berikutnya dari tabel ms_item_barang. 
Hal ini sesuai dengan urutan nama tabel yang diketikkan setelah FROM.
*/