'''
Fitur .split()
Memecah sebuah string berdasarkan string lainnya ke dalam sebuah list.
'''
print(">>> Fitur .split()")
bilangan = "ani dan budi dan wati dan johan"
karakter = bilangan.split("dan")
print(karakter)
kata = bilangan.split(" ")
print(kata)

'''
Fitur .join()
Menggabungkan sebuah list yang berisikan string berdasarkan sebuah string yang telah didefinisikan.
'''
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
kalimat = pemisah.join(karakter)
print(kalimat)

'''
Fitur .replace()
Menggantikan kemunculan suatu string tertentu dengan string lainnya dalam sebuah string.
'''
print(">>> Fitur .replace()")
kalimat = "apel malang apel yang paling segar, apel sehat, apel nikmat"
kalimat = kalimat.replace("apel", "jeruk")
print(kalimat)