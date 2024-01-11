
print('----- 1. Reading a file using readlines() method-----')
file =  open('Read file.txt', mode='r')
content = file.readlines()

print(f'{content}')

file.close()

print()

#==========================================================================================================

print('----- 2. Reading a file using readlines() method using for loop-----')
file =  open('Read file.txt', mode='r')
content = file.readlines()

for cont in content:
    print(f'{cont}')

file.close()

print()