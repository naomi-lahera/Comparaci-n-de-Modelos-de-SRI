from testing_models import get_similar_docs, _corpus
from testing_models import update_feedback_testing_models
from comparison import obtain_column
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/search', methods=['GET'])
def get_docs():
    query_id = request.args.get('query_id')
    docs_dict, returned_docs = get_similar_docs(int(query_id), 'extended')
    # print(docs_dict)
    # print('docs_dict: ', len(docs_dict))
    # print('docs_dict: ', len(returned_docs))
    if query_id:
        return jsonify(
            [
                {
                    'id': int(doc[0]),
                    'title': doc[1][0].upper() + doc[1][1:],
                    'text': doc[2]
                }
                for doc in returned_docs
            ])
        
    return jsonify({'error': 'Missing query parameter'}), 400

@app.route('/api/get_queries', methods=['GET'])
def get_sources():
    return jsonify([{'id': query.query_id, 'text': query.text[0].upper() + query.text[1:]} for query in _corpus.queries])

@app.route('/api/delete-doc', methods=['GET'])
def delete_doc_query():
    query_id = request.args.get('query_id')
    doc_id = request.args.get('doc_id')
    update_feedback_testing_models(int(query_id), int(doc_id))
    # print('update feedback')
    docs_dict, returned_docs = get_similar_docs(int(query_id), 'extended')
    # print(docs_dict)
    # print(docs_dict)
    if query_id and doc_id:
        return jsonify(
            [
                {
                    'id': int(doc[0]),
                    'title': doc[1][0].upper() + doc[1][1:],
                    'text': doc[2]
                }
                for doc in returned_docs
            ])
    return jsonify({'mdg': 'Error'})

@app.route('/api/get-metric', methods=['GET'])
def get_metric():
    metric = request.args.get('metric')
    if metric:
        print('metric: ', metric)
        return jsonify({'queries_id': [item[0][0] for item in obtain_column(metric)][:50], 'boolean': [float(item[0][1]) for item in obtain_column(metric)][:50], 'extended': [float(item[1][1]) for item in obtain_column(metric)][:50]})
    return jsonify({'msg':'error'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)