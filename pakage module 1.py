# Import PackageName.SubPackageName.moduleName

print('---- Import PackageName.SubPackageName.moduleName ----')

import MathOperation.Add.addition

#Accessing Variable, class, function
#PackageName.SubPackageName.moduleName.function_name()
print(f'Addition is {MathOperation.Add.addition.add(10,20)}')

print()
#==================================================================================================

# from PackageName import moduleName
print('---- from PackageName import moduleName ----')

from MathOperation.Div import division

#Accessing Variable, class, function
# moduleName.function_name()
print(f'Division is: {division.divide(10,2)}')

print()

#==================================================================================================
# from PackageName.SubPackage.moduleName import function_name()

print('----from PackageName.SubPackage.moduleName import function_name()----')

from MathOperation.Mul import multiplication

# Accessing Variable, class, function
# function_name()
print(f'Multiplication is: {multiplication.multiply(10,20)}')

