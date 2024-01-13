
print('----- 1. Reading a file using with statement-----')
with open('Read file.txt', mode='r') as file:
    content = file.read()
    print(f'{content}')
    print(file.closed)   # Will check whether the file is closed or not, return True if file is closed else False.
    
print(file.closed)


input_file_path = 'python.txt'
output_file_path = 'binary_output.bin'

# Read the text file
with open(input_file_path, 'r', encoding='utf-8') as text_file:
    text_content = text_file.read()

# Convert the text content to binary
binary_content = text_content.encode('utf-8')
print(binary_content)

# Write the binary content to a new file
with open(output_file_path, 'wb') as binary_file:
    binary_file.write(binary_content)
