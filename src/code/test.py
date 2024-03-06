import ir_datasets
from extended_boolean import get_similar_docs as getDocs
from process import corpus

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
                    relevant_documents.add(qrel.doc_id)
        
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
        self.retrieved = retrieved
        
        self.RR = relevant.intersection(retrieved)
        self.RI = irrelevant.intersection(retrieved)
        self.NR = relevant - retrieved
        self.NI= irrelevant - retrieved

        # print("RR: ", self.RR)
        # print("RI: ", self.RI)
        # print("NR: ", self.NR)
        # print("NI: ", self.NI)
        
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
    
    for query_id, query_text in cranfield_data.query_pairs:
        # Obtén los documentos recuperados para esta consulta
        retrieved_documents = getDocs(query_text).keys()
        print("PRDoc: ", retrieved_documents)
        # Construye los conjuntos de documentos relevantes e irrelevantes a esta consulta
        relevant_documents, irrelevant_documents = RelevanceDocumentSetBuilder.build_relevance_document_sets(retrieved_documents, query_id, cranfield_data.qrels)

        # Creamos una instancia de MetricsCalculator con los conjuntos relevantes, irrelevantes y recuperados
        metrics_calculator = MetricsCalculator(relevant_documents, irrelevant_documents, retrieved_documents)
        
        # Calculamos y mostramos algunas métricas para la consulta actual
        print(f"Query ID: {query_id}")
        print("Precision:", metrics_calculator.precision())
        print("Recall:", metrics_calculator.recall())
        print("F-measure:", metrics_calculator.f_measure())
        print("F1-measure:", metrics_calculator.f1_measure())
        print("R-Precision:", metrics_calculator.r_precision())

if __name__ == "__main__":
    main()