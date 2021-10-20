import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


'''Menulis ke file hello2.txt dengan mode append'''
# file = open("hello2.txt", "a")
file = open(os.path.join(__location__, 'hello2.txt'), "a")
# fungsi writelines untuk menambah beberapa baris teks
file.writelines([
"\n",
"Sekarang kita belajar menulis dengan menggunakan Python", 
"\n",
"Menulis konten file dengan mode a (append)."
])
file = open(os.path.join(__location__, 'hello2.txt'))
for line in file:
    print(line)
file.close()