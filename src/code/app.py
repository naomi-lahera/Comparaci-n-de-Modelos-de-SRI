from testing_models import get_similar_docs, _corpus
from feedback import update_feedback
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/search', methods=['GET'])
def get_docs():
    query_id = request.args.get('query_id')
    docs_dict = get_similar_docs(int(query_id), 'extended')
    # print(docs_dict)
    if query_id:
        return jsonify(
            [
                {
                    'id': _corpus.docs_iter[doc_id][0],
                    'title': _corpus.docs_iter[doc_id][1],
                    'text': _corpus.docs_iter[doc_id][2]
                }
                for doc_id, score in docs_dict.items()
            ])
        
    return jsonify({'error': 'Missing query parameter'}), 400

@app.route('/api/get_queries', methods=['GET'])
def get_sources():
    return jsonify([{'id': query.query_id, 'text': query.text} for query in _corpus.queries])

@app.route('/api/delete-doc', methods=['DELETE'])
def delete_doc_query():
    query_id = request.get('query_id')
    doc_id = request.get('doc_id')
    update_feedback(int(query_id), doc_id)
    print('update feedback')
    return jsonify({'msg': 'Done'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)