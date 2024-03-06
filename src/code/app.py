import os
from extended_boolean import _corpus, docs_from_query_id

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__, template_folder='./templates')
CORS(app)

@app.route('/api/search', methods=['GET'])
def get_docs():
    query_id = request.args.get('query_id')
    docs = docs_from_query_id(int(query_id))
    if query_id:
        return jsonify([doc.serialize() for doc in docs])
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