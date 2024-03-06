from sympy import sympify, to_dnf,symbols,And
from expasion import expand_query_with_wordnet

def query_to_dnf(query):
    
    processed_query = query
    override_and = ('and','AND','&&','&')
    override_or = ('or','OR','||', '|')
    override_not = ('not','NOT','~')
    override_notp = ('(NOT','(not','~')

    processed_query = [token for token in processed_query.split(' ') if token.isalnum()]

    newFND = ""
    for (i, item) in enumerate(processed_query):
        if item in override_and:
            processed_query[i] = override_and[-1]
            newFND += " & "
        elif item in override_or:
            processed_query[i] = override_and[-1]
            newFND += " | "
        elif item in override_not:
            processed_query[i] = override_not[-1]
            newFND += "~"
        elif item in override_notp:
            processed_query[i] = override_notp[-1]
            newFND += "(~"
        
        else:
            newFND+= processed_query[i]
            if i < len(processed_query)-1 and (not (processed_query[i+1] in override_and)) and (not (processed_query[i+1] in override_or)) and (not (processed_query[i+1] in override_not)):
                newFND+=" & "
    
    newFND = expand_query_with_wordnet(newFND)

    # Convertir a expresión sympy y aplicar to_dnf
    try:
        query_expr = sympify(newFND, evaluate=False)   
    except:
        simb = symbols(newFND)
        query_expr = And(*simb)
        query_expr = sympify(query_expr,evaluate=False)
    query_dnf = to_dnf(query_expr, simplify=True,force=True)
    return query_dnf
