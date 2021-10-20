import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.shape)


'''
output:

In [1]: import pandas as pd
        order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
        print(order_df.shape)

(49999, 12)
'''