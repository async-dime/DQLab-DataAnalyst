import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

plt.figure(figsize=(15, 5))

'''
  - color:      Mengubah warnanya (sama seperti di title)
  - linewidth:  Mengubah ketebalan line/garisnya (dalam satuan px)
  - linestyle:  Mengubah jenis dari garis. 
                    > '-' atau 'solid' untuk garis tak terputus (seperti pada default), 
                    > '--' atau 'dashed' untuk garis putus-putus, 
                    > ':' atau 'dotted' untuk garis berupa titik-titik, 
                    > '-.' atau ‘dashdot’ untuk garis dan titik bergantian.
  - marker:     Mengubah tipe points/titik data di chart. 
                Ada banyak sekali kemungkinan nilai untuk marker ini, 
                Yang biasanya digunakan yaitu: 
                    > ‘.’ untuk bulatan kecil/titik, 
                    > ‘o’ untuk bulatan agak besar, 
                    > ‘s’ untuk persegi, ‘D’ untuk diamond/wajik, 
                    > bentuk-bentuk lain seperti ‘+’, ‘x’, ‘|’, ‘*’.
'''
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.show()