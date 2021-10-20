'''
Untuk menentukan berapa jumlah data yang tersimpan di setiap elemen pada tuple/list, aku dapat menggunakan fungsi buit-in len(). 
'''
# Tuple
print(">>> Tuple")
tuple_menu = ('Gado-gado','Ayam Goreng','Rendang','Ketoprak')
jumlah_menu = len(tuple_menu)
print(jumlah_menu)
# List
print(">>> List")
list_menu = ['Gado-gado','Ayam Goreng','Rendang','Ketoprak']
jumlah_menu = len(list_menu)
print(jumlah_menu)

'''
Mengkonversi berbagai tipe data collection.
'''
# Mengkonversi sebuah list ke sebuah set
print(">>> Konversi tipe data")
list_buah = ['Apel', 'Apel', 'Jeruk', 'Markisa', 'Jeruk', 'Markisa', 'Apel']
set_buah = set(list_buah)
print(set_buah)
# Mengkonversi sebuah set ke sebuah list
list_buah = list(set_buah)
list_buah.sort()
print(list_buah)