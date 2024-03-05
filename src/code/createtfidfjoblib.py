import time
import glob
import pandas as pd
import prepro
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def save_info_to_Joblib(docs, corpus_name):
    # documents = docs[:docs_num]
    documents = list(docs)

    # Preprocesamiento de los documentos
    preprocessed_docs = prepro.preprocess_documents(documents,False)

    # Convertir cada lista de tokens en una cadena única
    preprocessed_docs = [' '.join(doc) for doc in preprocessed_docs]

    # Crear el vectorizador y calcular la matriz TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_docs)
    
    joblib.dump(tfidf_vectorizer, f'{corpus_name}_vect.joblib')
    joblib.dump(tfidf_matrix, f'{corpus_name}_matrix.joblib')
    
    return tfidf_vectorizer
