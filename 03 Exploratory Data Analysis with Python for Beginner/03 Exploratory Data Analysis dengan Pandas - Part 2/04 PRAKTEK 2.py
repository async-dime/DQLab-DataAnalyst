'''
Tampilkan data persebaran dari product_weight_gram
Gunakan standar deviasi dan variance untuk menganalisis lebar persebaran distribusi
'''


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Standar variasi kolom product_weight_gram
order_df.loc[:, "product_weight_gram"].std()
# Varians kolom product_weight_gram
order_df.loc[:, "product_weight_gram"].var()
