
print('----- 1. Reading a file using with statement-----')
with open('Read file.txt', mode='r') as file:
    content = file.read()
    print(f'{content}')
    print(file.closed)   # Will check whether the file is closed or not, return True if file is closed else False.
    
print(file.closed)

