class A:
    def __init__(self):
        print('class A')

class B(A):
    def __init__(self):
        super().__init__()
        print('Class B')

class C(A):
    def __init__(self):
        super().__init__()
        print('Class C')

class D(B,C):
    def __init__(self):
        super().__init__()
        print('Class D')

d=D()
# b=B()