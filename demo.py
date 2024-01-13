def text_to_binary(text):
    binary_result = ''.join(format(ord(char), 'b') for char in text)
    return binary_result

# Example usage:
input_text = "Hello, World!"
binary_representation = text_to_binary(input_text)
print(binary_representation)
