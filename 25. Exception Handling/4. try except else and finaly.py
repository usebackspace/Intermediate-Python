x= 100
y= 2

# z=x/y
# print(z)
try:
    z=x/y
    print(z)

except ZeroDivisionError:
    print("Error: Number cannot be divided zero")

except NameError as e:
    print(f'Error: {e}')

else:
    print("No exception is raised.")

finally:
    print("Finaly Block wil be executed no matter what, whether an exception occurs or not.")