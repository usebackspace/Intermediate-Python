
print('----- 1. Creating a file to write a data with mode="w"-----')
file =  open('Text file.txt', mode='w')
file.write("We have created a text file .")
file.close()

print()

#======================================================================================================
print('----- 2. Executing a same file in same mode="w" -----')

# file =  open('Text file.txt', mode='w')
# file.write("We have again excuted with same write mode. So it will overide the data.")
# file.close()

print()

#======================================================================================================

# print('----- 3. Appending a data to a file with mode="a"-----')
# file =  open('Text file.txt', mode='a')
# file.write(" Appending data in to ....We have created a text file .")
# file.close()

print()

#======================================================================================================

# print('----- 4. Exclusive creation of a file with mode="x"-----')
# file =  open('Text file.txt', mode='x')
# file.write(" Exclusive creating a text file .")
# file.close()

# print()