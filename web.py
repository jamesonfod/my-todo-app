
# streamlit run web.py

import streamlit as st
import functions

todo_list = functions.get_todo_items()

def add_todo():
    new_todo_item = st.session_state["new_todo_item"] + "\n"
    todo_list.append(new_todo_item)
    functions.write_todo_items(todo_list)


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.write_todo_items(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a todo item...",
              on_change=add_todo, key="new_todo_item")

