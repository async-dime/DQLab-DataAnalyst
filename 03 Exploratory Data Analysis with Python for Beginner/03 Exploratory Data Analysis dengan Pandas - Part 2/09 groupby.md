# .groupby menggunakan Pandas
Kegunaan .groupby adalah mencari summary dari data frame dengan menggunakan aggregate dari kolom tertentu.

### Contoh penggunaan:

Diberikan dataset bernama df seperti pada gambar dibawah!
![dataset df](df.png)

### Penggunaan groupby:
```sh
df["Score"].groupby([df["Name"]]).mean()
```

Hasil:
```sh
Name
Alisa     72.00
Bobby     57.50
Cathrine  63.75
Name: Score, dtype: float64
```

Penjelasan: komputasi diatas menggunakan kolom ‘Name’ sebagai aggregate dan kemudian menggunakan menghitung mean dari kolom ‘Score’ pada tiap - tiap aggregate tersebut.

### Contoh lainnya:
```sh
df["Score"].groupby([df["Name"], df["Exam"]]).sum()
```

Hasil:
```sh
Name      Exam
Alisa     Semester 1    136
          Semester 2    152
Bobby     Semester 1    78
          Semester 2    152
Cathrine  Semester 1    132
          Semester 2    123
Name: Score, dtype: float64
```

Penjelasan: komputasi diatas menggunakan kolom ‘Name’ dan ‘Exam’ sebagai aggregate dan kemudian menggunakan menghitung sum dari kolom ‘Score’ pada tiap - tiap aggregate tersebut.