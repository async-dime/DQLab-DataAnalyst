'''
Berdasarkan potongan kode berikut
'''

file = open("hello.txt","w")
file.writelines(["Halo", "Belajar Python", "Menyenangkan!"])
file.close()
file = open("hello.txt","w")
file.writeline("Menulis ke dalam file")
file.writeline("menggunakan Python")
file = open("hello.txt","r")
for line in file:
    print(line)

'''
Potongan kode akan menghasilkan output:

Ans: "Menulis ke dalam file" dan "menggunakan Python" secara baris per baris
'''