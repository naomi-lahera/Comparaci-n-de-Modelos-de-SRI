import ir_datasets
from extended_boolean import get_similar_docs as getDocs
from process import corpus
import csv

class CranfieldData:
    def __init__(self):
        _corpus = corpus("",100)
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

    def __init__(self, relevant, irrelevant, retrieved):
        self.relevant = relevant
        self.irrelevant = irrelevant
        self.retrieved = set(retrieved)

        self.RR = relevant.intersection(retrieved)
        self.RI = irrelevant.intersection(retrieved)
        self.NR = relevant - retrieved
        self.NI= irrelevant - retrieved

        # print("RR: ", self.RR)
        # print("RI: ", self.RI)
        # print("NR: ", self.NR)
        # print("NI: ", self.NI)
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

    def f_measure(self, beta=1):
        """Calculates F-measure."""
        precision = self.precision()
        recall = self.recall()
        if precision + recall == 0:
            return 0
        return (1 + beta**2) * (precision * recall) / ((beta**2 * precision) + recall)

    def f1_measure(self):
        """Calculates F1-measure."""
        return self.f_measure(beta=1)

    def r_precision(self):
        """Calculates R-Precision."""
        union = self.RR.union(self.RI)
        if len(union) == 0:
            return 0
        return len(self.RR) / len(union)


def main():
    cranfield_data = CranfieldData()
    
    # Abre un archivo CSV en modo escritura
    with open('MetricasExtended.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Escribe el encabezado del archivo CSV
        writer.writerow(['Query ID', 'Precision', 'Recall', 'F-measure', 'F1-measure', 'R-Precision'])

        # Itera sobre cada par de consulta y texto de consulta
        for query_id, query_text in cranfield_data.query_pairs:
            # Obtén los documentos recuperados para esta consulta
            retrieved_dict_keys = getDocs(query_text).keys()
            retrieved_documents = set(int(key) for key in retrieved_dict_keys)
            
            # Construye los conjuntos de documentos relevantes e irrelevantes a esta consulta
            relevant_documents, irrelevant_documents = RelevanceDocumentSetBuilder.build_relevance_document_sets(retrieved_documents, query_id, cranfield_data.qrels)

            # print("Relevantes: ", relevant_documents)
            # print("Irrelevantes: ", irrelevant_documents)

            # Creamos una instancia de MetricsCalculator con los conjuntos relevantes, irrelevantes y recuperados
            metrics_calculator = MetricsCalculator(relevant_documents, irrelevant_documents, retrieved_documents)
            
            # Calcula las métricas para la consulta actual
            precision = metrics_calculator.precision()
            recall = metrics_calculator.recall()
            f_measure = metrics_calculator.f_measure()
            f1_measure = metrics_calculator.f1_measure()
            r_precision = metrics_calculator.r_precision()

            # Escribe las métricas en el archivo CSV
            writer.writerow([query_id, precision, recall, f_measure, f1_measure, r_precision])

if __name__ == "__main__":
    main()