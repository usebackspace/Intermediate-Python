# Import PackageName.moduleName

print('---- Import PackageName.moduleName ----')

import Add.addition

#Accessing Variable, class, function
print(f'Addition is {Add.addition.add(10,20)}')     #PackageName.moduleName.function_name()

print()

#===================================================================================================

# from PackageName import moduleName
print('---- from PackageName import moduleName ----')

from Div import division

#Accessing Variable, class, function
# moduleName.function_name()
print(f'Division is: {division.divide(10,2)}')

print()

#==================================================================================================
# from PackageName.moduleName import function_name()

print('----from PackageName.moduleName import function_name()----')

from Mul import multiplication

# Accessing Variable, class, function
# function_name()
print(f'Multiplication is: {multiplication.multiply(10,20)}')

