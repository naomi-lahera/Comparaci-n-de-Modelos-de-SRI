import nltk

#Descargar WordNet
#nltk.download('omw-1.4')
#nltk.download('wordnet')

nltk.data.path.clear()
nltk.data.path.append('./')
from nltk.corpus import wordnet as wn

def expand_query_with_wordnet(query):
                
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

