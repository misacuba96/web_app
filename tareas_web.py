import streamlit as st
import funciones

todos = funciones.leer_tareas()


def añadir_tarea():
    todo = st.session_state["nueva_tarea"] + "\n"
    todos.append(todo)
    funciones.escribir_tareas(todos)


st.title("My App de Tareas")
st.subheader("Mi aplicación de tareas")
st.write("Esta es un programa de pruebas")

for index, i in enumerate(todos):
    checkbox = st.checkbox(i, key=i)
    if checkbox:
        todos.pop(index)
        funciones.escribir_tareas(todos)
        del st.session_state[i]
        st.rerun()


st.text_input(label="", placeholder="Agregue tarea..",
              on_change=añadir_tarea, key="nueva_tarea")


