# Import library math
import math


'''
Fungsi math.log()
Menerima input berupa dua buah bilangan (asumsikan x dan y) dan mengembalikan sebuah bilangan (z) 
di mana z merupakan hasil log basis y dari x (atau dengan kata lain x merupakan hasil pemangkatan dari z terhadap y)
'''
print(">>> Fungsi math.log()")
'''x = log basis 2 dari 8, output => 3'''
x = math.log(8,2)
'''y = log basis 3 dari 81, output => 4'''
y = math.log(81,3)
'''z = log basis 10 dari 10000, output => 4'''
z = math.log(10000,10)
print(x)
print(y)
print(z)


'''
Fungsi math.sqrt()
Menerima input berupa sebuah bilangan dan mengembalikan hasil akar pangkat dua (akar kuadrat) dari bilangan tersebut
'''
print(">>> Fungsi math.sqrt()")
'''akar kuadrat dari 100, output => 10'''
x = math.sqrt(100)
print(x)
'''akar kuadrat dari 2, output => 1.4142135'''
y = math.sqrt(2)
print(y)


'''
Fungsi math.copysign()
Menerima input berupa dua buah bilangan dan mengembalikan hasil bilangan pertama yang dikalikan dengan tanda dari bilangan kedua
'''
print(">>> Fungsi math.copysign()")
x = 10.32
y = -13.87
z = -15
'''output => -10.32'''
x = math.copysign(x, z)
'''output => -13.87'''
y = math.copysign(y, z)
'''output => -15'''
z = math.copysign(z, 10)
print(x)
print(y)
print(z)