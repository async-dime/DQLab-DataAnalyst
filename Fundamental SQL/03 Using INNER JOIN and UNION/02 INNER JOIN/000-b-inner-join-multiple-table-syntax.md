### Syntax INNER JOIN – Memilih Beberapa Kolom Untuk Ditampilkan


Bagian query
```sh
SELECT tabel1.nama_kolom1, tabel1.nama_kolom2, ..., tabel2.nama_kolom2, .... 
FROM tabel1
```
menghendaki pemilihan kolom mana saja dari kedua tabel yang akan digabungkan. Disini diperlukan penggunaan prefix nama tabelnya.


Selanjutnya, bagian query
```sh
INNER JOIN tabel2
```
digunakan untuk menggabungkan tabel1 dengan tabel2.


Akhirnya, bagian query
```sh
ON tabel_1.nama_kolom1 = tabel2.nama_kolom1;
```
adalah acuan penggabungan tabel1 dan tabel2 berdasarkan kolom yang memiliki tingkat kecocokan yang tinggi. Kedua kolom dengan tingkat kecocokan yang tinggi pada masing-masing tabel disebut juga dengan key column.



> Catatan:
> Perlu diperhatikan jika menampilkan kolom dengan nama yang sama di kedua tabel, maka pada bagian Select, tidak bisa hanya mengetikkan nama kolom saja, tetapi juga harus didahului oleh prefix nama tabel dimana kolom itu berasal untuk menghindari error karena ambiguitas," Senja mengingatkanku sekali lagi.