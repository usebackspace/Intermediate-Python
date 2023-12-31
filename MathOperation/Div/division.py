# division.py
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


# we will not get the output by normal execution method, we have to use flag in terminal.
# we get all flag in python by command :-        python --help
# -m mod : run library module as a script
    
# command :- python -m PackageName.ModuleName   - If we are inside the MathOperation Folder
# command :- python -m PackageName.SubPackageName.ModuleName   - If we are Outside the MathOperation Folder


#==============================================================================================================
    
# example python -m MathOperation.Div.division        - Outside the MathOperation Folder
# from MathOperation.Mul.multiplication import multiply
# print(multiply(4,5))

#==============================================================================================================

# example python -m Div.division        - Inside the MathOperation Folder
# from Mul.multiplication import multiply
# print(multiply(4,5))