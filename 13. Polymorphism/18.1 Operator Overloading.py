print('----- Operator Overrloading with two classses ----')
class Point1:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __add__(self, other):      
        return self.x + other.x ,self.y+other.y
 
class Point2:
    def __init__(self, x,y):
        self.x = x
        self.y = y

p1 = Point1(10,100)
p2 = Point2(20,200)


print(p1+p2)    #Point1.__add__(self, other)       #Point1.__add__(p1,p2)
# print(Point1.__add__(p1,p2))

#============================================================================================================
print('----- Operator Overrloading with one class ----')
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the addition operator (+)
    def __add__(self, other):
        return self.x + other.x, self.y + other.y
      
# Creating Point objects
point1 = Point(10, 2)
point2 = Point(3, 4)

# Using the overloaded addition operator
result = point1 + point2
print(result)  # Output: Point(13, 6)
