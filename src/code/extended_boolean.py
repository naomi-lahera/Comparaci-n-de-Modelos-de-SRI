import math
from query_preppro import query_to_dnf
import sympy
import joblib
from process import corpus



first = True
_corpus = corpus('cranfield', 10)
matrix = ''
vectorizer = ''
feature_names = ''
extended_matrix = ''

def sim(query_list, query_dnf):
    literals_total = len(query_list)
     
    scores = dict()
    
    for doc in _corpus.docs:
        _or = 0
        _or_count = 0
        for clause in query_dnf.args:
            _or_count += 1
            if not isinstance(clause, sympy.logic.boolalg.And):
                # Obtener el termino
                term = clause.as_independent(*clause.free_symbols)[1]
                # Obtener el indice del termino en la matriz
                term_index = feature_names.index(term)
                
                # Ver el valor de la matriz en la posicion doc, term
                tfxidf_term = extended_matrix[doc.index, term_index]
                
                # Annadir el valor de ese termino en dependencia de si es un not o no
                _or += math.pow(tfxidf_term, literals_total) if not isinstance(clause, sympy.logic.boolalg.Not) else - math.pow(tfxidf_term, literals_total)
            else:
                _and = 0
                _and_count = 0
                for literal in clause.args:  
                    _and_count += 1  
                    # Obtener el termino
                    term = literal.as_independent(*literal.free_symbols)[1]
                    # Obtener el indice del termino en la matriz
                    term_index = feature_names.index(term)

                    # Ver el valor de la matriz en la posicion doc, term
                    tfxidf_term = extended_matrix[doc.index, term_index]
                    
                    _and += math.pow(1 - tfxidf_term, literals_total) if not isinstance(clause, sympy.logic.boolalg.Not) else - (1 - math.pow(tfxidf_term, literals_total))
               
                # Calculo la raiz p-esima 
                _or += math.pow(1 - math.sqrt(_and/_and_count, 1/literals_total), literals_total)
        
        scores.update(doc.index, math.pow(_or / _or_count, literals_total))
    scores = dict(sorted(scores.items(), key=lambda item: item[1]))
    print([doc[0] for doc in scores.items])
                    
def init():
    global first
    global matrix
    global feature_names
    global extended_matrix
    
    mat_url = f'./../cranfield_matrix.joblib'
    
    if first:
        matrix = joblib.load(mat_url)  
        feature_names = matrix.get_feature_names()
        extended_matrix = matrix.fit_transform(_corpus.preprocess_docs)
        first = False
    
def get_similar_docs(query):
    query_dnf = query_to_dnf(query)
    print(query_dnf)
    
    query_literals = get_literals_from_dnf(query_dnf)
    print(query)
    
    sim(query_literals, query_dnf, matrix)
    
def get_literals_from_dnf(dnf):
    literals = []
    for disjunct in dnf.args:
        if not isinstance(disjunct, sympy.logic.boolalg.And):
            literals.append(str(disjunct.as_independent(*disjunct.free_symbols)[1]))
        else:
            for literal in disjunct.args:
                # Convertir cada literal a string
                literals.append(str(literal.as_independent(*disjunct.free_symbols)[1]))
    print(literals)
    
    return literals
    
    
test_query = 'house or number and value'
get_similar_docs(test_query)