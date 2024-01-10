file = open('opening in text and binary mode.txt', mode='w')
file.write('Opening \n file in \t text and binary \\ mode')
file.close()

file = open('opening in text and binary mode.txt', mode='r')
file_data = file.read()                 # Read the file and returns the value
print('Reading file in text mode')
print(file_data)
file.close()

print()

file = open('opening in text and binary mode.txt', mode='rb')
file_data = file.read()
print('Reading file in binary mode')
print(file_data)
file.close()
