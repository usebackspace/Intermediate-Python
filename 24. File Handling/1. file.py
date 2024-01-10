file=[]
for i in range(2):
    file.append(input("Enter Name: "))

print(file)

# If we remove the for loop, data inserted in the program will be get deleted automatically.
# Data is available only till the program is exectued


# Creating a file 
file =  open('Demo file.txt', mode='w')
file.write("We have created a text file .")
file.close()