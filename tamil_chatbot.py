import streamlit as st
import speech_recognition as sr
import os

st.set_page_config(page_title="Tamil News & Knowledge Chatbot")

st.title("🧠 Tamil News & Knowledge Chatbot")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner("🎤 Listening..."):
            audio = recognizer.listen(source, timeout=5)
        try:
            text = recognizer.recognize_google(audio)
            st.success("You said: " + text)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I couldn't understand your voice.")
        except sr.RequestError:
            st.error("Could not connect to speech recognition service.")
    return ""

def process_command(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "👋 Vanakkam! How can I assist you?"
    elif "tamil news" in text:
        return "🗞️ Here's a summary of today's Tamil news... (customize this)"
    elif "weather" in text:
        return "🌤️ Today’s weather in Tamil Nadu is sunny with light winds."
    elif "science" in text:
        return "🔬 Science is the study of the natural world. Ask me any topic!"
    elif "math" in text or "calculation" in text:
        return "➗ Sure! I can help with math problems. Try asking a question."
    elif "animal" in text:
        return "🐘 Tamil Nadu has rich wildlife including elephants, tigers, and birds!"
    else:
        return "😕 Sorry, I didn't understand that."

if st.button("🎙️ Speak Now"):
    spoken_text = recognize_speech()
    if spoken_text:
        st.chat_message("user").write(spoken_text)
        bot_reply = process_command(spoken_text)
        st.chat_message("assistant").write(bot_reply)

user_text = st.chat_input("💬 My name is Lithu. Type something")

if user_text:
    st.chat_message("user").write(user_text)
    bot_response = process_command(user_text)
    st.chat_message("assistant").write(bot_response)
