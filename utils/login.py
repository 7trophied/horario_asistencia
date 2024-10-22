import sqlite3
import streamlit as st

# Función para validar el login contra la base de datos
def validar_login(usuario, contraseña):
    conn = sqlite3.connect('clases.db')
    cursor = conn.cursor()

    # Verificar si el usuario y la contraseña coinciden
    cursor.execute("SELECT rol FROM usuarios WHERE usuario=? AND contraseña=?", (usuario, contraseña))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]  # Retorna el rol del usuario (maestro, jefe_grupo, usuario_comun)
    else:
        return None

# Función para mostrar el formulario de login
def mostrar_login():
    st.title("Iniciar Sesión (usuario ucol)")
    
    # Estilos adicionales con CSS
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Inputs de usuario y contraseña
    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar Sesión"):
        rol = validar_login(usuario, contraseña)

        if rol:
            st.success(f"Bienvenido, {usuario} ({rol})")
            st.session_state['usuario'] = usuario
            st.session_state['rol'] = rol
            st.experimental_rerun()  # Recarga la página para cargar el menú según el rol
        else:
            st.error("Credenciales incorrectas. Inténtalo de nuevo.")
