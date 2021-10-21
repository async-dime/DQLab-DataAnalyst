## Standar Deviasi dan Varians pada Pandas

Varians dan standar deviasi juga merupakan suatu ukuran dispersi atau variasi. Standar deviasi merupakan ukuran dispersi yang paling banyak dipakai. Hal ini mungkin karena standar deviasi mempunyai satuan ukuran yang sama dengan satuan ukuran data asalnya. Sedangkan varians memiliki satuan kuadrat dari data asalnya (misalnya cm^2).

Syntax dari standar deviasi pada Pandas:
```sh
print([nama_dataframe].loc[:, "nama_kolom"].std())
```

Syntax dari varians pada Pandas:
```sh
print([nama_dataframe].loc[:, "nama_kolom"].var())
```
Contoh penggunaan pada dataframe nilai_skor_df:
```sh
print([nilai_skor_df].loc[:, "Age"].std())
print([nilai_skor_df].loc[:, "Score"].var())
```

Hasil:

```sh
2.701851217
152.8
```
