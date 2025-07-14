import streamlit as st
import plotly.express as px
import pandas as pd

from dados_sidra import carregar_dados_sidra

st.set_page_config(layout="wide")
st.title("📊 Gráficos de Uso da Internet por Região - Censo 2022")

@st.cache_data
def get_data():
    return carregar_dados_sidra()

df = get_data()['final']

# --- Estilo CSS para aumentar tamanho da fonte dos botões ---
st.markdown("""
    <style>
    .stRadio > div {
        flex-direction: row;
    }
    div[role="radiogroup"] label {
        font-size: 30px !important;
        padding-right: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Botões de escolha ---
tipo_grafico = st.radio(
    "Escolha o tipo de gráfico:",
    ("👥 Nº de Pessoas", "🥧 Distribuição em Pizza", "📉 Coeficiente de Variação"),
    horizontal=True
)

# --- Gráfico 1 ---
if tipo_grafico == "👥 Nº de Pessoas":
    st.subheader("Pessoas que usaram Internet nos últimos 3 meses (por Região)")
    fig = px.bar(
        df,
        x='NOME_REG',
        y='NUM_PESSOAS_USO_3MESES',
        color='NOME_REG',
        text='NUM_PESSOAS_USO_3MESES',
        labels={'NUM_PESSOAS_USO_3MESES': 'Nº de Pessoas', 'NOME_REG': 'Região'},
        title="Nº de Pessoas com Acesso à Internet por Região",
    )
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

# --- Gráfico 2 ---
elif tipo_grafico == "🥧 Distribuição em Pizza":
    st.subheader("Distribuição Percentual de Pessoas com Acesso à Internet")
    fig = px.pie(
        df,
        names='NOME_REG',
        values='NUM_PESSOAS_USO_3MESES',
        title="Distribuição do Uso da Internet entre as Regiões"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Gráfico 3 ---
elif tipo_grafico == "📉 Coeficiente de Variação":
    st.subheader("Coeficiente de Variação do Uso da Internet por Região")
    fig = px.bar(
        df,
        x='COEF_VARIACAO',
        y='NOME_REG',
        orientation='h',
        text='COEF_VARIACAO',
        color='COEF_VARIACAO',
        labels={'COEF_VARIACAO': 'Coeficiente de Variação (%)', 'NOME_REG': 'Região'},
        title="Coeficiente de Variação por Região"
    )
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

