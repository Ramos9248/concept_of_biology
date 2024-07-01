from core_retrieval import core_retrieval
from utilities_core import llm_setup
import chainlit as cl

"""---------------------------------------------------------------------------------------
# Chat logic
---------------------------------------------------------------------------------------"""
async def chat_assiatant(query: str):
    search_result = core_retrieval(query)

    msg= [
        {
            "role": "system",
            "content": """ Take a user query and context. Based on context, give response to teh user query.
                            context: {context}

                            Rules:
                            1. Provide answer or response based on given 'context'.
                            2. If 'context' does not have the answer or response the return 'No information found in the document'
                            3. output as json
                                format : 
                                    "response" : "response to the user's query"
                            """.format(context=search_result)
        },

        {
            "role": "user",
            "content": query
        }
    ]

    res = llm_setup(messages = msg).initiate()
    # res = res.loads(res)
    print(res)
    # res = res["response"]

    return res


@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It sends back an intermediate response from the tool, followed by the final answer.

    Args:
        message: The user's message.

    Returns:
        None.
    """

    final_answer = await cl.Message(content="").send()

    print(message.content)
    # Call the tool
    final_answer.content = await chat_assiatant(query=message.content)
    # final_answer.content = "Give me 5 bucks :)"

    await final_answer.update()