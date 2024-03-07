import joblib
import os

def update_feedback(id_query, doc_id):
    """
    Actualiza o crea un archivo feedback.joblib con comentarios de documentos vetados.

    Esta función verifica si el archivo feedback.joblib existe. Si no existe, crea un nuevo
    diccionario vacío y lo guarda en el archivo. Si el archivo ya existe, carga el diccionario,
    actualiza o añade la entrada con el id_query proporcionado y la lista de documentos vetados,
    asegurando que no haya duplicados. Finalmente, guarda el diccionario modificado en el archivo.

    Args:
        id_query (int): Identificador de la consulta.
        list_docs_vetados (list): Lista de identificadores de documentos vetados.
    """
    # Nombre del archivo
    filename = "./data/feedback.joblib"
    
    doc_id = int(doc_id)

    # Verifica si el archivo existe
    if not os.path.exists(filename):
        # Crea un diccionario vacío si el archivo no existe
        feedback = dict()
    else:
        # Carga el diccionario si existe
        feedback = joblib.load(filename)
    
    # Verifica si la clave id_query ya existe en el diccionario
    try:
        # Si existe, actualiza su valor con la lista de documentos vetados
        feedback[id_query].append(doc_id)
        feedback[id_query] = list(set(feedback[id_query]))
    except:
        # Si no existe, añade una nueva entrada con la clave id_query y la lista de documentos vetados
        feedback[id_query] = [doc_id]
    
    # Guarda el diccionario modificado en el archivo
    joblib.dump(feedback, filename)
    print(f"Archivo {filename} modificado.")
