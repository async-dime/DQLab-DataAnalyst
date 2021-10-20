SELECT * FROM ms_item_warna
INNER JOIN ms_item_kategori
ON ms_item_warna.nama_barang = ms_item_kategori.nama_item;


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

Hasil yang diperoleh dengan penggunaan SELECT … FROM … INNER JOIN … ON …; adalah sama dengan penerapan SELECT … FROM … WHERE …;.
*/