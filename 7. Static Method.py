class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Using static methods without creating an instance
sum_result = MathOperations()

product_result = MathOperations.multiply(4, 6)

print(f'Sum is {sum_result.add(5,3)}')
print(f"Product: {product_result}")  # Output: Product: 24
