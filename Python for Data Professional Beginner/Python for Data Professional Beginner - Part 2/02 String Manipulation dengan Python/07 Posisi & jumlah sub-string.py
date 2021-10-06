'''
Cara menentukan posisi awal suatu sub-string dan jumlah kemunculan sub-string tersebut pada suatu string. 
'''


teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"

'''
Fitur .find()
Mengembalikan posisi dari sebuah teks (sub-string) lainnya dalam sebuah string.
'''
print(">>> Fitur .find()")
print(teks.find("Apel"))
'''output: 0'''
print(teks.find("malang"))
'''output: 5 => kata malang muncul dimulai dari indeks ke-5 ketika setiap karakter dalam string direpresentasikan sebagai array.'''

'''
Fitur .count()
Menghitung jumlah kemunculan sebuah teks (string) lainnya dalam suatu string (string yang dicari bersifat case sensitive).
'''
print(">>> Fitur .count()")
kemunculan_kata_apel = teks.count("apel")
print(kemunculan_kata_apel)
'''output: 3 => Hal ini dikarenakan kata "Apel" di awal kalimat tidak sama dengan "apel" ("Apel" diawali huruf kapital dan kata yang dicari diawali huruf kecil)'''