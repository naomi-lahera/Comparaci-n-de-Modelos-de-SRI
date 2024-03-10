def boolean(query_dnf, tokenized_docs):
    """
    Filtra y devuelve los índices de los documentos que coinciden con la consulta dada, 
    basándose en la representación en Disjunctive Normal Form (DNF) de la consulta.

    Esta función compara la consulta (representada en DNF) con un conjunto de documentos 
    tokenizados, para determinar qué documentos contienen todos los términos de la consulta.

    Parámetros:
    - query_dnf (sympy.And): La consulta en Disjunctive Normal Form (DNF). Cada componente 
      de la consulta debe ser una conjunción de términos.
    - tokenized_docs (list): Una lista de conjuntos de términos, donde cada conjunto 
      representa los términos de un documento tokenizado.

    Retorna:
    - list: Una lista de índices de documentos que coinciden con la consulta.

    Nota:
    - La función asume que cada componente de la consulta DNF es una conjunción de términos.
    - Los documentos se consideran coincidentes si contienen todos los términos de al menos un 
      componente de la consulta.
    """
    # Convert tokenized_docs to a list of sets for efficient operations
    doc_term_sets = tokenized_docs

    matching_documents = []
    for doc_i, doc_terms in enumerate(doc_term_sets):
        # Initialize a flag to check if the document matches the query
        all_match = False
        for q_ce in query_dnf.args:
            # Check if the query component is a subset of the document terms
            try:
                for elem in str(q_ce).split('&'):
                    if elem not in doc_terms:
                        # If any component of the query matches, the document is a match
                        break
                else:
                    all_match = True
            except:
                if str(q_ce) in doc_terms:
                    all_match = True
            if all_match:
                matching_documents.append(doc_i)
                continue
                
        # If the document matches all components of the query, add it to the list

    return matching_documents,''
