from query_preppro import query_to_dnf
import joblib
from corpus import corpus
from extended import boolean_extended
from boolean import boolean
from sympy import Not
first = True
_corpus = corpus("")
matrix = ''
vectorizer = ''
feature_names = dict()

     
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
        
def get_similar_docs(query,method):
    query_dnf = query_to_dnf(query)

    query_literals = get_literals_from_dnf(query_dnf)

    init()
    if method == "boolean":
        scores = boolean(query_dnf,_corpus.preprocessed_docs)
    else:
        scores = boolean_extended(query_literals, query_dnf,_corpus)
    return scores

def get_literals_from_dnf(dnf):
    literals = []
    for disjunct in dnf.args:
        if isinstance(disjunct, Not):
            literals.append(f"~{str(disjunct.args[0])}")  # Include the negation symbol (~)
        else:
            for literal in disjunct.args:
                # Access the literal directly without using 'as_independent'
                literals.append(str(literal))
    return list(set(literals))
    