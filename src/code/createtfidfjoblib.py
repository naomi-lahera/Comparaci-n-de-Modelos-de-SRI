import prepro
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def save_info_to_Joblib(docs, corpus_name):
    """
    Preprocesa un conjunto de documentos, calcula su matriz TF-IDF y guarda tanto el 
    vectorizador como la matriz en archivos joblib para su uso posterior.

    Esta función realiza el preprocesamiento de los documentos, que incluye la tokenización, 
    la eliminación de palabras vacías y posiblemente otras operaciones definidas en la función 
    prepro.preprocess_documents. Luego, utiliza TfidfVectorizer de scikit-learn para 
    calcular la matriz TF-IDF de los documentos preprocesados. Finalmente, guarda tanto el 
    vectorizador como la matriz en archivos joblib para su uso posterior.

    Parámetros:
    - docs (list): Una lista de documentos en formato de texto.
    - corpus_name (str): El nombre del corpus que se utilizará para nombrar los archivos 
      joblib donde se guardarán el vectorizador y la matriz TF-IDF.

    Retorna:
    - TfidfVectorizer: El vectorizador TF-IDF utilizado para calcular la matriz TF-IDF.

    Nota:
    - La función asume que la función prepro.preprocess_documents realiza un preprocesamiento 
      adecuado de los documentos, incluyendo la tokenización y la eliminación de palabras vacías.
    - Los archivos joblib se guardan con nombres basados en el parámetro corpus_name, 
      seguidos de '_vect.joblib' para el vectorizador y '_matrix.joblib' para la matriz.
    """
    # Preprocesamiento de los documentos
    documents = list(docs)
    preprocessed_docs = prepro.preprocess_documents(documents, False)

    # Convertir cada lista de tokens en una cadena única
    preprocessed_docs = [' '.join(doc) for doc in preprocessed_docs]

    # Crear el vectorizador y calcular la matriz TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_docs)
    
    # Guardar el vectorizador y la matriz en archivos joblib
    joblib.dump(tfidf_vectorizer, f'./data/{corpus_name}_vect.joblib')
    joblib.dump(tfidf_matrix, f'./data/{corpus_name}_matrix.joblib')
    
    return tfidf_vectorizer
