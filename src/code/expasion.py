import nltk
from nltk.corpus import wordnet as wn

def expand_query_with_wordnet(query):
    """
    Expande una consulta utilizando sinónimos encontrados en WordNet, una base de datos léxica de 
    inglés que contiene relaciones semánticas entre palabras. Si la consulta tiene 5 o más palabras, 
    se retorna la consulta original sin cambios. De lo contrario, se buscan sinónimos para cada palabra 
    en la consulta y se expande la consulta incluyendo estos sinónimos.

    Parámetros:
    - query (str): La consulta a expandir.

    Retorna:
    - str: La consulta original o una versión expandida con sinónimos encontrados en WordNet.

    Notas:
    - La función utiliza la biblioteca NLTK y su corpus WordNet para buscar sinónimos.
    - Si no se encuentran sinónimos para una palabra, la palabra original se incluye en la consulta 
      expandida.
    - La consulta expandida incluye una disyunción (OR) entre la palabra original y sus sinónimos, 
      excepto la palabra original que se excluye de la disyunción.
    """
    words = query.split()
    if len(words) >= 5:
        return query
    synonyms = {}
    for word in words:
        try:
            word_synset = wn.synsets(word)[0]
            similar_synsets = [synset for synset in wn.synsets(word) if synset != word_synset]
            sorted_synsets = sorted(similar_synsets, key=lambda x: word_synset.wup_similarity(x), reverse=True)
            top_synsets = sorted_synsets[:2] if sorted_synsets else []
            synonyms[word] = [lemma.name() for synset in top_synsets for lemma in synset.lemmas()[:2]]
        except IndexError:
            continue
    
    # Combine the original words with their synonyms, excluding the original words
    expanded_query_parts = []
    for word in words:
        if word in synonyms:
            synonym_list = [synonym for synonym in synonyms[word] if synonym not in words]
            if synonym_list:
                expanded_query_parts.append(f"( {word} | {' | '.join(synonym_list)} )")
            else:
                expanded_query_parts.append(word)
        else:
            expanded_query_parts.append(word)
    
    expanded_query = " ".join(expanded_query_parts)
    return expanded_query
