print('----- Copying file-----')
file =  open('Read file.txt', mode='r')    # Before reading first we have to read
file1 =  open('Copied file.txt', mode='w') # After reading we will have to write the read file

content = file.read()    # File will be read and return in content.
file1.write(content)     # Now we will write the read file into file1 object/file handler.
print(f'{content}') 
file.close()

print()
