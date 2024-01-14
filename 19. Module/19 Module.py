# Built-In Module
import math

print(math.sqrt(25))

#========================================================================================================

print('---- import modulename ----')
import ModuleOperation

print(ModuleOperation.welcome)                                    # modulename.variable_name

print()

print('Addition of two numbers :',ModuleOperation.add(30,40))     # modulename.function_name()

print()

#Making object of Marvel class from ModuleOperation module
m= ModuleOperation.Marvel()                                       # modulename.class_name
m.hero()

print()

#Making object of DC class from ModuleOperation module
m= ModuleOperation.Dc()
m.hero()

print()

#=============================================================================================================

print('---- import modulename as alias_name ----')
import ModuleOperation as mo

print(mo.welcome)                                                    # alias_name.variable_name

print()

print('Subtaction of two numbers :',mo.subtract(30,40))              # alias_name.function_name()

print()

#Making object of Marvel class from ModuleOperation module
m= mo.Marvel()                                                       # alias_name.class_name
m.hero()

print()

#Making object of DC class from ModuleOperation module
m= mo.Dc()
m.hero()

print()

#=============================================================================================================

print('---- from modulename as import var_name, class_name, function_name ----')

# If we import particular variable, function or classes we don't need to write modulename.function_name()... etc
# simply we have to write  variable, function or class name

from ModuleOperation import welcome,Marvel as Ml,Dc

print(welcome)                                                          # variable_name

print()

# As we have not imported add function it will show error while accessing the add function
# print('Addition of two numbers :',add(30,40))     # modulename.function_name()


#Making object of Marvel class from ModuleOperation module
m= Ml()                                                                # class_name
m.hero()

print()

#Making object of DC class from ModuleOperation module
m= Dc()                                                                # class_name
m.hero()

print()

#=============================================================================================================

print('---- from modulename as import * ----')

# from modulename as import * 
# Import all variable, calsses, function etc from the module 

from ModuleOperation import *

print(welcome)                                                              # variable_name

print()

# As we have not imported add function it will show error while accessing the add function
# print('Addition of two numbers :',add(30,40))     # modulename.function_name()

#Making object of Marvel class from ModuleOperation module
m= Marvel()                                                                 # class_name
m.hero()

print()

#Making object of DC class from ModuleOperation module
m= Dc()                                                                     # class_name
m.hero()

print()