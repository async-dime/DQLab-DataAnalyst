## Statistik Deskriptif dari Data Frame - Part 2

Jika ingin mendapatkan summary statistik dari kolom yang tidak bernilai angka, maka aku dapat menambahkan command include=["object"] pada syntax describe().

![describe object syntax](describe-object-syntax.png)

hasil:

![describe object nilai_skor_df](describe-object-nilai_skor_df.png)

Function describe() dengan include="all" akan memberikan summary statistik dari semua kolom. Contoh penggunaannya:

![describe all nilai_skor-df syntax](describe-all-nilai_skor_df-syntax.png)

hasil:

![describe all nilai_skor_df](describe-all-nilai_skor_df.png)
