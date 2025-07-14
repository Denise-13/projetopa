'''import streamlit as st
import pandas as pd
import sidrapy

st.set_page_config(layout="wide")
st.title("Dados do Censo 2022 - SIDRA IBGE")

# Carregar dados com cache
@st.cache_data
def carregar_dados_sidra():
    pop = sidrapy.get_table(
        table_code='7388',
        territorial_level='2',       # 2 = regiões, 1 = UF,
        ibge_territorial_code='all',
        period='all',
        variable='all',
       
    )
    return pop







# Obter os dados
pop = carregar_dados_sidra()

# Mostrar tamanho
st.write(f"Tamanho do DataFrame: {pop.shape[0]} linhas e {pop.shape[1]} colunas")

# Mostrar as primeiras linhas
st.subheader("Prévia dos Dados")
st.dataframe(pop.head(20))  # mostra só os 20 primeiros para não pesar

# Removendo acentos
pop = pop.apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8') if x.dtype == 'object' else x) 
# Removendo primeira linha
pop = pop.iloc[1:]

pop.head()


# Mostrar tamanho
st.write(f"Tamanho do DataFrame: {pop.shape[0]} linhas e {pop.shape[1]} colunas")

# Mostrar as primeiras linhas
st.subheader("Prévia dos Dados")
st.dataframe(pop.head(20))  # mostra só os 20 primeiros para não pesar

pop['V'] = pd.to_numeric(pop['V'], errors='coerce') #Garantir que a coluna V seja numérica

# Pivotando tabela
pop = pop.pivot_table(index=['D1C', 'D1N'], columns='D3N', values='V').reset_index()
pop.columns.name = None



# Mostrar tamanho
st.write(f"Tamanho do DataFrame: {pop.shape[0]} linhas e {pop.shape[1]} colunas")

# Mostrar as primeiras linhas
st.subheader("Prévia dos Dados")
st.dataframe(pop.head(20))  # mostra só os 20 primeiros para não pesar


# Dict mapeamento nomes das colunas
column_mapping = {
    'D1C': 'COD_REG',
    'D1N': 'NOME_REG',
    'Coeficiente de variacao - Pessoas de 10 anos ou mais de idade que utilizaram Internet no periodo de referencia dos ultimos tres meses': 'COEF_VARIACAO',
    'Percentual de pessoas de 10 anos ou mais de idade que utilizaram Internet no periodo de referencia dos ultimos tres meses': 'USO_3MESES%',
    'Pessoas de 10 anos ou mais de idade que utilizaram Internet no periodo de referencia dos ultimos tres meses': 'NUM_PESSOAS_USO_3MESES'
}

# Renomeando colunas
pop.rename(columns=column_mapping, inplace=True)

# Mostrar tamanho
st.write(f"Tamanho do DataFrame: {pop.shape[0]} linhas e {pop.shape[1]} colunas")

# Mostrar as primeiras linhas
st.subheader("Prévia dos Dados")
st.dataframe(pop.head(20))  # mostra só os 20 primeiros para não pesar

# Tratando tipos das colunas
pop[['COD_REG', 'NUM_PESSOAS_USO_3MESES']] = pop[['COD_REG', 'NUM_PESSOAS_USO_3MESES']].astype(int)
pop[['COEF_VARIACAO', 'USO_3MESES%']] = pop[['COEF_VARIACAO', 'USO_3MESES%']].astype(float) #/ 100  # Deixar como porcentagem por enquanto, fica mais fácil para visualizar no mapa

pop.head()

# Mostrar tamanho
st.write(f"Tamanho do DataFrame: {pop.shape[0]} linhas e {pop.shape[1]} colunas")

# Mostrar as primeiras linhas
st.subheader("Prévia dos Dados")
st.dataframe(pop.head(20))''' # mostra só os 20 primeiros para não pesar



'''------------------------------------------------------------------------------------------------------------------------------'''

'''import streamlit as st
import pandas as pd
import sidrapy

def carregar_dados_sidra():
    pop = sidrapy.get_table(
        table_code='7388',
        territorial_level='2',  # 2 = regiões
        ibge_territorial_code='all',
        period='all',
        variable='all',
    )
    
    # Limpeza e tratamento
    pop = pd.DataFrame(pop)
    pop = pop.apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8') if x.dtype == 'object' else x) 
    pop = pop.iloc[1:]
    pop['V'] = pd.to_numeric(pop['V'], errors='coerce')
    pop = pop.pivot_table(index=['D1C', 'D1N'], columns='D3N', values='V').reset_index()

    #Mostrar tamanho
    st.write(f"Tamanho do DataFrame: {pop.shape[0]} linhas e {pop.shape[1]} colunas")

    #Mostrar as primeiras linhas
    st.subheader("Prévia dos Dados")
    st.dataframe(pop.head(20))  # mostra só os 20 primeiros para não pesar

    pop.columns.name = None

    column_mapping = {
        'D1C': 'COD_REG',
        'D1N': 'NOME_REG',
        'Coeficiente de variacao - Pessoas de 10 anos ou mais de idade que utilizaram Internet no periodo de referencia dos ultimos tres meses': 'COEF_VARIACAO',
        'Percentual de pessoas de 10 anos ou mais de idade que utilizaram Internet no periodo de referencia dos ultimos tres meses': 'USO_3MESES%',
        'Pessoas de 10 anos ou mais de idade que utilizaram Internet no periodo de referencia dos ultimos tres meses': 'NUM_PESSOAS_USO_3MESES'
    }

    #Mostrar tamanho
    st.write(f"Tamanho do DataFrame: {pop.shape[0]} linhas e {pop.shape[1]} colunas")

    #Mostrar as primeiras linhas
    st.subheader("Prévia dos Dados")
    st.dataframe(pop.head(20))  # mostra só os 20 primeiros para não pesar

    pop.rename(columns=column_mapping, inplace=True)
    pop[['COD_REG', 'NUM_PESSOAS_USO_3MESES']] = pop[['COD_REG', 'NUM_PESSOAS_USO_3MESES']].astype(int)
    pop[['COEF_VARIACAO', 'USO_3MESES%']] = pop[['COEF_VARIACAO', 'USO_3MESES%']].astype(float)

    #Mostrar tamanho
    st.write(f"Tamanho do DataFrame: {pop.shape[0]} linhas e {pop.shape[1]} colunas")

    #Mostrar as primeiras linhas
    st.subheader("Prévia dos Dados")
    st.dataframe(pop.head(20))  # mostra só os 20 primeiros para não pesar

    return pop'''


'''---------------------------------------------------------------------------------------------------------------------------------'''




# tratamento_dados.py
import pandas as pd
import sidrapy
import unicodedata

def carregar_dados_sidra():
    # Etapa 1: Download dos dados brutos
    df_raw = sidrapy.get_table(
        table_code='7388',
        territorial_level='2',
        ibge_territorial_code='all',
        period='all',
        variable='all'
    )
    df_raw = pd.DataFrame(df_raw)

    # Etapa 2: Remoção de acentos
    df_no_accents = df_raw.copy()
    df_no_accents = df_no_accents.apply(
        lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8') 
        if x.dtype == 'object' else x
    )

    # Etapa 3: Remoção da primeira linha (rótulo duplicado do SIDRA)
    df_no_header = df_no_accents.iloc[1:].copy()

    # Etapa 4: Conversão da coluna 'V' para numérico
    df_no_header['V'] = pd.to_numeric(df_no_header['V'], errors='coerce')

    # Etapa 5: Pivotagem (transformar variáveis em colunas)
    df_pivot = df_no_header.pivot_table(index=['D1C', 'D1N'], columns='D3N', values='V').reset_index()
    df_pivot.columns.name = None

    # Etapa 6: Renomear colunas para facilitar leitura
    column_mapping = {
        'D1C': 'COD_REG',
        'D1N': 'NOME_REG',
        'Coeficiente de variacao - Pessoas de 10 anos ou mais de idade que utilizaram Internet no periodo de referencia dos ultimos tres meses': 'COEF_VARIACAO',
        'Percentual de pessoas de 10 anos ou mais de idade que utilizaram Internet no periodo de referencia dos ultimos tres meses': 'USO_3MESES%',
        'Pessoas de 10 anos ou mais de idade que utilizaram Internet no periodo de referencia dos ultimos tres meses': 'NUM_PESSOAS_USO_3MESES'
    }
    df_renamed = df_pivot.rename(columns=column_mapping)

    # Etapa 7: Conversão de tipos
    df_final = df_renamed.copy()
    df_final[['COD_REG', 'NUM_PESSOAS_USO_3MESES']] = df_final[['COD_REG', 'NUM_PESSOAS_USO_3MESES']].astype(int)
    df_final[['COEF_VARIACAO', 'USO_3MESES%']] = df_final[['COEF_VARIACAO', 'USO_3MESES%']].astype(float)

    return {
        "bruto": df_raw,
        "sem_acentos": df_no_accents,
        "sem_header": df_no_header,
        "pivotado": df_pivot,
        "renomeado": df_renamed,
        "final": df_final
    }

