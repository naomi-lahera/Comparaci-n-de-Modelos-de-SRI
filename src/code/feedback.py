import joblib
import os

def update_feedback(id_query, list_docs_vetados):
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

# Llamadas a la función
update_feedback(3, [1, 2, 4])
update_feedback(2, [1, 2, 4])
update_feedback(2, [3])

feedback = joblib.load("feedback.joblib")
print(feedback[2])
print(feedback[3])
    
