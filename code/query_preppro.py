from sympy import sympify, to_dnf
from prepro import preprocess_documents
import prepro

def query_to_dnf(query):
    query = prepro.preprocess_documents([query], True)[0]
    
    processed_query = query.lower().replace('and', '&').replace('&&', '|').replace('or', '|').replace('||', '|').replace('not', '~')
    
    try:
        # Convertir a expresión sympy y aplicar to_dnf. Cuando no existe operador entre un literal y un parentesis abiierto Sympy asume que es un AND
        query_expr = sympify(processed_query, evaluate=False)
        # print('logical expression: ', query_expr)
        query_dnf = to_dnf(query_expr, simplify=True)
    except:
        return None

    return query_dnf

# consulta = "A AND (B OR NOT C)"
# print('query: ', consulta)
# consulta_dnf = query_to_dnf(consulta)
# print('dnf expression: ', consulta_dnf)
# print('\n')

# consulta = "A (B OR NOT C)"
# print('query: ', consulta)
# consulta_dnf = query_to_dnf(consulta)
# print('dnf expression: ', consulta_dnf)
# print('\n')

# consulta = "A and  C and B and NOT Not C"
# print('query: ', consulta)
# consulta_dnf = query_to_dnf(consulta)
# print('dnf expression: ', consulta_dnf)
# print('\n')

# consulta = "A C and B and NOT Not C"
# print('query: ', consulta)
# consulta_dnf = query_to_dnf(consulta)
# print('dnf expression: ', consulta_dnf)
# print('\n')

# consulta = "A C B and NOT Not C"
# print('query: ', consulta)
# consulta_dnf = query_to_dnf(consulta)
# print('dnf expression: ', consulta_dnf)
# print('\n')

# consulta = "A (C and NOT Not C)"
# print('query: ', consulta)
# consulta_dnf = query_to_dnf(consulta)
# print('dnf expression: ', consulta_dnf)
# print('\n')

# consulta = "A (C (NOT Not b))"
# print('query: ', consulta)
# consulta_dnf = query_to_dnf(consulta)
# print('dnf expression: ', consulta_dnf)
# print('\n')

# consulta = "A B OR NOT C)"
# print('query: ', consulta)
# consulta_dnf = query_to_dnf(consulta)
# print('dnf expression: ', consulta_dnf)
# print('\n')

# consulta = "A B 'OR NOT C)"
# print('query: ', consulta)
# consulta_dnf = query_to_dnf(consulta)
# print('dnf expression: ', consulta_dnf)
# print('\n')

# consulta = "A AND OR B 'OR NOT Not C)"
# print('query: ', consulta)
# consulta_dnf = query_to_dnf(consulta)
# print('dnf expression: ', consulta_dnf)
# print('\n')
