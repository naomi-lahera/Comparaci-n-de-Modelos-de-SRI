from ast import mod
from testing_models import get_similar_docs as getDocs
from corpus import Corpus
import csv

class CranfieldData:
    """
    Clase para manejar los datos del corpus Cranfield, incluyendo la obtención de pares de consultas y resultados de relevancia (QRELs).

    Atributos:
    - corpus (Corpus): Un objeto Corpus que contiene los documentos y sus correspondientes índices.
    - docs (list): Lista de documentos en el corpus.
    - query_pairs (list): Lista de pares de consultas, donde cada par contiene el ID de la consulta y el texto de la consulta.
    - qrels (list): Lista de resultados de relevancia (QRELs) para las consultas.

    Métodos:
    - __init__(self): Inicializa la clase cargando los datos necesarios.
    - _get_query_pairs(self): Obtiene los pares de consultas.
    - _get_qrels(self): Obtiene los resultados de relevancia (QRELs) para las consultas.
    - get_query_ids(self): Devuelve un conjunto con los IDs de las consultas.
    """
    def __init__(self):
        _corpus = Corpus("")
        self.corpus = _corpus
        self.docs = self.corpus.docs
        #self.dataset = ir_datasets.load('cranfield')
        self.query_pairs = self._get_query_pairs()
        self.qrels = _corpus.qrels

    def _get_query_pairs(self):
        queries_iter = self.corpus.queries        
        query_pairs = []
        for query in queries_iter:
            query_pairs.append((query.query_id, query.text))
        return query_pairs

    def _get_qrels(self):
        qrels_iter = self.dataset.qrels_iter()
        qrels = []
        for qrel in qrels_iter:
            qrels.append((qrel.query_id, qrel.doc_id, qrel.relevance))
        return qrels
    
    def get_query_ids(self):
        """Returns a set with the IDs of the queries."""
        return set(query_id for query_id, _ in self.query_pairs)

class RelevanceDocumentSetBuilder:
    """
    Clase para construir conjuntos de documentos relevantes e irrelevantes basados en los resultados de relevancia (QRELs).

    Métodos:
    - build_relevance_document_sets(documents, query_id, qrels): Construye los conjuntos de documentos relevantes e irrelevantes para una consulta específica.
    """
    @staticmethod
    def build_relevance_document_sets(documents, query_id, qrels):
        relevant_documents = set()
        irrelevant_documents = set()
        
        # Crear un conjunto de todos los ID de documentos
        document_ids_set = documents
        
        # Extraer los ID de los documentos con relevancia diferente de -1 para la consulta dada
        for qrel in qrels:
            if qrel.query_id == query_id:
                if qrel.relevance != -1:
                    relevant_documents.add(int(qrel.doc_id))

        
        # Calcular los documentos irrelevantes como el conjunto de todos los documentos menos los relevantes
        irrelevant_documents = document_ids_set - relevant_documents
        
        # Devolver los conjuntos de documentos relevantes e irrelevantes
        return relevant_documents, irrelevant_documents

class QueryMetrics:
    """
    Clase para almacenar y recuperar métricas de rendimiento para consultas específicas.

    Atributos:
    - metrics (dict): Diccionario para almacenar las métricas de rendimiento para cada consulta.

    Métodos:
    - __init__(self): Inicializa la clase.
    - add_query_metrics(self, query_id, precision, recall, f_measure, f1_measure, r_precision): Agrega las métricas para una consulta específica.
    - get_query_metrics(self, query_id): Obtiene las métricas para una consulta específica.
    - get_all_metrics(self): Obtiene todas las métricas para todas las consultas.
    """
    def __init__(self):
        self.metrics = {}

    def add_query_metrics(self, query_id, precision, recall, f_measure, f1_measure, r_precision):
        """Agrega las métricas para una query específica."""
        self.metrics[query_id] = {
            'Precision': precision,
            'Recall': recall,
            'F-Measure': f_measure,
            'F1-Measure': f1_measure,
            'R-Precision': r_precision
        }

    def get_query_metrics(self, query_id):
        """Obtiene las métricas para una query específica."""
        return self.metrics.get(query_id, {})

    def get_all_metrics(self):
        """Obtiene todas las métricas para todas las queries."""
        return self.metrics

class MetricsCalculator:
    """
    Clase para calcular métricas de rendimiento como precisión, recall, F-measure, F1-measure y R-Precision para un conjunto de documentos recuperados.

    Atributos:
    - relevant (set): Conjunto de documentos relevantes.
    - irrelevant (set): Conjunto de documentos irrelevantes.
    - retrieved (set): Conjunto de documentos recuperados.

    Métodos:
    - __init__(self, relevant, irrelevant, retrieved): Inicializa la clase con los conjuntos de documentos relevantes, irrelevantes y recuperados.
    - precision(self): Calcula la precisión.
    - recall(self): Calcula el recall.
    - f_measure(self, beta=1): Calcula la medida F.
    - f1_measure(self): Calcula la medida F1.
    - accuracy(self): Calcula la exactitud.
    """
    def __init__(self, relevant, irrelevant, retrieved):
        self.relevant = relevant
        self.irrelevant = irrelevant
        self.retrieved = set(retrieved)

        self.RR = relevant.intersection(retrieved)
        self.RI = irrelevant.intersection(retrieved)
        self.NR = relevant - retrieved
        self.NI= irrelevant - retrieved

        # # print("RR: ", self.RR)
        # # print("RI: ", self.RI)
        # # print("NR: ", self.NR)
        # # print("NI: ", self.NI)
        # raise Exception("Stop")
        
    def precision(self):
        """Calculates the fraction of retrieved information that is relevant."""
        union = self.RR.union(self.RI)
        if len(union) == 0:
            return 0
        return len(self.RR) / len(union)

    def recall(self):
        """Calculates recall."""
        union = self.RR.union(self.NR)
        if len(union) == 0:
            return 0
        return len(self.RR) / len(union)

    def f_measure(self, beta=0):
        """Calculates F-measure."""
        precision = self.precision()
        recall = self.recall()
        if precision + recall == 0:
            return 0
        return (1 + beta**2) * (precision * recall) / ((beta**2 * precision) + recall)

    def f1_measure(self):
        """Calculates F1-measure."""
        return self.f_measure(beta=1)

    def accuracy(self):
        """Calculates Accuracy."""
        total_retrieved = len(self.RR) + len(self.RI)
        total_documents = len(self.relevant) + len(self.irrelevant)
        if total_documents == 0:
            return 0
        return (len(self.RR) + len(self.NI)) / total_documents


def main(model):
    """
    Función principal para cargar los datos de Cranfield, recuperar documentos para cada consulta, calcular métricas de rendimiento y escribir los resultados en un archivo CSV.

    Parámetros:
    - model (str): El modelo de recuperación de documentos a utilizar.

    Notas:
    - La función utiliza la clase CranfieldData para cargar los datos de Cranfield y obtener los pares de consultas y resultados de relevancia (QRELs).
    - La función utiliza la clase RelevanceDocumentSetBuilder para construir conjuntos de documentos relevantes e irrelevantes para cada consulta.
    - La función utiliza la clase MetricsCalculator para calcular métricas de rendimiento para cada consulta.
    - La función escribe las métricas calculadas en un archivo CSV.
    """
    cranfield_data = CranfieldData()
    # Abre un archivo CSV en modo escritura
    with open(f'./data/Metricas_{model}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Escribe el encabezado del archivo CSV
        writer.writerow(['Query ID', 'Precision', 'Recall', 'F-measure', 'F1-measure', 'Accuracy'])

        # Itera sobre cada par de consulta y texto de consulta
        for query_id, query_text in cranfield_data.query_pairs:
            if query_id == '160':
                break
            # Obtén los documentos recuperados para esta consulta
            try:
                retrieved_dict_keys, _ = getDocs(query_id,model)
                retrieved_dict_keys = retrieved_dict_keys.keys()
            except:
                retrieved_dict_keys, _ = getDocs(query_id,model)
            
            retrieved_documents = set(int(key) for key in retrieved_dict_keys)
            
            # Construye los conjuntos de documentos relevantes e irrelevantes a esta consulta
            relevant_documents, irrelevant_documents = RelevanceDocumentSetBuilder.build_relevance_document_sets(retrieved_documents, query_id, cranfield_data.qrels)

            # # print("Relevantes: ", relevant_documents)
            # # print("Irrelevantes: ", irrelevant_documents)

            # Creamos una instancia de MetricsCalculator con los conjuntos relevantes, irrelevantes y recuperados
            metrics_calculator = MetricsCalculator(relevant_documents, irrelevant_documents, retrieved_documents)
            
            # Calcula las métricas para la consulta actual
            precision = metrics_calculator.precision()
            recall = metrics_calculator.recall()
            f_measure = metrics_calculator.f_measure()
            f1_measure = metrics_calculator.f1_measure()
            accuracy = metrics_calculator.accuracy()

            # Escribe las métricas en el archivo CSV
            writer.writerow([query_id, precision, recall, f_measure, f1_measure, accuracy])

if __name__ == "__main__":
    main("boolean")
    main("extended")