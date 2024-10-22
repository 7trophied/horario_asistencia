import streamlit as st
from streamlit_option_menu import option_menu
import pages.inicio as inicio
import pages.registro_clase as registro_clase
import pages.registro_maestro as registro_maestro
import pages.visualizar_clases as visualizar_clases
import pages.reportes_estadisticas as reportes_estadisticas
from utils.login import mostrar_login
import sqlite3

# Registro de clase integrara los reportes de cada jefe de grupo en la parte inferior.
# Registro de maestro permitira logearse como maestro o superior y agregar horarios con todos los semestres.
# Visualizar clases sera una forma sencilla de ver el horario, separando por semestre, dia y hora.
# Acerca sera una opcion donde se haran automaticamente los reportes de cada semestre de manera semanal, donde se verificara el haber cumplido con las clases correspondientes en tiempo y forma.

#   ├── main.py
#   ├── pages()
#   │   ├── inicio.py
#   │   ├── registro_clase.py
#   │   ├── visualizar_clases.py                   
#   │   ├── reportes_estadisticas.py
#   ├── utils()
#   │   ├── login.py
#   ├── clases.db

def conectar_db():
    conn = sqlite3.connect('clases.db')
    return conn

def main():
    conn = conectar_db()

    with st.sidebar:
        selected = option_menu(
            "Menú Principal", 
            ["Inicio", "Registro de Clase", "Registro de Maestro", "Visualizar Clases", "Reportes y Estadísticas"], 
            icons=['house', 'book', 'person-add', 'clipboard', 'bar-chart-line'],
            menu_icon="menu-up", 
            default_index=0,
            styles={
                "container": {"padding": "1rem", "background-color": "#f5f5f5"},
                "icon": {"color": "#4CAF50", "font-size": "20px"}, 
                "nav-link": {
                    "font-size": "18px", 
                    "text-align": "left", 
                    "margin": "5px 0", 
                    "padding": "10px",
                    "--hover-color": "#f0f0f0",
                    "color": "#333333",
                    "font-weight": "bold",
                },
                "nav-link-selected": {"background-color": "#4CAF50", "color": "white"},
                "menu-title": {"font-weight": "bold", "color": "#333333", "font-size": "24px"}
            }
        )

   # if not mostrar_login():
       # st.warning("Por favor, inicia sesión para continuar.")
        # return

    if selected == "Inicio":
        inicio.mostrar_inicio()
    elif selected == "Registro de Clase":
        registro_clase.mostrar_registro_clase(conn)
    elif selected == "Registro de Maestro":
        registro_maestro.mostrar_registro_maestro(conn)
    elif selected == "Visualizar Clases":
        visualizar_clases.mostrar_visualizar_clases(conn)
    elif selected == "Reportes y Estadísticas":
        reportes_estadisticas.mostrar_reportes(conn)
    else:
        st.error("Opción no válida")

if __name__ == "__main__":
    main()
