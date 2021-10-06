'''
Berdasarkan potongan kode berikut
'''

file = open("hello.txt","w")
file.writelines(["Halo\n", "Belajar Python\n", "Menyenangkan!\n"])
file.close()
file = open("hello.txt","r")
for line in file:
    print(line)
    break

'''
Potongan kode akan menghasilkan output:

Ans: "Halo"
'''