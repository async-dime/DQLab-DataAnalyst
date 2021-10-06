# Import library math
import math


'''
Fungsi math.ceil()
Menerima input berupa bilangan dan mengembalikan pembulatan ke atas untuk bilangan input.
'''
print(">>> Fungsi math.ceil()")
x = 10.32
y = 13.87
z = -12.87
x_ceil = math.ceil(x)
y_ceil = math.ceil(y)
z_ceil = math.ceil(z)
print(x_ceil)
print(y_ceil)
print(z_ceil)


'''
Fungsi math.floor()
Menerima input berupa bilangan dan mengembalikan hasil pembulatan ke bawah untuk bilangan input.
'''
print(">>> Fungsi math.floor()")
x_floor = math.floor(x)
y_floor = math.floor(y)
print(x_floor)
print(y_floor)


'''
Fungsi math.fabs()
Menerima input berupa bilangan dan mengembalikan hasil absolut dari bilangan input.
'''
print(">>> Fungsi math.fabs()")
x = 10.32
y = -13.87
x = math.fabs(x)
y = math.fabs(y)
print(x)
print(y)


'''
Fungsi math.factorial()
Menerima input berupa bilangan dan mengembalikan hasil faktorial dari bilangan input
'''
print(">>> Fungsi math.factorial()")
x_factorial = math.factorial(5)
print(x_factorial)


'''
Fungsi math.fsum()
Menerima input berupa tipe data collection (tuple, list, etc.) dan mengembalikan hasil penjumlahan setiap elemennya.
'''
print(">>> Fungsi math.fsum()")
x = [1, 2, 3, 4, 5, 6, -6, -5, -4]
total = math.fsum(x)
print(total)