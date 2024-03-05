import ir_datasets
from createtfidfjoblib import save_info_to_Joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import prepro
from joblib import load
import cargar

# 'msmarco-document-v2/trec-dl-2022'

class corpus:
    def __init__(self, data_name, docs_num):
        loaded_data = load('data_cranfield.joblib')
        if data_name == "":
            data_name = loaded_data['data_name']
        else:
            cargar.cargar(data_name,docs_num)

        # Cargar los datos desde el archivo

        # Cargar un conjunto de datos específico
        #self.dataset = loaded_data['dataset']
        # Obtener los documentos
        #self.docs_iter = loaded_data['docs_iter']
        # Obtener cada texto por cada documentos
        self.docs = loaded_data['docs']
        self.preprocessed_docs = loaded_data['preprocessed_docs']
        
        # Obtener queries
        self.queries = loaded_data['queries']
        
        # Obtener resultados de cada query
        self.qrels = loaded_data['qrels']
        
    def print_qrels(self):
        # Iterar sobre las relaciones de relevancia (QRELs) para una consulta específica
        for query_id, doc_id, relevance in self.qrels:
            print(f"Query ID: {query_id}, Doc ID: {doc_id}, Relevance: {relevance}")
            