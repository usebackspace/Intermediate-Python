
class Addition():
    def operation(self, a, b):
        result = a + b
        print(f"Addition Result: {result}")

class Multiplication(Addition):
    def operation(self, a, b):
        result = a * b
        # super().operation(300,700)
        print(f"Multiplication Result: {result}")

mul = Multiplication()

mul.operation(10,20)