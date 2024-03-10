import math
import sympy
import math


dislike = dict()

def get_tfidf_value(document_text, word, matrix):
    """
    Obtiene el valor TF-IDF de una palabra específica en un documento dado, utilizando una matriz de valores TF-IDF.

    Parámetros:
    - document_text (int): El índice del documento en la matriz.
    - word (str): La palabra para la cual se busca el valor TF-IDF.
    - matrix (numpy.ndarray): La matriz de valores TF-IDF, donde cada fila representa un documento y cada columna representa una palabra.

    Retorna:
    - float: El valor TF-IDF de la palabra en el documento especificado. Retorna 0 si no se puede obtener el valor.
    """
    try:
        result = matrix[document_text, word] 
        return result
    except:
        return 0



def boolean_extended(query_id, query_list, query_dnf, _corpus, matrix, feature_names,feedback):
    """
    Calcula y devuelve una puntuación para cada documento en el corpus basada en una consulta dada, 
    utilizando una representación en Disjunctive Normal Form (DNF) de la consulta y una matriz de 
    valores TF-IDF.

    Esta función implementa una versión extendida del modelo booleano para la recuperación de información, 
    donde se toman en cuenta tanto los términos positivos como negativos en la consulta, y se aplica una 
    ponderación basada en el número de literales en la consulta.

    Parámetros:
    - query_list (list): Una lista de términos en la consulta.
    - query_dnf (sympy.logic.boolalg.And): La consulta en Disjunctive Normal Form (DNF), donde cada componente 
      de la consulta es una conjunción de términos.
    - _corpus (Corpus): Un objeto Corpus que contiene los documentos y sus correspondientes índices.
    - matrix (numpy.ndarray): La matriz de valores TF-IDF, donde cada fila representa un documento y cada columna representa una palabra.
    - feature_names (dict): Un diccionario que mapea cada palabra a su índice correspondiente en la matriz.

    Retorna:
    - dict: Un diccionario donde las claves son los índices de los documentos y los valores son las puntuaciones calculadas 
      para cada documento basadas en la consulta.

    Notas:
    - La función asume que la consulta está en DNF y que la matriz de valores TF-IDF y el diccionario de nombres de características 
      están correctamente formateados y alineados.
    - Los documentos se consideran coincidentes si contienen todos los términos de al menos un componente de la consulta.
    """
    literals_total = len(query_list)
    scores = dict()
    returned_docs = []
    
    for doc in _corpus.docs_iter:
        # # print('doc: ', doc)
        doc_index = int(doc[0])
        if query_id in feedback and doc_index in feedback[query_id]:
            print('doc_index : ', doc_index)
            continue 
        else:
       
            _or = 0
            _or_count = 0
            for clause in query_dnf.args:
                _or_count += 1
                if not isinstance(clause, sympy.logic.boolalg.And) and not isinstance(clause,sympy.logic.boolalg.Not):
                    term = clause.as_independent(*clause.free_symbols)[1]
                    try:
                        term_index = feature_names[str(term)]
                    except:
                        continue
                    tfxidf_term = get_tfidf_value(doc_index, term_index, matrix)
                    _or += math.pow(tfxidf_term, literals_total)
                else:
                    _and = 0
                    _and_count = 0
                    for literal in clause.args:  
                        _and_count += 1
                        if(not isinstance(clause,sympy.logic.boolalg.Not)): 
                            term = literal.as_independent(*literal.free_symbols)[1]
                        try:
                            term_index = feature_names[str(term)]
                        except:
                            continue
                        tfxidf_term = get_tfidf_value(doc_index, term_index, matrix)
                        _and += math.pow(1 - tfxidf_term, literals_total) 
                    ## print(f'math.pow {_or} / {_or_count}, 1/{literals_total}')
                    _or += math.pow(1 - math.pow(_and/_and_count, 1/literals_total), literals_total)
            value = math.pow(_or / _or_count, literals_total)
            scores.update({doc_index: value})
            returned_docs.append(doc)
    scores = dict([item for item in sorted(scores.items(), key=lambda item: item[1], reverse=True) if item[1] > 0])
    returned_docs = [item for item in returned_docs if item[0] in scores]
    
    # for i, (doc, val) in enumerate(scores.items()):
    #     # print(f'{doc} , {val}')
    
    # scores = {k: v for k, v in scores.items() if v > 0.}
    return scores, returned_docs



