'''
Cari berapa harga maksimum pembelian customer di dataset order_df.
'''


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="price", ascending=False)
print(sort_harga)


'''
output:

                               order_id  ...  product_weight_gram
37085  d7b2d3b902441cf3dd12cd125533217d  ...               1825.0
41958  2711089c7fec59d4dc8483e3c6a12fa3  ...                200.0
3976   f343624eab419250ad81f1ce6be22c93  ...                950.0
21072  c8947a583ab9791a5a9d02384cb84302  ...                550.0
47074  f6134169ca6f0cdfbe6458ebb5731613  ...              10600.0
22618  a767765cf25c6fcfd8307499da9205d2  ...                200.0
5273   10bf9305aa4d5fb3382720adad789a40  ...                200.0
34883  c262a5f352a22159735734b273a4b888  ...                650.0
2006   1b01e824ff3005e8108c5112f41c219c  ...              14600.0
11935  4ca6a87f196ea892c5abc4e84748fbde  ...               3100.0
46085  6aa1b68888b0cf160c7072009c46ea24  ...                460.0
41755  d0bff47153ef056bb4f884a2ec2f0691  ...                800.0
3590   d5a2a83ddd838aa8ea9297e7d3c773fb  ...                405.0
45800  7f2646b3858bd8c12613670a0da91593  ...               1350.0
27763  8031adfac87d3fb5ff7b41a0342aae74  ...                117.0
29265  e2e62108a0daf44573986d823484239a  ...               1300.0
9109   86f18e8bfc05ddce85ea8e1146eac6ee  ...               1383.0
34638  d7068745ac2b7e09a164d2a6791838e6  ...               9950.0
8871   d899e6d4576891e29d5a9d3f1867c6e1  ...               1032.0
29233  b2f924dadc7d30518a67a2c8598df64e  ...               3100.0
8470   0af646de6e8d7191b1020ec0a5defcee  ...               1200.0
4913   c27815f7e3dd0b926b58552628481575  ...               9250.0
48128  387016f36a926f6d861f812a8aeccffb  ...               3008.0
26167  0fcb1e2570afc2d20d3e369a90a39f94  ...                250.0
7000   5762165bd52d70f5a54d4cfe067fe5fd  ...                275.0
12344  0ecbb908b4b062b189e1723ef9a836e2  ...               6700.0
41435  8f81a4191bcbef23cdd139470cb50dda  ...               3900.0
21832  c5f692a4e47f015faa3f8a9b9d36aa03  ...                150.0
10359  385bc274c4cbac59c0bb866c770588dc  ...                114.0
3979   f86b24a45dc34d1b7fcdeb817bf503da  ...              10075.0
...                                 ...  ...                  ...
18925  468459668c11750c4d0a52b54045bf48  ...                600.0
39733  1857ec1a182661136fe7584592437d51  ...                925.0
28692  6649a190e9151aac8d553a45875d4b5e  ...                200.0
8895   1887b26eba419ce20f6fe34a6f88e80a  ...               3500.0
43479  ab1a06760db3f8bd369582042ab2cf03  ...                900.0
8617   fb14d0b924669f4fedd4109bbbfbb736  ...               1383.0
2122   77857b5f4745e31dcc0626a9326f6543  ...              17200.0
4661   d2c2a40d9d3d9479b0784a08930ebc75  ...               6050.0
26336  0301ec492e902f2630234df285fa2a1b  ...                900.0
6791   8908c3c6b8591a4d779bc5a4abf4f951  ...                900.0
13504  d3d5d98dda9bb549d81a9b4b9e404bc2  ...                600.0
27080  2e77e95ff07f298805637dfde7da4b4a  ...               8050.0
31174  9a0a6c39b6be7e1b0f796b6005d52ac4  ...                160.0
18005  f30e9b83b1b7557b48c20dc8cf2e383f  ...               1000.0
25105  d4bc55bf7aa33f5d5d8b6b53d1e2eb8f  ...                417.0
46752  0e19aa2216bf89063fdd8849774aea19  ...                200.0
9004   3462b9aa946649acaf4dbd05d3d61269  ...               6550.0
47671  a3c3508e603e9411b2b69972993bd079  ...                525.0
22607  8d74231228bdbc2e89fc0125abfc1c87  ...                536.0
8212   605a65763ded48a0db12fde2b0106a9b  ...               6400.0
22069  12d34cd89b0be0896cfecdbd41f5e952  ...                600.0
41915  1c8166cad99e5856dfb7d622902c623c  ...                500.0
42520  b14b52f3d9077665df2361f007c8e6ec  ...                150.0
6850   faaf6a860e3ad876765787c9e1a93464  ...                200.0
42025  36cdcd48e9697951eef9c32ef39dc9f3  ...                550.0
33786  0d9e86e02c1a823b20c03ea29d616607  ...               7550.0
42166  54220fcc516cabe9ec84b210c0765ef2  ...               1100.0
31745  59a19c83ff825948739dd1601cc107b6  ...                550.0
42452  9960ee97c2f8d801a200a01893b3942f  ...               6663.0
11939  64619901c45fba79638d666058bf6be6  ...                200.0

[49999 rows x 12 columns]
'''