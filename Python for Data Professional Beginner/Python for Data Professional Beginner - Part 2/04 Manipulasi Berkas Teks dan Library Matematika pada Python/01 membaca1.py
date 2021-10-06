import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

'''Membaca file hello.txt dengan fungsi read()'''
print(">>> Membaca file hello.txt dengan fungsi read()")
'''
pertama buka file dengan fungsi open()
file = open("hello.txt", "r")
'''
file = open(os.path.join(__location__, 'hello.txt'))
content = file.read()
file.close()
print(content)


'''Membaca file hello.txt dengan fungsi readline()'''
print(">>> Membaca file hello.txt dengan fungsi readline()")
'''
pertama buka file dengan fungsi open()
file = open("hello.txt", "r")
'''
file = open(os.path.join(__location__, 'hello.txt'))
first_line = file.readline()
second_line = file.readline()
file.close()
print(first_line)
print(second_line)