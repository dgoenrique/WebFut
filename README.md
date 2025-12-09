# WebFut - Painel de Gestão de Loja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://webfut.streamlit.app/)

> **Acesse o Dashboard Online:** [https://webfut.streamlit.app/](https://webfut.streamlit.app/)

Este projeto é uma solução de **Business Intelligence (BI)** voltada para o gerenciamento de inventário e precificação de camisas de futebol. Através de um painel interativo, é possível analisar o valor de estoque, distribuição de itens por times e categorização por tipo (Home, Away, Third, Outro).

O projeto é "End-to-End": os dados foram coletados via **Web Scraping**, tratados e depois visualizados.

## 📊 Funcionalidades do Dashboard

O painel foi construído focado em **KPIs de Varejo**:

* **Visão Geral de Inventário:** Métricas de Valor Total de Estoque e Ticket Médio.
* **Composição de Mix (Treemap):** Visualização hierárquica de Times e Tipos de Kit (Home, Away, Third) para identificar saturação de estoque.
* **Análise Financeira:** Identificação dos times que representam maior capital imobilizado ("dinheiro parado").
* **Segmentação por Era:** Classificação automática em "Retrô" (Anos 90/00) vs "Moderno" para direcionamento de marketing.
* **Faixas de Preço:** Categorização dos produtos em Entrada, Médio e Premium.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Visualização:** [Streamlit](https://streamlit.io/) (Interface Web)
* **Manipulação de Dados:** Pandas
* **Gráficos:** Plotly Express
* **Coleta de Dados:** BeautifulSoup e Cloudscraper

## 📂 Estrutura do Projeto

A solução está organizada em duas etapas principais: Coleta (ETL) e Visualização.

```text
/
├── LICENCE
├── README.md
├── requirements.txt # Requisitos para rodar o sistema
│
├── collect/          # Scripts de Web Scraping e ETL inicial
│   ├── web_scraping.py        # Extração dos dados brutos
|   ├── manipulation.py        # Limpeza primária
│   └── T_manipulation.ipynb   # Testes para manipulação dos dados    
|   
│
└── dashboard_camisetas/       # Aplicação Streamlit (Este repositório)
    ├── app.py                 # Código principal do Dashboard
    └── data/
        ├── data_camisetas.csv # Dataset processado
        └── raw_data.csv       # Dados brutos retirados do site original
```

## 🚀 Como Rodar Localmente
Siga os passos abaixo para configurar o ambiente e executar o projeto em sua máquina.

### 1. Preparar o Ambiente:
É altamente recomendável criar um ambiente virtual para isolar as dependências do projeto. Abra o seu terminal na pasta raiz do projeto e execute:

#### Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Linux/macOS
```sh
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Dependências
Com o ambiente virtual ativo, instale todas as bibliotecas necessárias (como streamlit, pandas e plotly) listadas no arquivo de requisitos:

```bash
pip install -r requirements.txt
``` 

### 3. Executar o Dashboard
Para iniciar a aplicação, utilize o comando do Streamlit apontando para o arquivo principal. Baseado na estrutura do projeto, o arquivo app.py está dentro da pasta dashboard_camisetas:

```bash
streamlit run dashboard_camisetas/app.py
```
O navegador abrirá automaticamente no endereço local.