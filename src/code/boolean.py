def similarity(query_dnf,tokenized_docs):
  # Convertir tokenized_docs a un conjunto de sets
  doc_term_sets = [set(doc) for doc in tokenized_docs]

  matching_documents = []
  for doc_i, doc_terms in enumerate(doc_term_sets):
    # Short-circuiting: si no hay coincidencia con una componente conjuntiva, se ignora el documento
    all_match = False
    for q_ce in query_dnf:
      if q_ce.issubset(doc_terms):
        all_match = True
        break
    if all_match:
      matching_documents.append(doc_i)

  return matching_documents