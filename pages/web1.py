import streamlit as st
from modules.functions import *


todos = get_todos(filepath=r'./files/todos.txt')
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    print('add', todo)
    if todo != '':
        todos.append(todo) # doesn't add \n without string
        write_todos(todos, filepath=r'./files/todos.txt')
        del st.session_state['new_todo']


st.title('My todo app')
st.subheader('This is my todo app')
st.write('This app is to increase your <b>productivity</b>.', unsafe_allow_html=True)

for index, todo in enumerate(todos):
    print('"{}"'.format(todo))
    checkbox = st.checkbox(todo, key='checkbox-{}'.format(index))
    if checkbox:
        print(todo.strip('\n'), checkbox)
        todos.pop(index)
        write_todos(todos, filepath=r'./files/todos.txt')
        del st.session_state['checkbox-{}'.format(index)]
        st.rerun()

if 'new_todo' not in st.session_state:
    st.session_state.new_todo = ''
    st.session_state.widget = ''

def submit():
    st.session_state.new_todo = st.session_state.widget#.copy()
    st.session_state.widget = ''
    add_todo()

st.text_input(label='', value='', placeholder='Add a todo item...', key='widget', on_change=submit)

# st.write(f'Last submission: {st.session_state.new_todo}')

print('hello')
# st.session_state

