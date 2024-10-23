import streamlit as st
import google.generativeai as genai
from PIL import Image
import pandas as pd
from config import GEMINI_API_KEY
import tkinter as tk
import pyttsx3

agree = st.checkbox("Escuchar 🔊")

# Configuración de Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Configuración del modelo
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 1024,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)
# Función para obtener respuesta del chatbot
def get_chatbot_response(prompt):
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    return response.text


# Interfaz de Streamlit
st.title("Chatbot Educativo con IA")

st.write("Este chatbot puede responder preguntas sobre diversas materias y ofrecer explicaciones detalladas.")

engine = pyttsx3.init()

def leer_texto(texto):
    voices = engine.getProperty('voices')
    es_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
    engine.setProperty('voice', es_voice_id)
    engine.say(texto)
    engine.runAndWait()
    engine.startLoop(False)
    engine.setProperty('rate', 140)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
# Área de entrada del usuario
user_input = st.text_area("Haz tu pregunta aquí:", height=100)

def onWord(name, location, length):
   print('word', name, location, length)
   if location > 1:
      engine.stop()

if engine._inLoop:
    engine.endLoop()

if st.button("Enviar"):
    if agree:
        if user_input:
            with st.spinner("Generando respuesta..."):
                response = get_chatbot_response(user_input)
                st.write("Respuesta del Chatbot:")
                st.write(response)
                leer_texto(response)
        else:
            st.warning("Por favor, ingresa una pregunta.")
            leer_texto("Por favor, ingresa una pregunta.")
    if agree == False:
        if user_input:
            with st.spinner("Generando respuesta..."):
                response = get_chatbot_response(user_input)
                st.write("Respuesta del Chatbot:")
                st.write(response)
        else:
            st.warning("Por favor, ingresa una pregunta.")
            leer_texto("Por favor, ingresa una pregunta.")

if engine._inLoop:
    engine.endLoop()

st.markdown("---")
st.write("Este chatbot utiliza la IA de Gemini para proporcionar respuestas educativas.")

