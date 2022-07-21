from Tableau_LP import tableua

# z = 6x + 5y
objective = [6, 5, 1]
# rest of coeffs
# x + y <= 5 and 3x + 2y <= 12
coeffs = [objective, [1, 1, 5], [3, 2, 12]]
results = tableua(coeffs)