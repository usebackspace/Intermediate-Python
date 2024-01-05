# main_program.py
from MathOperation.Add.addition import add
from MathOperation.Sub.subtraction import subtract
from MathOperation.Mul.multiplication import multiply
from MathOperation.Div.division import divide

def main():
    x = 10
    y = 2

    result_add = add(x, y)
    result_subtract = subtract(x, y)
    result_multiply = multiply(x, y)
    result_divide = divide(x, y)

    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")
    print(f"Multiplication: {result_multiply}")
    print(f"Division: {result_divide}")

