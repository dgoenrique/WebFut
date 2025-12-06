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