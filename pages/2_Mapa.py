import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import json
import pandas as pd

# Importa função de carregamento de dados já tratados
from dados_sidra import carregar_dados_sidra
st.set_page_config(layout="wide")
st.subheader("Mapa de Uso da Internet por Região - Censo 2022")

# Carrega os dados
@st.cache_data
def get_pop():
    return carregar_dados_sidra()

pop = get_pop()['final']


# Carrega o arquivo GeoJSON salvo localmente
with open("geojson_regioes_2022.json", encoding="utf-8") as f:
    geo_json = json.load(f)

# Criar o mapa coroplético com Plotly Express
fig = px.choropleth_mapbox(
    data_frame=pop,
    geojson=geo_json,
    locations='COD_REG',
    featureidkey='properties.codarea',
    color='USO_3MESES%',
    color_continuous_scale='thermal',
    range_color=(pop['USO_3MESES%'].min(), pop['USO_3MESES%'].max()),
    mapbox_style='open-street-map',
    zoom=3.5,
    center={"lat": -15.81, "lon": -47.93},
    opacity=1,
    labels={
        'USO_3MESES%': 'Uso da Internet (%)',
        'COD_REG': 'Código da Região'
    },
    width=1200,
    height=800,
    hover_name='NOME_REG',
)

# Customizar layout e bordas
fig.update_layout(
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
    coloraxis_colorbar={
        'title': {
            'text': 'Uso (%)',
            'side': 'right'
        }
    }
)
fig.update_traces(
    marker_line_width=0.2,
    selector=dict(type='choroplethmapbox')
)

# Mostrar no Streamlit
st.plotly_chart(fig, use_container_width=True)

# Salvar arquivos localmente
fig.write_html("uso_internet_regioes_2022.html")
fig.write_image("uso_internet_regioes_2022.png")


