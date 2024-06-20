import streamlit as st
from excuses import Excuses
from chat_info import ChatModel
from streamlit_chat import message


def Groq_function(model_name = "llama3-8b-8192", system_prompt = "Share response.\n\n"):
    
    ################################################
         
    if "messages_temp_F" not in st.session_state:
        st.session_state.messages_temp_F = []


    k = 1
    # with container_11:

    for message_s in st.session_state.messages_temp_F:
        if message_s["role"] == "Dipankaruser":
            message(message_s["content"], is_user = True, key = str(k) + '_user', avatar_style = "initials", seed = "Dipankar Porey")
        elif message_s["role"] == "FlowIQassistant":
            message(message_s["content"], key = str(k), avatar_style = "initials", seed = "FlowIQ", allow_html = True)
        k += 1

    def clear_chat_history():
        
        st.session_state.messages_temp_F = []
        
    st.sidebar.button(':green[*Clear chat*]', on_click = clear_chat_history)
            
    if prompt := st.chat_input("Message here !"):
        
        # with container_11:
            
        st.session_state.messages_temp_F.append({"role": str("Dipankar")+"user", "content": prompt})
        

        message(prompt, is_user = True, key = str(k) + '_user', avatar_style = "initials", seed = "Dipankar Porey")

        k += 1
        full_response = ""
        with st.spinner(":green[just wait . . .]"):
            try: 

                full_response = ChatModel.GroqModel(prompt, system_prompt, model_name)
                
                message(full_response , key = str(k), avatar_style = "initials", seed = "FlowIQ", allow_html=True)
            
            except Exception as e:
                
                full_response = Excuses.listofExcuses()
                message(full_response, key = str(k), avatar_style = "initials", seed = "FlowIQ", allow_html=True)
            
        st.session_state.messages_temp_F.append({"role": str("FlowIQ")+"assistant", "content": full_response})

    else:
        st.info("""
        
        FlowIQ is a AI chatbot, a specialized hardware & software platform designed for \
        efficient & high-performance artificial intelligence (AI) & machine learning (ML) \
        workloads.

        It delivers exceptional compute speed, quality & energy efficiency.
        Key features of the FlowIQ platform include low power consumption, high throughput & low latency. 

        Supported models are **Llama3-70B**, **Llama3-8B**, **Mixtral-7B**, **Gemma-7B** & **Gemini-flash**.

        """)
        col1, col2 = st.columns(2)
        col1.warning("👈 Choose model !")
        col2.success(" 👇 Message below !")
        st.info("""
        
        Instruction for the output can to set as *Response Instruction*. For example, \
        *Share only exact response, nothing else, nothing extra.* or *Share your response in bengali language.* or *Share response.*
        By default, it's given as *Share only exact response, nothing else, nothing extra.*

        """)
