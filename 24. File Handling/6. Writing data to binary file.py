
# print('----- 1. Creating a  Binary file to write a data with mode="w"-----')
# file =  open('Binary file.bin', mode='wb')
# file.write(b'Hello World')
# file.close()

# print()

#======================================================================================================
# print('----- 2. Executing a same file in same mode="w" -----')

# file =  open('Binary file.bin', mode='wb')
# file.write(b'Hello World')
# file.close()

print()

#======================================================================================================

# print('----- 3. Appending a data to a file with mode="a"-----')
# file =  open('Binary file.bin', mode='ab')
# file.write(b'Hello World')
# file.close()

print()

#======================================================================================================

print('----- 4. Exclusive creation of a file with mode="x"-----')
file =  open('Binary file.bin', mode='xb')
file.write(b'Hello World!')
file.close()

# print()