## Rename Kolom Data Frame
Pada bagian ini, aku belajar cara mengganti nama kolom dataframe menggunakan Pandas. Mengganti nama kolom pada Pandas dapat dilakukan dengan 2 cara:
  - Menggunakan nama kolom
    - Syntax:
      ```sh
      nama_dataframe.rename(columns={"column_name_before": "column_name_after"}, inplace=True)
      ```
    - contoh:
      ```sh
      nilai_skor_df.rename(columns={"Age": "Umur"}, inplace=True)
      ```

  - Menggunakan indeks kolom
    - Syntax:
      ```sh
      nama_dataframe.columns.values[no_of_colum] = "column_name_after"
      ```
    - contoh:
      ```sh
      nilai_skor_df.columns.values[0] = "Umur"
      ```
