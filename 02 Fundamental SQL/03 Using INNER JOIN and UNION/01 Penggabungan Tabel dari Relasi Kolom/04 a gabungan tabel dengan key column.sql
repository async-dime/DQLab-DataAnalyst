/*
Menggabungkan Tabel dengan Key Columns
*/


SELECT * FROM ms_item_kategori, ms_item_warna
WHERE nama_barang = nama_item;


/*
output:

+-----------+----------+-------------+--------------+
| nama_item | kategori | nama_barang | warna        |
+-----------+----------+-------------+--------------+
| bayam     | sayuran  | bayam       | hijau        |
| duku      | buah     | duku        | kuning pekat |
| durian    | buah     | durian      | kuning       |
| gandum    | buah     | gandum      | coklat       |
| jambu air | buah     | jambu air   | merah        |
| jeruk     | buah     | jeruk       | oranye       |
+-----------+----------+-------------+--------------+ 


Dapat dilihat hasil dari penggabungan dua tabel tersebut yaitu berupa tabel baru dengan empat kolom dan enam baris data. 
Perlu diketahui bahwa penggabungan ini bersifat sementara artinya tabel asli di database tidak mengalami perubahan, 
dan tabel baru hasil penggabungan ini juga tidak serta merta tersimpan di database.  
*/

