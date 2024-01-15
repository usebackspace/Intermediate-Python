# Binary files are essential for storing non-textual data, such as images, audio, video etc.

image_file= open('corvette.png', 'rb')
# Read binary data from the image file
binary_data = image_file.read()
image_file.close()

# Create a binary file and write the binary data to it

with open('binary_image_output.bin', 'wb') as binary_file:
    binary_file.write(binary_data)

print(f'Binary file "{'binary_image_output.bin'}" created successfully.')


#============================================================================================

# Open the binary file in binary read mode

binary_file=open('binary_image_output.bin', 'rb')
# Read binary data from the binary file
binary_data = binary_file.read()

# Create an image file and write the binary data to it

with open('restored_image.jpg', 'wb') as image_file:
    image_file.write(binary_data)

print(f'Image file "{'restored_image.jpg'}" created successfully.')
