import streamlit as st
import datetime,time
from dbhelper import DBHelper


st.set_page_config(page_title='Agentic Chat UI')
st.subheader('Write a Task to Delegate')
@st.cache_resource
def get_db():
    db = DBHelper()
    db.select_collection("tasks")
    return db

db_helper = get_db()

task_clues = {
    'how to create a task' : 'Create task: title, description, action(call etc.), contact_name,contact_phone',
    'how to view tasks' : 'list all tasks',
    'how to update task': 'update task: title, description, action(call etc.), contact_name,contact_phone',
    'how to delete task' : 'delete task: title'
}

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['text'])
    

user_input = st.chat_input('Type your Task here')
if user_input:
    
    message = {
        'role':'user',
        'text' : user_input
    }
    st.session_state.messages.append(message)
    with st.chat_message(message['role']):
        st.markdown(message['text'])
    
    if user_input in task_clues:
        clue = task_clues[user_input]

        message = {
            'role':'assistant',
            'text' : clue
        }
        st.session_state.messages.append(message)
            
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)
    elif 'create task:' in user_input:
        #save the task in MongoDB
        data1 = user_input.split(':')
        data2 = data1[1].split(',')
        task = {
            'title': data2[0].strip(),
            'description': data2[1].strip(),
            'action': data2[2].strip(),
            'contact_name': data2[3].strip(),
            'contact_phone': data2[4].strip(),
            'status': 'PENDING',
            'created_at': datetime.datetime.now()
        }
        db_helper.save(task)
        message = {
            'role':'assistant',
            'text' : f'Task: {task["title"]}, Saved Successfully.'
        }
        st.session_state.messages.append(message)
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)
    elif 'list all tasks' in user_input:
        documents = db_helper.retrieve()
        document_text = ''
        for i, document in enumerate(documents, start=1):
            document_text += (
                f"Task {i}\n\n"
                f"Title: {document['title']}\n\n"
                f"Description: {document['description']}\n\n"
                f"Action: {document['action']}\n\n"
                f"Contact: {document['contact_name']}\n\n"
                f"Phone: {document['contact_phone']}\n\n"
                f"Status: {document['status']}\n\n"
                f"Created At: {document['created_at']}\n\n"
                f"\n{'='*45}\n\n"
            )
        message = {
            'role':'assistant',
            'text' : document_text
        }
        st.session_state.messages.append(message)
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.01)
                
    elif 'update task:' in user_input:
        data1 = user_input.split(':')
        data2 = data1[1].split(',')
        task = {
            'title': data2[0].strip(),
            'description': data2[1].strip(),
            'action': data2[2].strip(),
            'contact_name': data2[3].strip(),
            'contact_phone': data2[4].strip(),
            'status': 'PENDING',
            'created_at': datetime.datetime.now()
        }
        condition = {'title' : task['title']}
        text = db_helper.update(condition,task)
        message = {
            'role':'assistant',
            'text' : text
        }
        st.session_state.messages.append(message)
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)
    elif 'delete task:' in user_input:
        data1 = user_input.split(':')
        data2 = data1[1].strip()
        condition = {'title' : data2}
        text = db_helper.delete(condition)
        message = {
            'role':'assistant',
            'text' : text
        }
        st.session_state.messages.append(message)
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)
    else:
        message = {
            'role':'assistant',
            'text' : 'Sorry, I cannot Help You'
        }
        st.session_state.messages.append(message)
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)
