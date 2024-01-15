
print('----- 1. Reading a file using tell() method -----')

file =  open('Read file.txt', mode='r')

print('tel-1',file.tell())
content = file.read(3)
print(f'{content}')

print('tel-2',file.tell())
content2 = file.read(3)
print(f'{content2}')

print('tel-3',file.tell())
content3 = file.read(5)
print(f'{content3}')

print('tel-4',file.tell())
content4 = file.read(3)
print(f'{content4}')
print('tel-5',file.tell())


file.close()

print()
