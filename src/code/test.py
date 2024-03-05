import ir_datasets
from extended_boolean import get_similar_docs as getDocs

class CranfieldData:
    def __init__(self):
        self.dataset = ir_datasets.load('cranfield')
        self.query_pairs = self._get_query_pairs()
        self.qrels = self._get_qrels()
    
    def _get_query_pairs(self):
        queries_iter = self.dataset.queries_iter()        
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

    @staticmethod
    def precision(relevant_retrieved, irrelevant_retrieved):
        """Calculates the fraction of retrieved information that is relevant."""
        union = relevant_retrieved.union(irrelevant_retrieved)
        if len(union) == 0:
            return 0
        return len(relevant_retrieved) / len(union)

    @staticmethod
    def recall(relevant_retrieved, relevant_not_retrieved):
        """Calculates recall."""
        union = relevant_retrieved.union(relevant_not_retrieved)
        if len(union) == 0:
            return 0
        return len(relevant_retrieved) / len(union)

    @staticmethod
    def f_measure(relevant_retrieved, irrelevant_retrieved, relevant_not_retrieved, beta=1):
        """Calculates F-measure."""
        precision = MetricsCalculator.precision(relevant_retrieved, irrelevant_retrieved)
        recall = MetricsCalculator.recall(relevant_retrieved, relevant_not_retrieved)
        if precision + recall == 0:
            return 0
        return (1 + beta**2) * (precision * recall) / ((beta**2 * precision) + recall)

    @staticmethod
    def f1_measure(relevant_retrieved, irrelevant_retrieved, relevant_not_retrieved):
        """Calculates F1-measure."""
        return MetricsCalculator.f_measure(relevant_retrieved, irrelevant_retrieved, relevant_not_retrieved, beta=1)

    @staticmethod
    def r_precision(relevant_retrieved, irrelevant_retrieved):
        """Calculates R-Precision."""
        union = relevant_retrieved.union(irrelevant_retrieved)
        if len(union) == 0:
            return 0
        return len(relevant_retrieved) / len(union)

        
def main():
    cranfield_data = CranfieldData()
    
    docs = getDocs('bind or number and value')
    
    for i, (doc, val) in enumerate(docs.items()):
        print(f'{doc} , {val}')
    # Acceso a las variables públicas de la clase
    # print("Query pairs:")
    # for query_id, query_text in cranfield_data.query_pairs:
    #     print(f"Query ID: {query_id}, Query Text: {query_text}")
    
    # print("\nQrels:")
    # for query_id, doc_id, relevance in cranfield_data.qrels:
    #     print(f"Query ID: {query_id}, Document ID: {doc_id}, Relevance: {relevance}")

if __name__ == "__main__":
    main()