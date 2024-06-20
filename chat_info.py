from geminiKey import GeminiKey
import google.generativeai as geminiai
from gorqKey import GorqKey
from groq import Groq

class ChatModel:
    def __init__(self):
        pass
    
    @staticmethod
    def GroqModel(user_prompt, system_prompt, model_name):
        
        client = Groq(api_key = str(GorqKey()))
        
        chat_completion = client.chat.completions.create(
                    messages = [{"role": "user",
                                "content": user_prompt},
                               {"role": "system",
                                "content": system_prompt}],
                                model = model_name,
                    )
        return chat_completion.choices[0].message.content
    
    @staticmethod
    def GeminiModel(user_prompt, system_prompt):
        
        main_prompt = f"""{user_prompt}. {system_prompt}"""
        
        ################################################
        
        MODEL_CONFIGURATION = {
        "temperature" : 0.0,
        "top_p" : 1,
        "top_k" : 1,
        "max_output_tokens" : 400,
        }
        
        ################################################
        
        safety_settings = [
            {
                "category": "HARM_CATEGORY_DANGEROUS",
                "threshold": "BLOCK_NONE",
            },
            {
                "category" : "HARM_CATEGORY_HARASSMENT",
                "threshold" : "BLOCK_NONE", # "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category" : "HARM_CATEGORY_HATE_SPEECH",
                "threshold" : "BLOCK_NONE", # "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category" : "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold" : "BLOCK_NONE", # "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category" : "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold" : "BLOCK_NONE", # "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]
        
        geminiai.configure(api_key = str(GeminiKey()))  # "AIzaSyAde1168Yh8ORh8GS-jFMWMDNg7h5RbiHw"
        
        ################################################
        
        gemini_model = geminiai.GenerativeModel(model_name = "gemini-1.5-flash", # "gemini-1.0-pro-vision-latest",
                                                generation_config = MODEL_CONFIGURATION,
                                                safety_settings = safety_settings)
        
        chat = gemini_model.start_chat(history=[])
        response = chat.send_message(main_prompt)
        full_response = response.text
        
        return full_response
