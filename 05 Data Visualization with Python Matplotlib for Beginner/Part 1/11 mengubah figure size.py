import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

'''
Ukuran Figure diubah agar memiliki panjang 15 inch, dan lebar 5 inch.
Sehingga line chart-nya bisa memanjang ke kanan dan lebih mudah dilihat trend-nya.
'''
plt.figure(figsize=(15,5))

dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()