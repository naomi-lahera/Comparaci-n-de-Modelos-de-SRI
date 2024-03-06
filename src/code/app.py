import os

from testing_models import get_similar_docs, _corpus
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/search', methods=['GET'])
def get_docs():
    query_id = request.args.get('query_id')
    query = _corpus.queries[int(query_id)][1]
    docs = get_similar_docs(query, 'extended')
    print(docs)
    if query_id:
        return jsonify(
            [
                {
                    'id': _corpus.docs[doc.key][0], 
                    'title': _corpus.docs[doc.key][1], 
                    'text': _corpus.docs[doc.key][2]
                } 
                for doc in docs
            ])
        
    return jsonify({'error': 'Missing query parameter'}), 400

@app.route('/api/get_queries', methods=['GET'])
def get_sources():
    return jsonify([{'id': query.query_id, 'text': query.text} for query in _corpus.queries])

@app.route('/api/delete-doc', methods=['DELETE'])
def delete_doc_query():
    query_id = request.get('query_id')
    doc_id = request.get('doc_id')
    return jsonify({'msg': 'Done'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)