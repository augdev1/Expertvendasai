👽 Devchat: Agente de IA especializado em programação e IA

💬 Chat tutor focado para desenvolvedores e estudantes de tecnologia

📝 Descrição
Este projeto é um agente conversacional de Inteligência Artificial focado exclusivamente em temas de programação e IA 🤖.
Seu objetivo é ser um tutor digital, respondendo questões técnicas, oferecendo exemplos de código 💻, esclarecendo dúvidas sobre linguagens e frameworks.

🚫 O agente não responde temas fora da área de tecnologia, garantindo foco e especialização, tornando o ambiente seguro e eficiente para quem busca aprendizado estruturado em desenvolvimento e inteligência artificial.

🛠️ Principais Tecnologias

⚡ Gemini 2.5 Flash — modelo LLM de alta performance para respostas contextualizadas

🕸️ Agno — framework para orquestração de agentes e contexto histórico

🌐 Streamlit — interface web interativa para chat e visualização

🐍 Python — toda a lógica de backend e integração

🚀 FastAPI — opcional para servir rotas de API para integrações externas

🗃️ SQLite — armazenamento local de histórico de conversa/contexto

🗝️ dotenv/Python-dotenv — gerenciamento de variáveis de ambiente e config

✨ Funcionalidades
💬 Chat interativo com agente IA restrito a tópicos de programação e IA

🎓 Geração de exemplos de código, boas práticas e dicas para devs

📚 Citação de fontes confiáveis e explicação técnica contextualizada

🖥️ Interface moderna e responsiva via Streamlit

🗂️ Histórico de conversas salvo em banco SQLite

🚀 Possibilidade de extensão via API usando FastAPI

⚙️ Instalação
Clone o repositório


git clone https://github.com/augdev1/Devchat.git
cd ai-dev-chat-by-aug
Crie e ative um ambiente virtual (opcional, mas recomendado):


python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
Instale as dependências:
pip install -r requirements.txt

Configure variáveis de ambiente:

Crie um arquivo .env com suas credenciais (API keys, configs do Gemini, etc).

Rode o projeto:

streamlit run app.py
Ou rode o servidor FastAPI (opcional, se desejar API REST):

uvicorn testapi:app --reload
⚡ Como funciona
O agente utiliza o LLM Gemini 2.5 Flash via Agno, recebendo instruções personalizadas para responder apenas assuntos de dev e IA.

O chat filtra qualquer pergunta fora do escopo e prioriza explicações claras, exemplos reais e recomendações metodológicas para aprendizado e prática profissional.

🏗️ Arquitetura
agent.py — Lógica do agente via Agno

agno.db — Banco SQLite para histórico/contexto

teste_front.py — Agno + Gemini + Streamlit para visual

testapi.py — Servidor FastAPI (opcional)

🚩 Diferenciais
🎯 Foco exclusivo em tecnologia: não responde sobre temas gerais

⚙️ Respostas pensadas para devs, profissionais de IA

🚀 Alto desempenho e contexto preservado na conversa

🔌 Fácil extensão e integração via API

🤝 Contribuições e Licença
Pull requests e sugestões são bem-vindas!
Licença MIT.
