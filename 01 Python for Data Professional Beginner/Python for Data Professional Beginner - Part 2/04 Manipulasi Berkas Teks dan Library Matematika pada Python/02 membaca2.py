import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


'''Membaca file hello.txt dengan fungsi readlines()'''
print(">>> Membaca file hello.txt dengan fungsi readlines()")
'''
pertama buka file dengan fungsi open()
file = open("hello.txt", "r")
'''
file = open(os.path.join(__location__, 'hello.txt'))
all_lines = file.readlines()
file.close()
print(all_lines)
# Membaca file hello.txt dengan menerapkan looping
print(">>> Membaca file hello.txt dengan menerapkan looping")
'''
pertama buka file dengan fungsi open()
file = open("hello.txt", "r")
'''
file = open(os.path.join(__location__, 'hello.txt'))
for line in file:
    print(line)
file.close()