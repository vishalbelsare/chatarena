import streamlit as st
from streamlit_chat import message, _streamlit_chat


def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    st.session_state.generated.append("The messages from Bot")


def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]


st.session_state.setdefault('past', [])
st.session_state.setdefault('generated', [])


with st.sidebar:
    st.title("Chat Arena")


with st.container():
    st.write("This is inside the container")

    chatbox = _streamlit_chat
    chatbox(message="Hello", key="chatbox")

    # # chat_placeholder = st.empty()
    # #
    # # with chat_placeholder.container():
    for i in range(len(st.session_state['generated'])):
        chatbox(message=st.session_state['past'][i], is_user=True, key=f"{i}_user")
        chatbox(message=st.session_state['generated'][i], key=f"{i}")


with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")
    st.button("Clear message", on_click=on_btn_click)
