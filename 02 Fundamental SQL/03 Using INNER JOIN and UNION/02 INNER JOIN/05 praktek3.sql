/*
Gabungkan tabel tr_penjualan dan ms_produk

Kolom yang ditampilkan dari tabel tr_penjualan adalah kode_transaksi, kode_pelanggan, kode_produk, qty. 
Kolom yang ditampilkan dari tabel ms_produk adalah nama_produk dan harga." 

Kemudian bentuk kolom total yang merupakan hasil perkalian setiap baris pada kolom harga di tabel ms_produk dengan kolom qty di tabel tr_penjualan.

 Tabel hasil penggabungan haruslah membentuk kolom-kolom dengan urutannya adalah kode_transaksi, kode_pelanggan, kode_produk, nama_produk, harga, qty, dan total.
*/


SELECT tr_penjualan.kode_transaksi, tr_penjualan.kode_pelanggan, tr_penjualan.kode_produk, ms_produk.nama_produk, ms_produk.harga, tr_penjualan.qty, ms_produk.harga * tr_penjualan.qty AS total
FROM tr_penjualan
INNER JOIN ms_produk
ON tr_penjualan.kode_produk = ms_produk.kode_produk;


/*
output:

+----------------+----------------+-------------+-------------------------------+--------+------+---------+
| kode_transaksi | kode_pelanggan | kode_produk | nama_produk                   | harga  | qty  | total   |
+----------------+----------------+-------------+-------------------------------+--------+------+---------+
| tr-001         | dqlabcust07    | prod-01     | Kotak Pensil DQLab            |  62500 |    5 |  312500 |
| tr-001         | dqlabcust07    | prod-03     | Gift Voucher DQLab 100rb      | 100000 |    1 |  100000 |
| tr-001         | dqlabcust07    | prod-09     | Buku Planner Agenda DQLab     |  92000 |    3 |  276000 |
| tr-001         | dqlabcust07    | prod-04     | Flashdisk DQLab 32 GB         |  40000 |    3 |  120000 |
| tr-002         | dqlabcust01    | prod-03     | Gift Voucher DQLab 100rb      | 100000 |    2 |  200000 |
| tr-002         | dqlabcust01    | prod-10     | Sticky Notes DQLab 500 sheets |  55000 |    4 |  220000 |
| tr-002         | dqlabcust01    | prod-07     | Tas Travel Organizer DQLab    |  48000 |    1 |   48000 |
| tr-003         | dqlabcust03    | prod-02     | Flashdisk DQLab 64 GB         |  55000 |    2 |  110000 |
| tr-004         | dqlabcust03    | prod-10     | Sticky Notes DQLab 500 sheets |  55000 |    5 |  275000 |
| tr-004         | dqlabcust03    | prod-04     | Flashdisk DQLab 32 GB         |  40000 |    4 |  160000 |
| tr-005         | dqlabcust05    | prod-09     | Buku Planner Agenda DQLab     |  92000 |    3 |  276000 |
| tr-005         | dqlabcust05    | prod-01     | Kotak Pensil DQLab            |  62500 |    1 |   62500 |
| tr-005         | dqlabcust05    | prod-04     | Flashdisk DQLab 32 GB         |  40000 |    2 |   80000 |
| tr-006         | dqlabcust02    | prod-05     | Gift Voucher DQLab 250rb      | 250000 |    4 | 1000000 |
| tr-006         | dqlabcust02    | prod-08     | Gantungan Kunci DQLab         |  15800 |    2 |   31600 |
+----------------+----------------+-------------+-------------------------------+--------+------+---------+
*/