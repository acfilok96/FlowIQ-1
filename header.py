import streamlit as st
from gorq_function import Groq_function
from gemini_function import Gemini_function


st.set_page_config(page_title="FlowIQ", layout="wide", page_icon = 'Image1/flowIQ8-1.png', initial_sidebar_state = 'auto')

st.markdown("""
<style>
.big-font-1 {
    font-size:30px !important;
    text-align: center; 
    color: yellow
}
</style>
""", unsafe_allow_html=True)


def main(): 
    # st.sidebar.markdown('<p class="big-font-1">FlowIQ</p>', unsafe_allow_html = True)
    
    st.sidebar.image("Image1/flowIQ5-1.png")
   
    model_name_check = st.sidebar.selectbox(""":blue[**Choose Model**]""", ("Llama3-70B", "Llama3-8B", "Mixtral-7B", "Gemma-7B", "Gemini-flash"))

    model_name = "llama3-8b-8192"
    model_pick = "Groq"
    if model_name_check == "Llama3-70B" :
        model_name = "llama3-70b-8192"
        model_pick = "Groq"
    elif model_name_check == "Llama3-8B" :
        model_name = "llama3-8b-8192"
        model_pick = "Groq"
    elif model_name_check == "Mixtral-7B" :
        model_name = "mixtral-8x7b-32768"
        model_pick = "Groq"
    elif model_name_check == "Gemma-7B" :
        model_name = "gemma-7b-It"
        model_pick = "Groq"
    elif model_name_check == "Gemini-flash":
        model_pick = "Gemini-flash"

    show_advanced_info_0 = st.sidebar.toggle(":blue[*Response Instruction*]", value = False)
    root_system_prompt = f"""Share only exact response, nothing else, nothing extra\n\n"""
    system_prompt = f"""\n"""
    if show_advanced_info_0:
        system_prompt = st.sidebar.text_input(":blue[**Response Instruction**]", placeholder = "Enter here", help = "For example, Share only exact response, nothing else, nothing extra. or Share your response in bengali language. or Share response.")
    root_system_prompt = str(root_system_prompt)+str("\n")+str(system_prompt)
    
    if model_pick == "Groq":
        Groq_function(model_name = model_name, system_prompt = root_system_prompt)
    elif model_pick == "Gemini-flash":
        Gemini_function(system_prompt = root_system_prompt)

    show_advanced_info_1 = st.sidebar.toggle(":blue[*Application Details*]", value = False)
    
    if show_advanced_info_1:
        st.sidebar.info("""

                    **Generative AI Chatbot**
                    
                    - **Model:** *Llama3, Mixtral, Gemma & Gemini*
                    
                    - **Language:** *English*
                    
                    - **Release Date:** *June, 2024*
                    
                    """)
        
    show_advanced_info_2 = st.sidebar.toggle(":blue[*Developer Details*]", value = False)
    
    if show_advanced_info_2:
        st.sidebar.info("""
                    
                    *This appplication has been created by [:blue[Dipankar Porey]](https://www.linkedin.com/in/dipankar-porey-403320259/),
                    BluWebMedia Pvt. Ltd., Ernst & Young.* 
                    
                    """)

       
if __name__ == '__main__':
    main()
