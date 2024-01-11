
print('----- 1. Reading a file using readline() method-----')
file =  open('Read file.txt', mode='r')
content = file.readline()

print(f'{content}')

file.close()

print()

#=========================================================================================================

print('----- 2. Reading a file using readline() method line by line -----')

file =  open('Read file.txt', mode='r')
content = file.readline()
content2 = file.readline()
content3 = file.readline()
content4 = file.readline()

print(f'Line 1: {content}')
print(f'Line 2: {content2}')
print(f'Line 3: {content3}')
print(f'Line 4: {content4}')

file.close()

print()

#=========================================================================================================

print('----- 3. Reading a file using readline() method using a while loop-----')
file =  open('Read file.txt', mode='r')
content = file.readline()

while content:
    print(f'{content}')
    content = file.readline()

file.close()

print()


