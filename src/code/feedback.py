import joblib
import os

def update_feedback(id_query, list_docs_vetados):
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
    filename = "feedback.joblib"

    # Verifica si el archivo existe
    if not os.path.exists(filename):
        # Crea un diccionario vacío si el archivo no existe
        feedback = {}
    else:
        # Carga el diccionario si existe
        feedback = joblib.load(filename)
    
    # Verifica si la clave id_query ya existe en el diccionario
    if id_query in feedback:
        # Si existe, actualiza su valor con la lista de documentos vetados
        feedback[id_query].extend(list_docs_vetados)
        feedback[id_query] = list(set(feedback[id_query]))
    else:
        # Si no existe, añade una nueva entrada con la clave id_query y la lista de documentos vetados
        feedback[id_query] = list_docs_vetados
    
    # Guarda el diccionario modificado en el archivo
    joblib.dump(feedback, filename)
    print(f"Archivo {filename} modificado.")
