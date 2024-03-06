import math
from query_preppro import query_to_dnf
import sympy
import joblib
from process import corpus
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import time

first = True
_corpus = corpus("", 10)
matrix = ''
vectorizer = ''
feature_names = dict()
def get_tfidf_value(document_text, word):
    global matrix
    global vectorizer 
    global feature_names
    
    try:
        result = matrix[document_text,word] 
        return result
    except:
        return 0

def sim(query_list, query_dnf):
    global matrix
    global feature_names
    literals_total = len(query_list)
     
    scores = dict()
    for doc_index,doc in enumerate(_corpus.docs):
        _or = 0
        _or_count = 0
        for clause in query_dnf.args:
            _or_count += 1
            if not isinstance(clause, sympy.logic.boolalg.And):
                # Obtener el termino
                term = clause.as_independent(*clause.free_symbols)[1]
                # Obtener el indice del termino en la matriz
                try:
                    term_index = feature_names[str(term)]
                except:
                    continue
                 
                
                # Ver el valor de la matriz en la posicion doc, term
                #tfxidf_term = extended_matrix[doc.index, term_index]

                #tfxidf_term = matrix[doc_index][term_index]
                tfxidf_term = get_tfidf_value(doc_index,term_index)
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
                    try:
                        term_index = feature_names[str(term)]
                    except:
                        continue

                    # Ver el valor de la matriz en la posicion doc, term
                    #tfxidf_term = extended_matrix[doc.index, term_index]
                    tfxidf_term = get_tfidf_value(doc_index,term_index)
                    
                    _and += math.pow(1 - tfxidf_term, literals_total) if not isinstance(clause, sympy.logic.boolalg.Not) else - (1 - math.pow(tfxidf_term, literals_total))
               
                # Calculo la raiz p-esima 
                _or += math.pow(1 - math.pow(_and/_and_count, 1/literals_total), literals_total)
        
        scores.update({doc_index: math.pow(_or / _or_count, literals_total)})

    scores = dict([item for item in sorted(scores.items(), key=lambda item: item[1], reverse=True) if item[1] > 0])

    
    # for i, (doc, val) in enumerate(scores.items()):
    #     print(f'{doc} , {val}')
    return scores

                    
def init():
    global first
    global matrix
    global feature_names
    global vectorizer
    
    if first:
        mat_url = f'./cranfield_matrix.joblib'
        vec_url = f'./cranfield_vect.joblib'
        matrix = joblib.load(mat_url)
        vectorizer = joblib.load(vec_url)        
        feature_names = vectorizer.get_feature_names_out()
        feature_names = {word: index for index, word in enumerate(feature_names)}

        first = False
        
    

def get_similar_docs(query):
    query_dnf = query_to_dnf(query)

    query_literals = get_literals_from_dnf(query_dnf)

    init()

    scores = sim(query_literals, query_dnf)
    return scores

def get_literals_from_dnf(dnf):
    literals = []
    for disjunct in dnf.args:
        if isinstance(disjunct, sympy.Not):
            literals.append(f"~{str(disjunct.args[0])}")  # Include the negation symbol (~)
        else:
            for literal in disjunct.args:
                # Access the literal directly without using 'as_independent'
                literals.append(str(literal))
    return list(set(literals))
    
#def get_literals_from_dnf(dnf):
#    literals = []
#    for disjunct in dnf.args:
#        if not isinstance(disjunct, sympy.logic.boolalg.And):
#            literals.append(str(disjunct.as_independent(*disjunct.free_symbols)[1]))
#        else:
#            for literal in disjunct.args:
#                # Convertir cada literal a string
#                literals.append(str(literal.as_independent(*disjunct.free_symbols)[1]))
#    print(literals)
#    
#    return literals
#    
    
test_query = 'What or similarity laws '
get_similar_docs(test_query)