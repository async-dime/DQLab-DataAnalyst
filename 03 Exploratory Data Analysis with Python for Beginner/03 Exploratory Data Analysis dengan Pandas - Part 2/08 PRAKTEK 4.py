'''
Cobalah untuk mengubah kolom freight_value menjadi shipping_cost dalam data frame order_df, dengan menggunakan fungsi rename()
'''


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
print(order_df)


'''
output:

                               order_id  ...  product_weight_gram
0      2e7a8482f6fb09756ca50c10d7bfc047  ...               1800.0
1      2e7a8482f6fb09756ca50c10d7bfc047  ...               1400.0
2      e5fa5a7210941f7d56d0208e4e071d35  ...                700.0
3      3b697a20d9e427646d92567910af6d57  ...                300.0
4      71303d7e93b399f5bcd537d124c0bcfa  ...                500.0
5      be5bc2f0da14d8071e2d45451ad119d9  ...                400.0
6      0a0837a5eee9e7a9ce2b1fa831944d27  ...               3100.0
7      1ff217aa612f6cd7c4255c9bfe931c8b  ...                200.0
8      22613579f7d11cc59c4347526fc3c79e  ...                600.0
9      356b492aba2d1a7da886e54e0b6212b7  ...                610.0
10     35d3a51724a47ef1d0b89911e39cc4ff  ...               1400.0
11     36989eb07a0de2d3d3129eea35553875  ...               1500.0
12     36989eb07a0de2d3d3129eea35553875  ...               1500.0
13     39d0be719247e3b3a38846ba810197ea  ...                300.0
14     3f72d2b757e725cd48a4726f831c7789  ...                610.0
15     46046adea0e222a29259bad3d922fee8  ...                300.0
16     4d66b3a9d12facad48a3b23cc9fe7898  ...               1850.0
17     50013835d7b14aefb452825864d3e414  ...                100.0
18     51725d3e4bdfc97e28b40543310da8a3  ...               1300.0
19     51725d3e4bdfc97e28b40543310da8a3  ...               1000.0
20     5b1376fe61863fe3508011db309e35fe  ...               1200.0
21     5cb8558cbb7c0c2f00f43468579d3e3c  ...                900.0
22     60762802b48bb6d256d55b013d115013  ...                610.0
23     63638a6806d67773f3adba8534553fff  ...               2100.0
24     65d1e226dfaeb8cdc42f665422522d14  ...                476.0
25     6eb51c1c9c69f78ea9fd4665fb98b7d2  ...                100.0
26     7033745709b7cf1bac7d2533663592de  ...               1200.0
27     711b9be9c346d9ecdb9d38a5e1e7e39b  ...                400.0
28     79ffdd52a918bbe867895a4b183d6457  ...               8600.0
29     80606b26965c5ed21e85a085e0667b63  ...                850.0
...                                 ...  ...                  ...
49969  cee7c304d30da21674177c8c988774c9  ...                100.0
49970  cf76c6e04bd586a2cf526c57144cbede  ...                200.0
49971  d11fc5b9e5bf7a0c4ce41b04a59f0154  ...               1600.0
49972  d11fc5b9e5bf7a0c4ce41b04a59f0154  ...               1600.0
49973  d153b78750c904577222dbe5d1c066fd  ...                700.0
49974  d3b8750f21e85ef7a244c8a0cb8ae7b6  ...                300.0
49975  d6f81840dedabe214cbfa42226e7dfd4  ...               1965.0
49976  d738a4231586b1053ffdc9e064e9b1ab  ...               4100.0
49977  d7491ab46e00584734e88ea402f23e78  ...                 50.0
49978  d74a4114b1ecea21d099a6c7aea88058  ...                425.0
49979  d779d1f64c00cb888484f4b2f5eab951  ...                431.0
49980  d8eb5e8c7fc14da34fc5252a2ca7cfab  ...              15700.0
49981  dc12f9e8414131e62897902a78e0286e  ...                600.0
49982  dc12f9e8414131e62897902a78e0286e  ...                600.0
49983  dd873443c3a8427c7a65cfe4c9671b1a  ...                250.0
49984  df1ca8d699e806b9f7218c3bbedd99aa  ...                300.0
49985  e04d2191af862183e0ebda80377a6a32  ...               4338.0
49986  e09eca55c225b904c8579bb1c56b77b2  ...               8300.0
49987  e18cd51191ffbe2bca934d1d13805164  ...               2600.0
49988  e18cd51191ffbe2bca934d1d13805164  ...               2600.0
49989  e2abaacfbaa87cb128b9c6675bcd2b98  ...                150.0
49990  e35d5b4ff8dc9aeccf9cd8ce63c07a68  ...               1150.0
49991  e59dbfb7d81fd513f1ffa941fe849c57  ...               1064.0
49992  e821c71ba6efed0813bbc0a01a95f24d  ...                925.0
49993  e821c71ba6efed0813bbc0a01a95f24d  ...                925.0
49994  ec88157ad03aa203c3fdfe7bace5ab6b  ...               2425.0
49995  ed60085e92e2aa3debf49159deb34da7  ...               2350.0
49996  ed98c37d860890f940e2acd83629fdd1  ...               2600.0
49997  ed98c37d860890f940e2acd83629fdd1  ...               2600.0
49998  ede4ebbb6e36cbd377eabcc7f5229575  ...               1450.0

[49999 rows x 12 columns]
'''