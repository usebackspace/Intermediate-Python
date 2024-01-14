welcome="Welcome to world of Operation"

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


class Marvel:
    def hero(self):
        print('Favourite hero of Marvel Character is Spider-Man')

class Dc:
    def hero(self):
        print('Favourite hero of DC Character is Super-Man')

def willian():                   # Having same function in ModuleOperation1
    print('Thanos')
