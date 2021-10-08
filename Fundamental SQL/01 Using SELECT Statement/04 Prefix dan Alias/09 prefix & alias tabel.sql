/*
Contoh kode alias pada kolom dan tabel:

SELECT t1.kode_produk AS product_kode, t1.nama_produk as product_name FROM ms_produk as t1;
*/

/*
Gantilah perintah pada code editor dengan nama alias t2 
- tanpa menggunakan keyword AS - 
untuk tabel ms_produk dan menampilkan kolom nama_produk dan harga, lengkap dengan prefix alias.
*/

SELECT t2.nama_produk, t2.harga FROM ms_produk t2;