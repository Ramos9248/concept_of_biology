from core_search import retrieve_search_result

def core_retrieval(query: str):
    search_result = retrieve_search_result(query =query , 
                           search_type = 'hybrid', 
                           kb = 'index-quantiphi', 
                           num_retievals=5)
    
    search_string = ""
    for val in search_result.get("matches"):
        search_string += val.get("metadata").get("chunk_text") 
        # chunk_num = val.get("metadata").get("chunk_num") 
        # print(chunk_num)
        # print(search_string)
        # print("---------------------------------------------")

    return search_string


##testing

if __name__ == "__main__":
    # search_result = core_retrieval("what is haemoglonbin?")
    # print(search_result)
    pass

    