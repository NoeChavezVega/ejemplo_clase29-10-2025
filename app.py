import streamlit as st

st.title("Ejemplo para usar session_state")


if "count" not in st.session_state:
    st.session_state["count"] = 0

if "name" not in st.session_state:
    st.session_state["name"] = ""


if st.button("Click me"):
    st.session_state["count"] += 1
    
if nombre = st.text_input("Escribe tu nombre", st.session_state["name"])
st.session_state["name"] = nombre
st.write(st.session_state)
