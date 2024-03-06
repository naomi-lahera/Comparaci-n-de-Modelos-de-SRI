import nltk
import spacy
import gensim

nlp = spacy.load("en_core_web_sm")

#Tokenizamos
def tokenization_spacy(texts):
  return [[token for token in nlp(str(doc))] for doc in texts]

#Eliminamos el ruido
def remove_noise_spacy(tokenized_docs):
  return [[token for token in doc if token.is_alpha] for doc in tokenized_docs]

#Eliminamos las stop_words
def remove_stopwords_spacy(tokenized_docs, query):
  stopwords = spacy.lang.en.stop_words.STOP_WORDS
  return [
      [token for token in doc if token.text not in stopwords or (token.text in ['and', 'or', 'not'])] for doc in tokenized_docs
  ]

#Reducción Morfológica
def morphological_reduction_spacy(tokenized_docs, use_lemmatization=True):
  stemmer = nltk.stem.PorterStemmer()
  return [
    [token.lemma_ if use_lemmatization else stemmer.stem(token.text) for token in doc]
    for doc in tokenized_docs
  ]

def preprocess_documents(documents, is_query):  
    # Tokenización
    tokenized_docs = tokenization_spacy(documents)

    # Eliminación de ruido (solo tokens alfabéticos)
    tokenized_docs = remove_noise_spacy(tokenized_docs)
    
    #Eliminamos las stop_words
    tokenized_docs = remove_stopwords_spacy(tokenized_docs, is_query)
    
    #Reducción Morfológica
    tokenized_docs = morphological_reduction_spacy(tokenized_docs)

    return tokenized_docs