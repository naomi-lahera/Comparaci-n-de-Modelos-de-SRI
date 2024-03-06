from joblib import load
import cargar

class corpus:
    def __init__(self, data_name):
        loaded_data = ''
        if data_name == "":
            data_name = 'cranfield'
            loaded_data = load(f'data_{data_name}.joblib')
            data_name = loaded_data['data_name']
            
        else:
            cargar.cargar(data_name)
            loaded_data = load(f'data_{data_name}.joblib')

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
            