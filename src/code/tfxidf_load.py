import pandas
import prepro
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib


def load_mat(name):
    tfidf_matrix = joblib.load(name)
    return tfidf_matrix

def load_vec(name):
    vectorizer = joblib.load(name)
    return vectorizer

def save_info_to_Joblib(csvpath, cantDocs):
    # Leer el archivo CSV en un DataFrame de pandas
    df = pandas.read_csv(csvpath)

    # Aquí cargamos los documentos
    documents = [doc['title'] + " " + doc['description'] for _, doc in df.iterrows()]
    documents = documents[:cantDocs]

    # Preprocesamiento de los documentos
    preprocessed_docs = prepro.preprocess_documents(documents)

    # Convertir cada lista de tokens en una cadena única
    preprocessed_docs = [' '.join(doc) for doc in preprocessed_docs]

    # Crear el vectorizador y calcular la matriz TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_docs)

    joblib.dump(tfidf_vectorizer, 'vectorizer.joblib')
    joblib.dump(tfidf_matrix, 'matrix.joblib')
    
    return tfidf_vectorizer


