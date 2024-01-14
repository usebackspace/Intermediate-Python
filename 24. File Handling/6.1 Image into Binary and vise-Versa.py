# Binary files are essential for storing non-textual data, such as images, audio, video etc.

image_file= open('corvette.png', 'rb')
# Read binary data from the image file
binary_data = image_file.read()
image_file.close()

# Create a binary file and write the binary data to it
output_binary_file_path = 'binary_image_output.bin'
with open(output_binary_file_path, 'wb') as binary_file:
    binary_file.write(binary_data)

print(f'Binary file "{output_binary_file_path}" created successfully.')


#============================================================================================

# Open the binary file in binary read mode
binary_file_path = 'binary_image_output.bin'
binary_file=open(binary_file_path, 'rb')
# Read binary data from the binary file
binary_data = binary_file.read()

# Create an image file and write the binary data to it
output_image_file_path = 'restored_image.jpg'
with open(output_image_file_path, 'wb') as image_file:
    image_file.write(binary_data)

print(f'Image file "{output_image_file_path}" created successfully.')
