import numpy as np

def tableua(coeff_list):
    '''
    inputs
    obj_coeff: list of coefficients in objective equation
    rest_coeffs: list of list containing restraint coeffs
    
    output: optimum values
    '''
    numBasicVariables = len(coeff_list[0]) - 1
    # create calculation table
    # rows: number of non-basic variables (0 values) + row for objective equation coeffs
    # columns: 0: coeff of basic variable i dno wtf the columns are for
    table = np.full(2+numBasicVariables, numBasicVariables*2+4)
    for i in range(0, numBasicVariables):
        table[0][i+2] = coeff_list[0][i]

    for i in range(numBasicVariables, numBasicVariables*2):
        table[0][i+2] = 0
    

# rearrange the constraints to equalities with a standin variable
# x + y <= 5 and 3x + 2y <= 12 BECOMES s = 5 - x - y and t = 12 - 3x - 2y
# set the new values of new variables to the constant values and variables in objective function to 0
# first column of table is coeffs of variables in objective function and number of added variables
