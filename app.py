import streamlit as st
import speech_recognition as sr

st.title("Speech-to-Text Web App")

st.write("Click the button and start speaking...")

if st.button("Start Recording"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success("Transcription:")
        st.write(text)
    except sr.UnknownValueError:
        st.error("Could not understand audio.")
    except sr.RequestError as e:
        st.error(f"Could not request results; {e}")

