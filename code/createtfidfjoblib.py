import time
import glob
import pandas as pd
import prepro
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib


# Specify the path to the directory containing the CSV files
csv_directory = './'

# Use glob to find all CSV files in the specified directory
csv_files = glob.glob(csv_directory + '*.csv')


def save_info_to_Joblib(csvpath,cantDocs):

    # Leer el archivo CSV en un DataFrame de pandas
    df = pd.read_csv(csvpath, sep=',', engine='python')


    # Aquí cargamos los documentos
    documents = [str(doc['title']) + " " + str(doc['description']) for _, doc in df.iterrows()]
    documents = documents[:cantDocs]

    # Preprocesamiento de los documentos
    preprocessed_docs = prepro.preprocess_documents(documents)

    # Convertir cada lista de tokens en una cadena única
    preprocessed_docs = [' '.join(doc) for doc in preprocessed_docs]

    # Crear el vectorizador y calcular la matriz TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_docs)
    
    base_filename = csvpath.rsplit('.',  1)[0]
    joblib.dump(tfidf_vectorizer, f'{base_filename}_vect.joblib')
    joblib.dump(tfidf_matrix, f'{base_filename}_matrix.joblib')
    
    return tfidf_vectorizer

for csv_file in csv_files:
    print(f'Processing {csv_file}...')
    start_time = time.time()
    
    # Read the CSV file into a DataFrame and get the number of rows
    df = pd.read_csv(csv_file)
    filas_csv = len(df)
    
    save_info_to_Joblib(csv_file, filas_csv)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Processing {csv_file} took {execution_time} seconds to execute.")

print('All CSV files processed.')

if __name__ == '__main__':
    pass
