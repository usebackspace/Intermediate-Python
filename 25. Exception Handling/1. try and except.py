x= 100
y= 0

# z=x/y
# print(z)
try:
    z=x/y
    print(z)

except ZeroDivisionError:
    print("Error: Number cannot be divided zero")

print()

#==================================================================================================

print('---- Exception as an Object ----')
x= 100
y= 0

# z=x/y
# print(z)
try:
    z=x/y
    print(z)

except ZeroDivisionError as e:
    print(f'Error {e}')

