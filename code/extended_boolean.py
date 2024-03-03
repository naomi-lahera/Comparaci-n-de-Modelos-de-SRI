import math
from query_preppro import query_to_dnf
from tfxidf_load import load_mat, load_vec
from ...SRI.data.process import corpus
import prepro
import pandas
import sympy

first = True
_corpus = corpus('cranfield', 10)

def sim(query_list, query_dnf, qvector, matrix):
    literals_total = len(query_list)
    feature_names = matrix.get_feature_names()
    extended_matrix = matrix.fit_transform(_corpus.preprocess_docs)
    scores = dict()
    for doc in _corpus.docs:
        inside = 0
        for clause in query_dnf.args:
            if not isinstance(clause, sympy.logic.boolalg.And):
                # Obtener el termino
                term = clause.as_independent(*clause.free_symbols)[1]
                # Obtener el indice del termino en la matriz
                term_index = feature_names.index(term)
                
                # Ver el valor de la matriz en la posicion doc, term
                tfxidf_term = extended_matrix[doc.index, term_index]
                
                # Annadir el valor de ese termino en dependencia de si es un not o no
                inside += (1 - math.pow(tfxidf_term, literals_total)) if not isinstance(clause, sympy.logic.boolalg.Not) else - (1 - math.pow(tfxidf_term, literals_total))
        
        scores.update(doc.index)
                    
        
def get_tfxidf(query):
    global first
    
    url_csv = f"./files_charged/csv/all_news"
    selected_file = 'all_news'
    mat_url = f'./files_charged/matrix/{selected_file[:-4]}_matrix.joblib'
    vec_url = f'./files_charged/vect/{selected_file[:-4]}_vect.joblib'
    
    if first or matrix_url != mat_url:
        matrix = load_mat(mat_url)
        matrix_url = mat_url
        vectorizer = load_vec(vec_url)        
        first = False
        
    df = pandas.read_csv(f'{url_csv}.csv')
    # Tokenización y preprocesamiento de la consulta
    query_tokens = prepro.preprocess_documents([query])[0]
    qvector = vectorizer.transform(query_tokens)
    
    return qvector, matrix
    
def get_similar_docs(query):
    query_dnf = query_to_dnf(query)
    print(query_dnf)
    
    query = get_literals_from_dnf(query_dnf)
    print(query)
    
    qvector, matrix = get_tfxidf(query)
    print(qvector)
    
    sim(query, query_dnf, qvector, matrix)
    
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
    
    
# test_query = 'A or c and b'
# get_similar_docs(test_query)
# # sim('A or c and b')