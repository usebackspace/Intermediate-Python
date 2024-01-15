
# print('----- 1. Creating a  Binary file to write a data with mode="w"-----')
file =  open('Binary file.bin', mode='wb')
file.write(b'Hello World')
file.close()

print()

#======================================================================================================
print('----- 2. Executing a same file in same mode="w" -----')

# file =  open('Binary file.bin', mode='wb')
# data = [0x48, 0x65, 0x6C, 0x6C, 0x6F]  # ASCII codes for "Hello"
# file.write(bytes(data))
# file.close()

print()

#======================================================================================================

print('----- 3. Appending a data to a file with mode="a"-----')
# file =  open('Binary file.bin', mode='ab')
# file.write(b'\x48\x65\x6C\x6C\x6F\x2C\x20\x57\x6F\x72\x6C\x64\x21')
# file.close()

# print()

#======================================================================================================

# print('----- 4. Exclusive creation of a file with mode="x"-----')
# file =  open('Binary file.bin', mode='xb')
# file.write(b'Hello World!')
# file.close()

# print()


#=======================================================================================================

#  Representing "Hello, World!" in binary, in different aspects:

# 1. ASCII Text Representation:

# - Each character is encoded using 7-bit ASCII codes:


# 01001000 01100101 01101100 01101100 01101111 00101100 00100000 01010111 01101111 01110010 01101100 01100100 00100001


# 2. Machine Code (x86):

# - The actual binary instructions to print "Hello, World!" on a specific hardware architecture:

# 
# 48 65 6c 6c 6f 2c 20 57 6f 72 6c 64 21 0a
# 

# 3. Executable File:

# - Combines machine code with other data and metadata:

# 
# 0d 0a 48 65 6c 6c 6f 2c 20 57 6f 72 6c 64 21 20 20 0a 00 00 ... (more complex structure)
# 

# 4. Python Representation:

# - Using bytes or bytearray objects:

# python
# hello_bytes = b'Hello, World!'
# print(hello_bytes)  # Output: b'Hello, World!'
# 

# Important Notes:

# - Humans usually use hexadecimal notation (base 16) for readability:
#    - ASCII: 48 65 6C 6C 6F 2C 20 57 6F 72 6C 64 21
#    - x86 machine code: B8 21 4C 00 00 BA 0E 00 00 00 BB 01 00 00 00 B9 40 00 00 00 CD 80
# - The actual binary representation depends on the specific context and purpose.
