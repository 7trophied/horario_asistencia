import streamlit as st
import pandas as pd
import sqlite3

ruta_excel = 'horario_db.xlsx'  
df = pd.read_excel(ruta_excel)


conexion = sqlite3.connect('clases.db')  
nombre_tabla = 'clases'  
df.to_sql(nombre_tabla, conexion, if_exists='replace', index=False)
conexion.close()

st.write(f"los datos se han importado")


def mostrar_visualizar_clases():
    st.title("Ver Clases")

    
    conn = sqlite3.connect('clases.db')
    cursor = conn.cursor()

    
    cursor.execute("SELECT * FROM clases")
    clases = cursor.fetchall()

    
    if clases:
        
        df_clases = pd.DataFrame(clases, columns=["Carrera", "Materia", "ID", "Profesor","Semestre y Grupo", "Dia", "Horario", "Asistencia"])
        st.write(df_clases)
    else:
        st.write("No hay clases registradas en la base de datos.")

    conn.close()

mostrar_visualizar_clases()

