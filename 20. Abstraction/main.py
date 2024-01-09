from circle import Circle
from rectangle import Rectangle

print('---- Area and Perimeter of Rectangle ----')

rect =Rectangle(4,5)

print(f'Area of rectangle : {rect.area()}')

print(f'Perimeter of rectangle : {rect.perimeter()}')

# rect.shape()  # This is a concrete method

print()

#============================================================================================================
print('---- Area and Perimeter of Circle ----')
cir =Circle(3)

print(f'Area of circle: {cir.area()}')

print(f'Perimeter of circle: {cir.perimeter()}')