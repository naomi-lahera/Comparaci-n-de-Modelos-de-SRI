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

def main():
    cranfield_data = CranfieldData()
    
    docs = getDocs('house or number and value')
    # Acceso a las variables públicas de la clase
    print("Query pairs:")
    for query_id, query_text in cranfield_data.query_pairs:
        print(f"Query ID: {query_id}, Query Text: {query_text}")
    
    # print("\nQrels:")
    # for query_id, doc_id, relevance in cranfield_data.qrels:
    #     print(f"Query ID: {query_id}, Document ID: {doc_id}, Relevance: {relevance}")

if __name__ == "__main__":
    main()