import pandas
import prepro
from class_News import News
from sklearn.metrics.pairwise import cosine_similarity
from tfxidf_load import load_mat, load_vec
from HTMLProcessor import query_html_processor
import os
from datetime import date

first = True
directorio_actual = os.path.dirname(os.path.abspath(__file__))
file_url= directorio_actual+'/files_charged/csv/'
csv_files = [f for f in os.listdir(file_url) if f.endswith('.csv')]
matrix = ""
matrix_url = ""
vectorizer = ""

def query_result(query,loaded_matrix,csvpath,vectorizador,cantDocs_to_return= 0,presition = 0.05):

    df = pandas.read_csv(csvpath)
    # Tokenización y preprocesamiento de la consulta
    query_tokens = prepro.preprocess_documents([query])[0]
    qvector = vectorizador.transform(query_tokens)

    # Calcular las similitudes del coseno entre la consulta y los documentos
    similarity_scores = cosine_similarity(qvector,loaded_matrix)[0]

    similarity_scores = {i: score for i, score in enumerate(similarity_scores)}
    diccionario_ordenado = dict(sorted(similarity_scores.items(), key=lambda item: item[1],reverse = True))
    diccionario_ordenado = {k: v for k, v in diccionario_ordenado.items() if v >  presition}
    
    if cantDocs_to_return > 0:
        # Convertir el diccionario ordenado en una lista de tuplas para poder indexarlo
        lista_ordenada = list(diccionario_ordenado.items())
        # Obtener los primeros 'cantDocs_to_return' elementos de la lista
        diccionario_ordenado = dict(lista_ordenada[:cantDocs_to_return])

    documents = []
    for score in diccionario_ordenado:
        index = score
        print(f"indice: {index}")
        title = df.loc[index, 'title']
        try:
            author = df.loc[index, 'author']
        except:
            author = 'Unknown'
        try:
            date = df.loc[index, 'date']
        except:
            date = 'Unknown'
        summary = df.loc[index, 'description']
        url = df.loc[index, 'link']

        news_item = News(title, author, date, summary, url)
        documents.append(news_item)
    return documents


def sri(save_name,url,cant_docs_return = 10):
    global first
    global file_url
    global csv_files
    global matrix
    global matrix_url
    global vectorizer
    try:
        # selected_file = csv_files[int(save_name)]
        selected_file = save_name
        url_csv = f"./files_charged/csv/{selected_file[:-4]}"
    except:
        url_csv = f"./files_charged/csv/all_news"


    mat_url = f'./files_charged/matrix/{selected_file[:-4]}_matrix.joblib'
    print('selected_file: ', selected_file)
    print('mat_url: ', mat_url)
    
    vec_url = f'./files_charged/vect/{selected_file[:-4]}_vect.joblib'
    process = query_html_processor(url)
    struc_new = process[0]
    query = process[1]

    if first or matrix_url != mat_url:
        matrix = load_mat(mat_url)
        matrix_url = mat_url
        vectorizer = load_vec(vec_url)        
        first = False

    scores = query_result(query, matrix, f'{url_csv}.csv', vectorizer, cant_docs_return)

    return [struc_new, scores]