
from pinecone import Pinecone
index_name = 'index-quantiphi'
namespace = 'index-quantiphi'
pinecone = Pinecone(api_key='8de69224-0aea-435d-a8f6-1f665a12abec')
index = pinecone.Index(index_name)
index.delete(namespace=namespace, delete_all=True)