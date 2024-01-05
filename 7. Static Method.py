class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Using static methods without creating an instance
sum_result = MathOperations()

print(f'Sum is {sum_result.add(5,3)}')
print(f"Product is: {MathOperations.multiply(4, 6)}")  # Output: Product: 24
