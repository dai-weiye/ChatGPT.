from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

import os


def get_chat_response(prompt, memory):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


