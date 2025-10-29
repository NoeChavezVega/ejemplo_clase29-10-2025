import streamlit as st
st.title("Ejemplo para usar sesion_state")

count = 0

increment = st.button("Increment")
if increment :
  count += 1


st.write("Count =" , count)
# st. sessio_state= demuestra las cantidades que va guardando 
st.session_state

