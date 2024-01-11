
print('----- 1. Creating a file to write a data with write() method which number of character-----')
file =  open('Text file.txt', mode='w')
number_of_character = file.write("We have created a text file.")

print(f'Number of character in a file is: {number_of_character}')
file.close()

print()

#=========================================================================================================

print('----- 2. Creating a file to write a data with writeline() method-----')

file = open('Text file.txt', mode="w")
list_file =['Captain America','Iron Man','Spider-Man','Black Panther','White Wolf','Thor','Hulk']
# list_file =('Captain America\n','Iron Man\n','Spider-Man\n','Black Panther\n','White Wolf\n','Thor\n','Hulk\n')

file.writelines(list_file)
file.close()

#=========================================================================================================

print('----- 2. Creating a file to write a data with writeline() method using mode="a"-----')

file = open('Text file.txt', mode="a")
list_file =['Captain America','Iron Man','Spider-Man','Black Panther','White Wolf','Thor','Hulk']
# list_file =('Captain America\n','Iron Man\n','Spider-Man\n','Black Panther\n','White Wolf\n','Thor\n','Hulk\n')

file.writelines(list_file)
file.close()
