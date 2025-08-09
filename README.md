# Projeto de Agentes de IA com CrewAI e RAG para Análise de Apólices de Seguro

Este repositório contém um projeto que demonstra o uso de Agentes de Inteligência Artificial, construídos com a ferramenta CrewAI, para responder a perguntas sobre um seguro de saúde. As respostas são geradas a partir de informações extraídas de um documento PDF, utilizando a técnica de Geração Aumentada por Recuperação (RAG).

## 🇧🇷 Em Português

### 📄 Sobre o Projeto

O objetivo deste projeto é criar uma equipe de agentes de IA autônomos que colaboram para fornecer respostas precisas e contextuais a perguntas relacionadas a uma apólice de seguro de saúde. Para isso, utilizamos a biblioteca CrewAI, que permite orquestrar, de forma flexível e poderosa, o trabalho de múltiplos agentes com papéis e ferramentas distintas.

A base de conhecimento para nossos agentes é um arquivo PDF contendo os detalhes da apólice de seguro. A técnica de RAG é empregada para permitir que os agentes consultem este documento em tempo real, garantindo que as respostas sejam sempre baseadas nas informações contidas no PDF.

### ⚙️ Como Funciona

O fluxo de trabalho do projeto pode ser resumido nas seguintes etapas:

1.  **Configuração da Equipe (Crew):** Definimos uma equipe de agentes de IA, cada um com uma função específica. Por exemplo, podemos ter um agente "Pesquisador" responsável por encontrar as informações relevantes no PDF e um agente "Analista" que interpreta essas informações para formular a resposta final.
2.  **Definição das Tarefas (Tasks):** Criamos as tarefas que a equipe de agentes deve executar. A tarefa principal é receber uma pergunta do usuário sobre o seguro de saúde.
3.  **Processo de RAG (Retrieval-Augmented Generation):**
    * Quando uma pergunta é recebida, o agente "Pesquisador" utiliza uma ferramenta de busca em documentos (como a `PDFSearchTool` do CrewAI) para vasculhar o PDF da apólice de seguro.
    * A ferramenta de RAG não apenas localiza trechos relevantes, mas também os utiliza para "aumentar" o contexto da pergunta original.
    * Essa informação enriquecida é então passada para o agente "Analista".
4.  **Geração da Resposta:** O agente "Analista", com o contexto fornecido pelo RAG, gera uma resposta coesa e precisa para a pergunta do usuário.

### 🛠️ Tecnologias Utilizadas

* **CrewAI:** Framework para orquestração de agentes de IA autônomos.
* **Python:** Linguagem de programação principal do projeto.
* **Modelos de Linguagem (LLMs):** O projeto pode ser configurado para usar diferentes LLMs, como os da OpenAI, Google, ou modelos open-source.
* **Bibliotecas de RAG:** Ferramentas que permitem a busca e recuperação de informações em documentos, como a `PDFSearchTool` integrada ao CrewAI.

### 🚀 Como Começar

Para executar este projeto em seu ambiente local, siga estas etapas:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/goncasthiago/my_acp_project.git](https://github.com/goncasthiago/my_acp_project.git)
    cd seu-repositorio
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

    **Utilizando o UV:**
    ```bash
    cd my_acp_project
    uv init
    uv venv
    source .venv/bin/activate
    uv add crewai crewai-tools acp-sdk load_dotenv nest-asyncio python-dotenv colorama
    ```
3.  **Adicione sua chave de API:**
    * Renomeie o arquivo `.env.example` para `.env`.
    * Insira sua chave de API do modelo de linguagem que você utilizará (por exemplo, `OPENAI_API_KEY`).

4.  **Coloque o arquivo PDF:**
    * Adicione o arquivo PDF da apólice de seguro na pasta designada no projeto (por exemplo, `data/`).

5.  **Execute o projeto:**
    ```bash
    python main.py
    ```

### 💬 Exemplo de Uso

Após iniciar o projeto, você poderá inserir perguntas como:

* "Qual a cobertura para despesas com fisioterapia?"
* "O plano cobre consultas com psicólogos?"
* "Qual o procedimento para solicitar um reembolso?"

Os agentes de IA irão processar sua pergunta, consultar o PDF e fornecer uma resposta detalhada com base nas informações encontradas.

---

## 🇺🇸 In English

### 📄 About the Project

The goal of this project is to create a team of autonomous AI agents that collaborate to provide accurate and contextual answers to questions related to a health insurance policy. To achieve this, we use the CrewAI library, which allows for the flexible and powerful orchestration of multiple agents with distinct roles and tools.

The knowledge base for our agents is a PDF file containing the details of the insurance policy. The RAG technique is employed to enable the agents to consult this document in real-time, ensuring that the answers are always based on the information contained within the PDF.

### ⚙️ How It Works

The project's workflow can be summarized in the following steps:

1.  **Crew Setup:** We define a crew of AI agents, each with a specific role. For example, we might have a "Researcher" agent responsible for finding relevant information in the PDF and an "Analyst" agent who interprets this information to formulate the final answer.
2.  **Task Definition:** We create the tasks that the crew of agents must execute. The main task is to receive a user's question about the health insurance.
3.  **RAG Process (Retrieval-Augmented Generation):**
    * When a question is received, the "Researcher" agent uses a document search tool (such as CrewAI's `PDFSearchTool`) to scan the insurance policy PDF.
    * The RAG tool not only locates relevant passages but also uses them to "augment" the context of the original question.
    * This enriched information is then passed to the "Analyst" agent.
4.  **Response Generation:** The "Analyst" agent, with the context provided by RAG, generates a cohesive and precise answer to the user's question.

### 🛠️ Technologies Used

* **CrewAI:** A framework for orchestrating autonomous AI agents.
* **Python:** The main programming language for the project.
* **Language Models (LLMs):** The project can be configured to use different LLMs, such as those from OpenAI, Google, or open-source models.
* **RAG Libraries:** Tools that enable information search and retrieval in documents, like the `PDFSearchTool` integrated with CrewAI.

### 🚀 Getting Started

To run this project in your local environment, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/goncasthiago/my_acp_project.git](https://github.com/goncasthiago/my_acp_project.git)
    cd your-repository
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

     **Using UV:**
    ```bash
    cd my_acp_project
    uv init
    uv venv
    source .venv/bin/activate
    uv add crewai crewai-tools acp-sdk load_dotenv nest-asyncio python-dotenv colorama

3.  **Add your API key:**
    * Rename the `.env.example` file to `.env`.
    * Insert your API key for the language model you will be using (e.g., `OPENAI_API_KEY`).

4.  **Place the PDF file:**
    * Add the insurance policy PDF file to the designated folder in the project (e.g., `data/`).

5.  **Run the project:**
    ```bash
    python main.py
    ```

### 💬 Example Usage

After starting the project, you can enter questions such as:

* "What is the coverage for physiotherapy expenses?"
* "Does the plan cover consultations with psychologists?"
* "What is the procedure for requesting a reimbursement?"

The AI agents will process your question, consult the PDF, and provide a detailed answer based on the information found.



