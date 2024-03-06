def boolean(query_dnf, tokenized_docs):
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

    return matching_documents
