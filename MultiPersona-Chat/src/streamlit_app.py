import streamlit as st
import openai
import os
from system_prompts import prompts

openai.api_key=os.getenv("OPENAI_API_KEY")

st.title("Chabot")

persona=st.sidebar.selectbox("Choose Persona",list(prompts.keys()))
system_prompts=prompts[persona]

if "messages" not in st.session_state:
    st.session_state.messages.append({"role":"system","content":system_prompts})

user_input=st.text_input("You")
if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    try:
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply=response.choices[0].message["content"]
        st.session_state.messages.append({"role":"assistant","content":reply})
    except Exception as e:
        reply=f"Error: {e}"

for msg in st.session_state.messages:
    if msg["role"]=="user:"
        st.markdown(f"**You {msg['content']}")
    elif msg["role"]=="assistant":
        st.markdown(f"**Bot ({persona}):** {msg['content']}")