

print('----- 1. Reading a file using seek() method -----')

file =  open('Read file.txt', mode='r')
print('Tell-',file.tell())
file.seek(8,0)
content = file.read(2)
print(f'{content}')           # captain America -Am :- Seeked Upto 8 letter
print('Tell-',file.tell())


file.seek(2,1)
content = file.read(3)
print(f'{content}')          # captain -pta :- Seeked Upto 2 letter
print('Tell-',file.tell())

file.close()

print()