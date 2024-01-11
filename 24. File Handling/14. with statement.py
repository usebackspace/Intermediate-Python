
print('----- 1. Reading a file using read() method-----')
with open('Read file.txt', mode='r') as file:
    content = file.read()
    print(f'{content}')
    print(file.closed)
    
print(file.closed)
