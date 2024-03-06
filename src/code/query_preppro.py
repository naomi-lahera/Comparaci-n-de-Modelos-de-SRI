from sympy import sympify, to_dnf, symbols, And
from expasion import expand_query_with_wordnet
from prepro import preprocess_documents

def query_to_dnf(query):
    """
    Convierte una consulta en su forma Disjunctive Normal Form (DNF) utilizando SymPy y expansión de consultas con WordNet.

    La función procesa primero la consulta utilizando funciones de preprocesamiento, luego expande la consulta con sinónimos de WordNet y finalmente convierte la consulta en DNF.

    Parámetros:
    - query (str): La consulta a convertir en DNF.

    Retorna:
    - sympy.logic.boolalg.And: La consulta en DNF, representada como una expresión booleana de SymPy.

    Notas:
    - La función utiliza la biblioteca SymPy para convertir la consulta en una expresión booleana y luego en DNF.
    - La expansión de la consulta con sinónimos de WordNet se realiza para mejorar la recuperación de información al incluir términos relacionados.
    - La función maneja operadores lógicos 'and', 'or', 'not' y sus variantes en mayúsculas y con símbolos, reemplazándolos por sus equivalentes en minúsculas y con símbolos.
    """
    processed_query = preprocess_documents(query, True)
    override_and = ('and', 'AND', '&&', '&')
    override_or = ('or', 'OR', '||', '|')
    override_not = ('not', 'NOT', '~')
    override_notp = ('(NOT', '(not', '~')

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
            newFND += processed_query[i]
            if i < len(processed_query)-1 and (not (processed_query[i+1] in override_and)) and (not (processed_query[i+1] in override_or)) and (not (processed_query[i+1] in override_not)):
                newFND += " & "
    
    newFND = expand_query_with_wordnet(newFND)

    # Convertir a expresión sympy y aplicar to_dnf
    try:
        query_expr = sympify(newFND, evaluate=False)   
    except:
        simb = symbols(newFND)
        query_expr = And(*simb)
        query_expr = sympify(query_expr, evaluate=False)
    query_dnf = to_dnf(query_expr, simplify=True, force=True)
    return query_dnf
