from sympy import sympify, symbols,to_dnf,And

# Define los símbolos lógicos
simb = symbols('what are the structural aeroelastic problems associated high speed aircraft')

# Ahora, puedes convertir la cadena de texto en una expresión lógica de SymPy
a = 'what & are & the & structural & aeroelastic & problems & associated & with & high & speed & aircraft'
query_expr = And(*simb)

query_expr = sympify(query_expr,evaluate=False)
query_dnf = to_dnf(query_expr, simplify=True,force=True)


print(query_expr)
print(query_dnf)
