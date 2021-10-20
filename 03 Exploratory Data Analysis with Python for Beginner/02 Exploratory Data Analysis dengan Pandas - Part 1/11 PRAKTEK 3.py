'''
Pada dataframe order_df
Buatlah quick summary dari segi kuantitas, harga, freight value, dan weight yang dibeli konsumen. 
Juga median dari total pembelian konsumen per transaksi
'''


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Quick summary  dari segi kuantitas, harga, freight value, dan weight
print(order_df.describe())
# Median dari total pembelian konsumen per transaksi kolom price
print(order_df.loc[:, "price"].median())


'''
output:

In [1]: import pandas as pd
        order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
        # Quick summary  dari segi kuantitas, harga, freight value, dan weight
        print(order_df.describe())
        # Median dari total pembelian konsumen per transaksi kolom price
        print(order_df.loc[:, "price"].median())

           quantity         price  freight_value  product_weight_gram
count  49999.000000  4.999900e+04   49999.000000         49980.000000
mean       1.197484  2.607784e+06  104521.390428          2201.830892
std        0.722262  1.388312e+06   55179.844962          3929.896875
min        1.000000  2.000000e+05    9000.000000            50.000000
25%        1.000000  1.410500e+06   57000.000000           300.000000
50%        1.000000  2.610000e+06  104000.000000           800.000000
75%        1.000000  3.810000e+06  152000.000000          1850.000000
max       21.000000  5.000000e+06  200000.000000         40425.000000
2610000.0
'''