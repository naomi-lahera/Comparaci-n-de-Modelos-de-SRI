import nltk

#Descargar WordNet
#nltk.download('omw-1.4')
#nltk.download('wordnet')

# Importar WordNet correctamente
from nltk.corpus import wordnet as wn

def expand_query_with_wordnet(query):
    # Convertir la consulta en palabras
    words = query.split()
    # Inicializar un conjunto para almacenar los sinónimos
    synonyms = set()
    for word in words:
        # Buscar sinónimos para cada palabra
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
    # Convertir el conjunto de sinónimos en una cadena
    expanded_query = " ".join(synonyms)
    return expanded_query

query = "run"
expanded_query = expand_query_with_wordnet(query)
print(expanded_query)
