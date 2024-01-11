
print('----- 1. Reading a file using read() method-----')
file =  open('Read file.txt', mode='r')
content = file.read()

print(f'{content}')
file.close()

print()

#============================================================================================================

print('----- 2. Reading a file using read() method with particular size -----')

file =  open('Read file.txt', mode='r')
content = file.read(3)
content2 = file.read(3)
content3 = file.read(5)
content4 = file.read(5)

print(f'{content}')
print(f'{content2}')
print(f'{content3}')
print(f'{content4}')

file.close()

print()