'''
Cobalah untuk check bagaimana contoh data dari dataframe tersebut dengan fungsi head dengan limit 10 baris!
'''


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.head(10))


'''
output:

In [1]: import pandas as pd
        order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
        print(order_df.head(10))

                           order_id  ...  product_weight_gram
0  2e7a8482f6fb09756ca50c10d7bfc047  ...               1800.0
1  2e7a8482f6fb09756ca50c10d7bfc047  ...               1400.0
2  e5fa5a7210941f7d56d0208e4e071d35  ...                700.0
3  3b697a20d9e427646d92567910af6d57  ...                300.0
4  71303d7e93b399f5bcd537d124c0bcfa  ...                500.0
5  be5bc2f0da14d8071e2d45451ad119d9  ...                400.0
6  0a0837a5eee9e7a9ce2b1fa831944d27  ...               3100.0
7  1ff217aa612f6cd7c4255c9bfe931c8b  ...                200.0
8  22613579f7d11cc59c4347526fc3c79e  ...                600.0
9  356b492aba2d1a7da886e54e0b6212b7  ...                610.0

[10 rows x 12 columns]
'''