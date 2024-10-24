import streamlit as st
import function


todos = function.get_todos()


def add_todo():
        todo=st.session_state['new_todo'] + '\n'
        todos.append(todo)
        function.write_todos(todos)
        



st.title('My Todo App')
st.subheader('hei amici questa è la mia porcoddio di app')
st.write('''questa app ti consente di ricordati tutto!!!!!
        (anche le chiavi del CBR) ''')


for index,todo in enumerate (todos):
       checkbox= st.checkbox(todo,key=todo)
       if checkbox:
               todos.pop(index)
               function.write_todos(todos)
               del st.session_state[todo]
               st.rerun()
        
        
st.text_input(label='scrivi una frase',placeholder='scrivi qui..',
              on_change=add_todo,key='new_todo')

print('hello')


