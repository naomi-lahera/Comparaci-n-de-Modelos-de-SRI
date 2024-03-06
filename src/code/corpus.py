from joblib import load
import cargar

class Corpus:
    """
    Clase para representar un corpus de documentos y consultas, cargando datos preprocesados 
    desde archivos joblib. Permite el acceso a documentos, consultas y resultados de 
    relevancia (QRELs) para su posterior uso en tareas de procesamiento de lenguaje natural 
    y recuperación de información.

    Atributos:
    - docs (list): Lista de documentos en su forma original.
    - preprocessed_docs (list): Lista de documentos preprocesados.
    - queries (list): Lista de consultas.
    - qrels (list): Lista de resultados de relevancia (QRELs) para las consultas.

    Métodos:
    - __init__(self, data_name): Inicializa la clase cargando los datos necesarios.
    - print_qrels(self): Imprime los resultados de relevancia (QRELs) para una consulta específica.
    """
    def __init__(self, data_name):
        """
        Inicializa la clase cargando los datos necesarios desde un archivo joblib o llamando 
        a la función cargar para cargar y preprocesar los datos si no están previamente cargados.

        Parámetros:
        - data_name (str): El nombre del conjunto de datos a cargar. Si se proporciona una cadena 
          vacía, se utilizará el conjunto de datos 'cranfield' por defecto.
        """
        loaded_data = ''
        if data_name == "":
            data_name = 'cranfield'
            loaded_data = load(f'data_{data_name}.joblib')
            data_name = loaded_data['data_name']
            
        else:
            cargar.cargar(data_name)
            loaded_data = load(f'data_{data_name}.joblib')

        # Obtener cada texto por cada documento
        self.docs = loaded_data['docs']
        self.preprocessed_docs = loaded_data['preprocessed_docs']
        
        # Obtener queries
        self.queries = loaded_data['queries']
        
        # Obtener resultados de cada query
        self.qrels = loaded_data['qrels']

    def print_qrels(self):
        """
        Imprime los resultados de relevancia (QRELs) para todas las consultas, mostrando 
        el ID de la consulta, el ID del documento y la relevancia asignada.
        """
        # Iterar sobre las relaciones de relevancia (QRELs) para una consulta específica
        for query_id, doc_id, relevance in self.qrels:
            print(f"Query ID: {query_id}, Doc ID: {doc_id}, Relevance: {relevance}")
