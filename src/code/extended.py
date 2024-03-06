import math
import sympy
import math

def get_tfidf_value(document_text, word):
    global matrix
    global vectorizer 
    global feature_names
    
    try:
        result = matrix[document_text,word] 
        return result
    except:
        return 0
               
def boolean_extended(query_list, query_dnf,_corpus):
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
    return scores
