x= 100
y= 0

# z=x/y
# print(z)
try:
    z=x/y
    print(z)

except ZeroDivisionError:
    print("Error: Number cannot be divided zero")

except NameError as e:
    print(f'Error: {e}')

except SyntaxError as e:
    print(f'Error: {e}')

except TypeError as e:
    print(f'Error: {e}')


