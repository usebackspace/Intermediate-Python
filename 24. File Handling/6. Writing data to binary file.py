
# print('----- 1. Creating a  Binary file to write a data with mode="w"-----')
# file =  open('Binary file.bin', mode='wb')
# file.write(b'\x48\x65\x6C\x6C\x6F\x2C\x20\x57\x6F\x72\x6C\x64\x21')
# file.close()

# print()

#======================================================================================================
# print('----- 2. Executing a same file in same mode="w" -----')

# file =  open('Binary file.bin', mode='wb')
# file.write(b'\x0A\x42\x79\x74\x65\x73')
# file.close()

print()

#======================================================================================================

# print('----- 3. Appending a data to a file with mode="a"-----')
# file =  open('Binary file.bin', mode='ab')
# file.write(b'\x0A\x42\x79\x74\x65\x73')
# file.close()

print()

#======================================================================================================

print('----- 4. Exclusive creation of a file with mode="x"-----')
file =  open('Binary file.bin', mode='xb')
file.write(b'\x48\x65\x6C\x6C\x6F\x2C\x20\x57\x6F\x72\x6C\x64\x21')
file.close()

# print()