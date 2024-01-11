print('----- Copying file-----')
file =  open('Read file.txt', mode='r')
file1 =  open('Copied file.txt', mode='w')

content = file.read()
file1.read(content)
print(f'{content}') 
file.close()

print()
