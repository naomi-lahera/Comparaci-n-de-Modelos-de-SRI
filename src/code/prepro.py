import nltk
import spacy

nlp = spacy.load("en_core_web_sm")

#Tokenizamos
def tokenization_spacy(texts):
  return [[token for token in nlp(str(doc))] for doc in texts]

#Eliminamos el ruido
def remove_noise_spacy(tokenized_docs):
  return [[token for token in doc if token.is_alpha or token.text in ['&','|','~','&&','||']] for doc in tokenized_docs]

#Eliminamos las stop_words
def remove_stopwords_spacy(tokenized_docs, query):
  stopwords = spacy.lang.en.stop_words.STOP_WORDS
  if query:
    return [
      [token for token in doc if token.text not in stopwords or (token.text in ['and', 'or', 'not'])] for doc in tokenized_docs
  ] 
  return [
      [token for token in doc if token.text not in stopwords] for doc in tokenized_docs
  ]

#Reducción Morfológica
def morphological_reduction_spacy(tokenized_docs, use_lemmatization=True):
  stemmer = nltk.stem.PorterStemmer()
  return [
    [token.lemma_ if use_lemmatization else stemmer.stem(token.text) for token in doc]
    for doc in tokenized_docs
  ]

def preprocess_documents(documents, is_query): 
    """
    Preprocesa los documentos, incluyendo la tokenización, eliminación de ruido, eliminación de palabras vacías y reducción morfológica.

    Este proceso es fundamental para preparar el texto para el análisis de texto o la recuperación de información.

    Parámetros:
    - documents (list): Una lista de documentos a preprocesar.
    - is_query (bool): Un booleano que indica si los documentos son consultas. Si es verdadero, se procesará como una consulta.

    Retorna:
    - str: Si los documentos son una consulta, retorna la consulta preprocesada como una cadena de texto.
    - list: Si los documentos no son una consulta, retorna una lista de listas de tokens preprocesados.
    """ 
    # Tokenización
    if is_query:
      documents = [documents]
    tokenized_docs = tokenization_spacy(documents)

    # Eliminación de ruido (solo tokens alfabéticos)
    tokenized_docs = remove_noise_spacy(tokenized_docs)
    
    #Eliminamos las stop_words
    tokenized_docs = remove_stopwords_spacy(tokenized_docs, is_query)
    if is_query:
      lista = [token.text for token in tokenized_docs[0]]
      strin = " ".join(lista)
      return strin
    
    #Reducción Morfológica
    tokenized_docs = morphological_reduction_spacy(tokenized_docs)
    
    return tokenized_docs