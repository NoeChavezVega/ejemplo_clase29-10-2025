import streamlit as st
st.title("Ejemplo para usar sesion_state")

count = 0

increment = st.button("Increment")
if increment :
  count += 1
  
st.write("Count =" , count)
# st. sessio_state= demuestra las cantidades que va guardando 

if "count" not in st.session_state:
  st.session_state["count"] = 0

if "name" not in st.session_state:
  st.session_state["name"] = ""

st.write(st.session_state)

if st.button("Click me"):
  st.session_state["count"] = 1

nombre = st.text_input("Escribe tu nombre")
st.write(nombre)

st.write(st.session_state)
