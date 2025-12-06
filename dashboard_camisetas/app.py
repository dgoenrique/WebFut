import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Gestão de Estoque - Camisas", layout="wide")

# --- 1. CARREGAMENTO E TRATAMENTO ---
@st.cache_data
def load_data():
    # Carrega os dados
    df = pd.read_csv('data/data_camisetas.csv')
    
    # CORREÇÃO DO ERRO: Removemos linhas onde o nome da camisa está vazio
    df = df.dropna(subset=['nome'])
    
    # Tratamento de Ano
    def extrair_ano(temp):
        if pd.isna(temp): return None
        try:
            return int(str(temp)[:4])
        except:
            return None

    df['ano_inicial'] = df['temporada'].apply(extrair_ano)
    
    # Criar coluna de Década
    def definir_decada(ano):
        if pd.isna(ano): return "Indefinido"
        if ano >= 2020: return "2020 - Atual"
        if ano >= 2010: return "2010 - 2019"
        if ano >= 2000: return "2000 - 2009"
        if ano < 2000: return "Retrô (Anos 90 ou antes)"
        return "Indefinido"

    df['decada'] = df['ano_inicial'].apply(definir_decada)
    
    # Criar Faixa de Preço
    def faixa_preco(preco):
        if pd.isna(preco): return "Indefinido" # Segurança extra
        if preco < 200: return "Até R$ 200"
        if preco < 250: return "R$ 200 - R$ 250"
        return "Premium (> R$ 250)"

    df['categoria_preco'] = df['preço'].apply(faixa_preco)
    
    # Padronizar nomes (Título) e Tipos
    df['nome'] = df['nome'].astype(str).str.title() # Força tudo virar texto
    df['tipo'] = df['tipo'].str.capitalize().fillna("Outros")
    
    return df

# Carrega os dados tratados
df = load_data()

# --- 2. SIDEBAR (FILTROS) ---
st.sidebar.header("Filtros de Estoque")

# Filtro de Times
times = sorted(df['nome'].unique())
time_selecionado = st.sidebar.multiselect("Filtrar por Time", times)

# Filtro de Tipo
tipos = df['tipo'].dropna().unique()
tipo_selecionado = st.sidebar.multiselect("Tipo de Kit", tipos, default=tipos)

if time_selecionado and tipo_selecionado:
    df_filtered = df[(df['nome'].isin(time_selecionado)) & (df['tipo'].isin(tipo_selecionado))]
elif time_selecionado:
    df_filtered = df[df['nome'].isin(time_selecionado)]
elif tipo_selecionado:
    df_filtered = df[df['tipo'].isin(tipo_selecionado)]
else:
    df_filtered = df

# --- 3. DASHBOARD ---
st.title("👕 WebFut - Painel de Gestão de Loja")
st.markdown("Visão geral do inventário e valor potencial de venda.")

# KPIs
total_itens = len(df_filtered)
valor_total_estoque = df_filtered['preço'].sum()
ticket_medio = df_filtered['preço'].mean()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Itens em Estoque", total_itens)
col2.metric("Valor Total do Estoque", f"R$ {valor_total_estoque:,.2f}")
col3.metric("Ticket Médio", f"R$ {ticket_medio:.2f}")
col4.metric("Mais Cara", f"R$ {df_filtered['preço'].max():.2f}")
col5.metric("Mais Barata", f"R$ {df_filtered['preço'].min():.2f}")

st.divider()

# --- GRÁFICOS VISUAIS ---

col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("1. Composição do Estoque")
    # Treemap
    if not df_filtered.empty:
        df_tree = df_filtered.groupby(['nome', 'tipo']).size().reset_index(name='quantidade')
        fig_tree = px.treemap(df_tree, path=['nome', 'tipo'], values='quantidade',
                              color='nome', 
                              title="Distribuição: Time > Tipo de Kit")
        fig_tree.update_layout(margin=dict(t=30, l=0, r=0, b=0))
        st.plotly_chart(fig_tree, use_container_width=True)
    else:
        st.warning("Sem dados para exibir com esses filtros.")

with col_dir:
    st.subheader("2. Valor Financeiro por Time")
    # Gráfico de Barras
    if not df_filtered.empty:
        df_valor = df_filtered.groupby('nome')['preço'].sum().reset_index()
        df_valor = df_valor.sort_values(by='preço', ascending=True).tail(10)
        
        fig_bar = px.bar(df_valor, x='preço', y='nome', text_auto='.2s',
                         title="Top 10 Times (Valor R$)",
                         orientation='h', color='preço', color_continuous_scale='Blugrn')
        fig_bar.update_layout(xaxis_title="Valor Total (R$)", yaxis_title=None)
        st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.subheader("3. Perfil de Época")
    # Gráfico de Rosca
    if not df_filtered.empty:
        df_decada = df_filtered['decada'].value_counts().reset_index()
        df_decada.columns = ['Década', 'Quantidade']
        
        fig_pie = px.pie(df_decada, names='Década', values='Quantidade', hole=0.4,
                         color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig_pie, use_container_width=True)

with col4:
    st.subheader("4. Faixas de Preço")
    # Gráfico de Colunas
    if not df_filtered.empty:
        df_cat = df_filtered['categoria_preco'].value_counts().reset_index()
        df_cat.columns = ['Categoria', 'Quantidade']
        ordem = ["Até R$ 200", "R$ 200 - R$ 250", "Premium (> R$ 250)"]
        
        fig_col = px.bar(df_cat, x='Categoria', y='Quantidade', color='Categoria',
                         category_orders={"Categoria": ordem})
        st.plotly_chart(fig_col, use_container_width=True)