
print('----- 1. Reading a file using tell() method -----')

file =  open('Read file.txt', mode='r')

print(file.tell())
content = file.read(3)
print(f'{content}')

print(file.tell())
content2 = file.read(3)
print(f'{content2}')

print(file.tell())
content3 = file.read(5)
print(f'{content3}')

print(file.tell())
content4 = file.read(3)
print(f'{content4}')
print(file.tell())


file.close()

print()
