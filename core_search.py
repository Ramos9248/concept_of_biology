from utilities_core import helper_setup_env
from utilities_core import embed_connection, apply_embedding_query
from utilities_core import doc_search

#0.0: AI model set up
embeddings_model = embed_connection()

#1.0: search fucntion
def retrieve_search_result(query, search_type, kb, num_retievals=100):
    search_result = doc_search(query, 
                           'index-quantiphi',
                           embeddings_model, 
                           num_retievals=num_retievals,
                           search_type  =search_type,
                           namespace=kb)
    
    return search_result
"""
search_result = retrieve_search_result("What the indicaton uder review for oncology")
print(search_result)
"""