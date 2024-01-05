print(100+200)

print()
#========================================================================================================
# __add__(self,other)

print(int.__add__(100,200))

print()
#========================================================================================================

class Point1:
    def __init__(self, x):
        self.x = x
        
    def __add__(self, other):      
        return self.x + other.x
        

class Point2:
    def __init__(self, x):
        self.x = x

p1 = Point1(10)
p2 = Point2(20)


print(p1+p2)     #Point1.__add__(self, other)       #Point1.__add__(p1,p2)
# print(Point1.__add__(p1,p2))


# 10+20                 int.__add__(10,20)
# 'hello'+ 'World'      str.__add__('hello','world')
# p1+p2                 Point1.__add__(p1,p2)