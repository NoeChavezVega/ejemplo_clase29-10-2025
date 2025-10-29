import streamlit as st

st.title("Ejemplo para usar session_state")

# Inicializar las variables en session_state si no existen
if "count" not in st.session_state:
    st.session_state["count"] = 0

if "name" not in st.session_state:
    st.session_state["name"] = ""

# Botón que aumenta el contador
if st.button("Click me"):
    st.session_state["count"] += 1

# Entrada de texto para el nombre
nombre = st.text_input("Escribe tu nombre", st.session_state["name"])

# Guardar el nombre en session_state
st.session_state["name"] = nombre

# Mostrar el nombre y el contador
st.write(f"Hola, {st.session_state['name']}!")
st.write(f"Has hecho clic {st.session_state['count']} veces.")

# Mostrar todo el session_state (opcional, para depurar)
st.write("Estado actual de sesión:")
st.write(st.session_state)
