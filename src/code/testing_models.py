from query_preppro import query_to_dnf
import joblib
from corpus import Corpus
from extended import boolean_extended
from boolean import boolean
from sympy import Not
import os
first = True
_corpus = Corpus("")
matrix = ''
vectorizer = ''
feature_names = dict()
filename = "feedback.joblib"
# Verifica si el archivo existe
if not os.path.exists(filename):
    # Crea un diccionario vacío si el archivo no existe
    feedback = {}
else:
    # Carga el diccionario si existe
    feedback = joblib.load(filename)
     
def init():
    """
    Inicializa las variables globales necesarias para el procesamiento de consultas, incluyendo la carga de la matriz de valores TF-IDF y el vectorizador.

    Esta función se ejecuta solo una vez para evitar la sobrecarga de cargar los datos de la matriz y el vectorizador en cada llamada.

    Notas:
    - Carga la matriz de valores TF-IDF y el vectorizador desde archivos joblib.
    - Genera un diccionario de nombres de características a partir de los nombres de características proporcionados por el vectorizador.
    """
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
        
def get_similar_docs(query_id,method):
    """
    Obtiene documentos similares a una consulta dada utilizando un método específico de recuperación de información.

    Parámetros:
    - query (str): La consulta para la cual se buscan documentos similares.
    - method (str): El método de recuperación de información a utilizar ('boolean' o 'extended').

    Retorna:
    - dict: Un diccionario donde las claves son los índices de los documentos y los valores son las puntuaciones calculadas 
      para cada documento basadas en la consulta.

    Notas:
    - La función utiliza el método `query_to_dnf` para convertir la consulta en su forma Disjunctive Normal Form (DNF).
    - Dependiendo del método especificado, utiliza el modelo booleano o una versión extendida del modelo booleano para calcular las puntuaciones.
    """
    query =_corpus.queries[int(query_id)][1]
    query_dnf = query_to_dnf(query)

    query_literals = get_literals_from_dnf(query_dnf)

    init()
    if method == "boolean":
        scores = boolean(query_dnf,_corpus.preprocessed_docs)
    else:
        query_id = _corpus.docs_iter
        scores = boolean_extended(query_id,query_literals, query_dnf,_corpus,matrix,feature_names,feedback)
    return scores

def get_literals_from_dnf(dnf):
    """
    Extrae los literales de una expresión booleana en DNF (Disjunctive Normal Form).

    Parámetros:
    - dnf (sympy.logic.boolalg.And): Una expresión booleana en DNF.

    Retorna:
    - list: Una lista de literales extraídos de la expresión DNF.

    Notas:
    - Los literales pueden ser palabras o frases de la consulta, representadas como cadenas de texto.
    - Si un literal es una negación, se incluye el símbolo de negación (~) antes de la palabra o frase.
    """
    literals = []
    for disjunct in dnf.args:
        if isinstance(disjunct, Not):
            literals.append(f"~{str(disjunct.args[0])}")  # Include the negation symbol (~)
        else:
            for literal in disjunct.args:
                # Access the literal directly without using 'as_independent'
                literals.append(str(literal))
    return list(set(literals))
    