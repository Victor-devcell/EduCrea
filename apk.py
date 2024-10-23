import streamlit as st

# Inicializar variables de estado si no existen
if 'info_1' not in st.session_state:
    st.session_state.info_1 = ""
if 'info_2' not in st.session_state:
    st.session_state.info_2 = ""

# Función para agregar información al primer botón
def agregar_info_1():
    st.session_state.info_1 += "Nueva información para el botón 1\n"

# Función para agregar información al segundo botón
def agregar_info_2():
    st.session_state.info_2 += "Nueva información para el botón 2\n"

# Crear los botones
col1, col2 = st.columns(2)

with col1:
    if st.button("Agregar Info 1"):
        agregar_info_1()

with col2:
    if st.button("Agregar Info 2"):
        agregar_info_2()

# Mostrar la información
st.text_area("Información del Botón 1:", value=st.session_state.info_1, height=100, disabled=True)
st.text_area("Información del Botón 2:", value=st.session_state.info_2, height=100, disabled=True)
