# Expert Vendas AI

Um agente de IA especializado em vendas consultivas, copywriting persuasivo e criação de ofertas irresistíveis para negócios, produtos e serviços. Este projeto visa fornecer uma ferramenta poderosa para maximizar conversões, solucionar objeções, entender as dores do cliente e criar diferenciação competitiva, pensando e agindo como um "closer" profissional.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e01caded-2ea9-4719-a9de-757c4491faf5" />

## Funcionalidades Principais

*   **Agente de Vendas Consultivas:** Atua como um mentor, consultor e copywriter, com domínio de técnicas de persuasão, funil de vendas, storytelling, gatilhos mentais, negociação e abordagem em canais digitais.
*   **Criação de Conteúdo:** Capaz de gerar copys, páginas de vendas, scripts de ligação, abordagens para WhatsApp/Telegram, templates de e-mail, textos curtos para anúncios e planos de ação para lançamento.
*   **Interação Conversacional:** Interface de chat para interação direta com o agente de IA.
*   **Histórico de Conversas:** Mantém um histórico das interações para contexto contínuo.

## Tecnologias Utilizadas

*   **Backend:** Django (Python)
*   **LLM:** Groq (com modelos como Llama-3.1-8b-instant)
*   **Banco de Dados:** SQLite (para desenvolvimento)
*   **Gerenciamento de Ambiente:** `python-dotenv`

## Configuração do Projeto

Siga estes passos para configurar e rodar o projeto localmente:

### 1. Clonar o Repositório

```bash
git clone https://github.com/augdev1/Expertvendasai.git
cd Expertvendasai
```

### 2. Configurar Ambiente Virtual

É altamente recomendável usar um ambiente virtual para gerenciar as dependências do projeto.

```bash
python -m venv venv
# No Windows
.\venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate
```

### 3. Instalar Dependências

Instale todas as bibliotecas Python necessárias:

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (na mesma pasta que `manage.py`) com base no `.env.example`. **Substitua `YOUR_ACTUAL_GROQ_API_KEY` pela sua chave de API real do Groq.**

```dotenv
GROQ_API_KEY="SUA_CHAVE_DE_API_GROQ_AQUI"
AGNO_DB_PATH="./agno.db"
DJANGO_SECRET_KEY="sua-chave-secreta-aqui" # Gere uma chave segura para produção
DJANGO_DEBUG="True"
```

### 5. Migrações do Banco de Dados

Aplique as migrações do Django para configurar o banco de dados:

```bash
python agnoframework/manage.py migrate
```

### 6. Coletar Arquivos Estáticos (Opcional, para deploy)

```bash
python agnoframework/manage.py collectstatic
```

## Como Rodar a Aplicação

Para iniciar o servidor de desenvolvimento Django:

```bash
python agnoframework/manage.py runserver
```

Acesse a aplicação no seu navegador em `http://127.00.1:8000/`.

## Mudanças Recentes e Melhorias

*   **Remoção da Funcionalidade TTS (Text-to-Speech):** A funcionalidade de conversão de texto em fala foi removida para simplificar o projeto e focar na interação textual com o LLM.
*   **Correção do Salvamento do Histórico de Conversas:** O problema que impedia o salvamento e a exibição do histórico de conversas foi corrigido, garantindo que as interações anteriores sejam mantidas.
*   **Configuração da Chave de API Groq:** O processo de configuração da chave de API do Groq foi esclarecido e verificado para garantir a comunicação adequada com o modelo de linguagem.
*   **Inclusão de Arquivos do Projeto `agnoframework`:** Todos os arquivos essenciais do framework Django foram adicionados e rastreados pelo Git.

## Próximos Passos e Ideias para Melhoria

*   **Capacidades Multimodais:** Integrar modelos de Visão Computacional (por exemplo, do Hugging Face) para permitir que o agente "leia" e entenda imagens, respondendo a perguntas visuais ou descrevendo o conteúdo.
*   **Geração de Imagens:** Adicionar a capacidade do agente de gerar imagens com base em descrições textuais.
*   **Uso de Ferramentas (Function Calling):** Capacitar o LLM a interagir com ferramentas externas (pesquisa na web, APIs de CRM, etc.) para expandir suas capacidades.
*   **Memória de Longo Prazo:** Implementar um sistema mais robusto para o agente lembrar de informações importantes sobre o usuário ou tópicos ao longo do tempo.
*   **Deploy em Nuvem:** Realizar o deploy da aplicação em plataformas como Render, Railway, Heroku ou DigitalOcean para acesso público.

---
