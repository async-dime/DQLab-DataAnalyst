'''
Cobalah untuk mencari rata rata dari price per payment_type dari dataset order_df ("https://storage.googleapis.com/dqlab-dataset/order.csv")!
'''


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Hitung rata rata dari price per payment_type
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)


'''
output:

payment_type
credit card        2.600706e+06
debit card         2.611974e+06
e-wallet           2.598562e+06
virtual account    2.619786e+06
Name: price, dtype: float64
'''