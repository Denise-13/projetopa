# tratamento_de_Dados.py
import streamlit as st

import sys
import os
sys.path.append(os.path.dirname(__file__))  # Adiciona a pasta atual (pages/) ao path

from dados_sidra import carregar_dados_sidra

st.set_page_config(page_title="Etapas do Tratamento - SIDRA", layout="wide")
st.title("📊 Tratamento de Dados - Censo 2022 (SIDRA IBGE)")

# Carrega os dados tratados por etapa
dados = carregar_dados_sidra()

# Etapa 1: Bruto
st.subheader("🟡 Etapa 1: Dados brutos do SIDRA")
st.write(f"🔢 {dados['bruto'].shape[0]} linhas × {dados['bruto'].shape[1]} colunas")
st.dataframe(dados['bruto'].head(10), use_container_width=True)

# Etapa 2: Sem acentos
st.subheader("🟡 Etapa 2: Remoção de acentos")
st.dataframe(dados['sem_acentos'].head(10), use_container_width=True)

# Etapa 3: Remoção da primeira linha
st.subheader("🟡 Etapa 3: Remoção de linha com rótulos duplicados")
st.dataframe(dados['sem_header'].head(10), use_container_width=True)

# Etapa 4: Conversão para numérico
st.subheader("🟡 Etapa 4: Conversão da coluna 'V' para numérica")
st.dataframe(dados['sem_header'][['V']].head(10), use_container_width=True)

# Etapa 5: Tabela pivotada
st.subheader("🟡 Etapa 5: Dados reorganizados (pivotados)")
st.dataframe(dados['pivotado'].head(10), use_container_width=True)

# Etapa 6: Colunas renomeadas
st.subheader("🟡 Etapa 6: Colunas renomeadas")
st.dataframe(dados['renomeado'].head(10), use_container_width=True)

# Etapa 7: Tipos convertidos (final)
st.subheader("✅ Etapa 7: Dados prontos para uso (tratados)")
st.write(f"✅ {dados['final'].shape[0]} linhas × {dados['final'].shape[1]} colunas")
st.dataframe(dados['final'].head(10), use_container_width=True)
