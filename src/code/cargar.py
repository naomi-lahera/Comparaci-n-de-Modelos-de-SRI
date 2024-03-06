import ir_datasets
from createtfidfjoblib import save_info_to_Joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import prepro
from joblib import dump

def cargar(data):
    data_name = data
    # Cargar un conjunto de datos específico
    dataset = ir_datasets.load(data_name)
    # Obtener los documentos
    docs_iter =  dataset.docs_iter()
    # Obtener cada texto por cada documentos
    docs = [doc.text for doc in docs_iter]
    # Procesar los documentos
    preprocessed_docs = prepro.preprocess_documents(docs,False)
    # Convertir cada lista de tokens en una cadena única
    preprocessed_docs = [' '.join(doc) for doc in preprocessed_docs]

     # Obtener queries
    queries = dataset.queries_iter()

    # Obtener resultados de cada query
    qrels = dataset.qrels_iter()

    data_to_save = {
        'preprocessed_docs': preprocessed_docs,
        'queries': list(queries),
        'qrels': list(qrels),
        'docs' : docs,
        'data_name' : data_name
    }

    dump(data_to_save, f'data_{data}.joblib')
    # Crea un jblin con los valores de tfxidf con la coleccion de documentos y se puede modificar la cantidad de documentos a escoger 
    save_info_to_Joblib(docs, data_name)
    # Guardar los datos en un archivo
