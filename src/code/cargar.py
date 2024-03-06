import ir_datasets
from createtfidfjoblib import save_info_to_Joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import prepro
from joblib import dump

def cargar(data):
    """
    Carga y preprocesa un conjunto de datos de IR específico, luego guarda la información relevante 
    en archivos para su posterior uso, incluyendo los documentos preprocesados, consultas, resultados de 
    relevancia y el nombre del conjunto de datos.

    Esta función utiliza el paquete ir_datasets para cargar el conjunto de datos, y realiza un preprocesamiento 
    básico en los documentos y consultas utilizando funciones personalizadas. Posteriormente, guarda toda la 
    información relevante en un archivo joblib para su uso posterior.

    Parámetros:
    - data (str): El nombre del conjunto de datos a cargar. Este nombre debe ser reconocido por el paquete 
      ir_datasets para cargar el conjunto de datos correcto.

    Nota:
    - La función asume que el preprocesamiento de los documentos se realiza con la función 
      prepro.preprocess_documents, que acepta una lista de documentos y un booleano que indica si se 
      deben incluir o no los tokens nulos.
    - Los resultados de la relevancia (qrels) y las consultas se guardan tal como se obtienen del conjunto de 
      datos, sin ningún preprocesamiento adicional.
    - La función también utiliza save_info_to_Joblib para guardar información adicional, como los valores 
      de tf-idf, pero esta parte del código no se incluye en el docstring debido a su naturaleza específica 
      de la función.

    Retorna:
    - No retorna nada directamente, pero guarda la información relevante en un archivo joblib.
    """
    data_name = data
    # Cargar un conjunto de datos específico
    dataset = ir_datasets.load(data_name)
    # Obtener los documentos
    docs_iter = dataset.docs_iter()
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
