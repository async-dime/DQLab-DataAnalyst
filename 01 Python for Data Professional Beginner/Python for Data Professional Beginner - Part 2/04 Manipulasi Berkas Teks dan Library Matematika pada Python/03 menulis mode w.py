import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


'''Menulis ke file hello1.txt'''
# file = open("hello.txt", "w")
file = open(os.path.join(__location__, 'hello1.txt'), "w")
file.write("Sekarang kita belajar menulis dengan menggunakan Python")
file.write("\n")
file.write("Menulis konten file dengan mode w (write).")
file = open(os.path.join(__location__, 'hello1.txt'))
for line in file:
    print(line)
file.close()