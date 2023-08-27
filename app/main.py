'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-08-19 13:03:28
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-08-19 13:10:36
 # @ Description:
'''

import os
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv, find_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

from langchain.memory import ConversationBufferMemory


def init_chatbot():
    # load env variables and error handling if key not found
    _ = load_dotenv(find_dotenv())
    open_api_key = os.getenv("OPENAI_API_KEY")
    
    if open_api_key is None or len(open_api_key) == 0:
        st.error("Please set your OpenAI API key in the environment variable OPENAI_API_KEY.")
        return
    else:
        print("OpenAI API key found.")

def main():
    init_chatbot()    
    
    st.header("FoodieGPT 🍙")

    # takes in a history of messages
    chat = ChatOpenAI(temperature = 0,
                      model_name = "gpt-3.5-turbo")
    
    # append to session_state (st's persistent variables)
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content = "You are a helpful assistant.")
        ]
    
    
    # st.set_page_config(page_title="FoodieGPT", 
    #                    page_icon="🍙",)
    
    message("Hello, I am FoodieGPT. Anything i can help you with?",
            is_user = False)

    
    with st.sidebar:
        user_input = st.text_input("Enter a prompt",
                                   key="I love to eat")
        
        # user input
        if user_input:
            message(user_input, is_user = True)
            # adding user input to conversational dialogue
            st.session_state.messages.append(HumanMessage(content = user_input))
            with st.spinner("Cooking..."):       
                # conversational log --> response -append-> conversational log
                response = chat(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content = response.content))

        
        st.markdown(
            "---\n"
            "## How to use\n"
            "1. Upload a csv of your favored restaurant (optional) 📄\n"  
            "2. Chat with FoodieGPT\n"
            "3. yum, yum in your tummy 💬\n"
        )

        st.markdown(
            "---\n"
            "## About Team 8\n"
            "Adam, Nick, Jiaxin, Rick, Alessandro! \n"
        )
        st.markdown(
            "your pocket guide to the best restaurants in town 🍙\n"
            "Doesn't matter if you are feeling exotic food or just something local.\n"
            "FoodieGPT got you covered!\n"
        )
        
    # show the messages hisotry
    messages = st.session_state.get('messages', [])
    
    # skip the 1st system msg
    for i,msg in enumerate(messages[1:]):
        # user
        if i % 2 == 0:
            message(msg.content,
                    is_user = True,
                    key = str(i) + '_user',)
        else:
            message(msg.content, 
                    is_user = False, 
                    key = str(i) + '_bot',)
            
    
if __name__ == "__main__":
    main()