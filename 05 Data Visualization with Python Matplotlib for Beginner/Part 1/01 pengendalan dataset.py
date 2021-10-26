import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())



'''
Penjelasan:

  - order_id : ID dari order/transaksi, 1 transaksi bisa terdiri dari beberapa produk, tetapi hanya dilakukan oleh 1 customer
  - order_date : tanggal terjadinya transaksi
  - customer_id : ID dari pembeli, bisa jadi dalam satu hari, 1 customer melakukan transaksi beberapa kali
  - city : kota tempat toko terjadinya transaksi
  - province : provinsi (berdasarkan city)
  - product_id : ID dari suatu product yang dibeli
  - brand : brand/merk dari product. Suatu product yang sama pasti memiliki brand yang sama
  - quantity : Kuantitas/banyaknya product yang dibeli
  - item_price : Harga dari 1 product (dalam Rupiah). Suatu product yang sama, bisa jadi memiliki harga yang berbeda saat dibeli
'''