from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
import streamlit as st
import os

load_dotenv()

db = SqliteDb(db_file="agno.db")
llm_model = Gemini(id="gemini-2.5-flash")

agent = Agent(
    model=llm_model,
    db=db,
    add_history_to_context=True,
    instructions=(
        "Você é um assistente de programação e IA para desenvolvedores. "
        "Use respostas detalhadas. "
        "Cite fontes confiáveis e sempre mantenha o contexto das interações anteriores, seja claro, objetivo e ofereça exemplos de código quando for útil. "
        "Priorize explicações em português e adapte respostas ao nível do público (iniciante ou avançado). "
        "Responda perguntas sobre Python, IA, React, JavaScript, Tailwind, TypeScript. "
        "Quando adequado, explique termos técnicos e sugira boas práticas de desenvolvimento. "
        "Evite responder fora dessas áreas, e nunca invente ou omita informações importantes. "
        "Para tarefas de automação, gere scripts funcionais e explique passo a passo como implementar. "
        "Instrua sobre possíveis erros comuns, formas de testar o código e recursos de documentação útil para devs. "
        "Quando solicitado, faça recomendações de bibliotecas, frameworks e metodologias de estudo, considerando o contexto do projeto ou disciplina mencionada na conversa. "
        "Ao final de cada interação, pergunte se o usuário quer algo mais específico. "
        "Seja claro e assertivo, poupando várias linhas."
    ),
    markdown=True,
)





#STREAMLIT

st.set_page_config(page_title="ASSISTENTE IA PARA DEVS", layout="wide")

st.set_page_config(page_title="DEV CHAT", layout="wide")

# CSS customizado:
st.markdown("""
    <style>
    .stApp{
        background-color:  #222327;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .chat-bubble-user {
        background: #3d6868;
        border-radius: 12px;
        padding: 10px 16px;
        color: #222327;
        margin-bottom: 8px;
        margin-right: 40%;
        font-size: 1rem;
    }
    .chat-bubble-agent {
        background: #fff;
        border-radius: 12px;
        padding: 10px 16px;
        color: #35353f;
        margin-bottom: 8px;
        margin-left: 40%;
        font-size: 1rem;
        border: 1px solid #ececf1;
    }
    .stTextInput input {
        background: #fff;
        color: #3d6868;
        border-radius: 8px;
        border: none;
        font-size: 1rem;
    }
    </style>
    """, unsafe_allow_html=True
)

st.set_page_config(page_title="DEV CHAT", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    /* Muda cor da barra de cima (header Streamlit) */
    header[data-testid="stHeader"] {
        background-color: #000000;
        box-shadow: none;
    }
    header[data-testid="stHeader"] .st-emotion-cache-18ni7ap {
        background: none;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .chat-bubble-user {
        background: #3d6868;
        border-radius: 12px;
        padding: 10px 16px;
        color: #ececec;
        margin-bottom: 8px;
        margin-right: 40%;
        font-size: 1rem;
    }
    .chat-bubble-agent {
        background: #fff;
        border-radius: 12px;
        padding: 10px 16px;
        color: #35353f;
        margin-bottom: 8px;
        margin-left: 40%;
        font-size: 1rem;
        border: 1px solid #ececf1;
    }
    .stTextInput input {
        background: #fff;
        color: #3d6868;
        border-radius: 8px;
        border: none;
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='
        color:#ececec;
        text-align:center;
        width:100%;
        margin-top:32px;
        margin-bottom:0;
        font-size:2.4rem;
        font-weight:700;
        letter-spacing:-2px;
    '>
        👽 DEV CHAT 
    </h1>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    if msg["role"] == "Usuário":
        st.markdown(f"<div class='chat-bubble-user'>Você: {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-agent'>Agente: {msg['content']}</div>", unsafe_allow_html=True)

with st.form(key="chat_form"):
    user_input = st.text_input("Digite sua pergunta:", key="input", label_visibility="collapsed")
    send = st.form_submit_button("Enviar")
    if send and user_input:
        st.session_state.messages.append({"role": "Usuário", "content": user_input})
        response = agent.run(user_input)
        st.session_state.messages.append({"role": "Agente", "content": response.content})
        st.rerun()