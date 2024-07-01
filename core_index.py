from utilities_core import helper_setup_env
from utilities_core import doc_parse, doc_chunk
from utilities_core import embed_connection, apply_embedding_doc
from utilities_core import setup_pinecone, doc_index
import json

from data import get_info

#0.0: AI model set up and vector DB set up
embeddings_model = embed_connection()
setup_pinecone("index-quantiphi")

# core upload and index function
def upload_and_index(filenm, kb):
    print("Parsing initiated")
    #1.0 apply parsing
    _text_all, metadata = doc_parse(filenm)
    print("Parsing successful")
    _text = get_info()
    
    #2.0: apply chunking
    print("Chunking initiated")
    doc_obj = doc_chunk(_text, metadata)
    print("Chunking successful")

    print(doc_obj)
    
    # doc_obj = json.loads(doc_obj)
    # print(type(doc_obj))

    # with open(".\data\chunk_result.json", 'w', encoding='utf-8') as jfile:
    #     json.dump(doc_obj, jfile, indent=4, ensure_ascii=False)

    #3.0: apply sense emedding
    print("Embedding initiated")
    embed_doc = apply_embedding_doc(embeddings_model, doc_obj, kb)
    print("Embedding successful")


    #5.0: indexing
    print("Indexing initiated")
    doc_index(embed_doc, "index-quantiphi", namespace=kb)
    print("Indexing successful")



# if __name__ =="__main__":
#     print("Parsing initiated")
#     filenm = r".\data\temp\index-quantiphi\ConceptsofBiology-WEB.pdf"
#     #1.0 apply parsing
#     _text, metadata = doc_parse(filenm)
#     print(len(_text))
          
    
#     # #2.0: apply chunking
#     # print("Chunking initiated")
#     # doc_obj = doc_chunk(_text, metadata)
#     # print(len(doc_obj))
