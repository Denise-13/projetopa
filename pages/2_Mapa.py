import streamlit as st
import plotly.express as px
import json
import pandas as pd
from dados_sidra import carregar_dados_sidra

st.set_page_config(layout="wide")
st.subheader("🗺️ Mapa do Coeficiente de Variação - Uso da Internet (Censo 2022)")

@st.cache_data
def get_pop():
    return carregar_dados_sidra()

pop = get_pop()['final']

# --- Carrega o GeoJSON ---
with open("geojson_regioes_2022.json", encoding="utf-8") as f:
    geo_json = json.load(f)

# --- Cria o mapa fixo com COEF_VARIACAO ---
fig = px.choropleth_mapbox(
    data_frame=pop,
    geojson=geo_json,
    locations='COD_REG',
    featureidkey='properties.codarea',
    color='COEF_VARIACAO',
    color_continuous_scale='thermal',
    range_color=(pop['COEF_VARIACAO'].min(), pop['COEF_VARIACAO'].max()),
    mapbox_style='open-street-map',
    zoom=3.5,
    center={"lat": -15.81, "lon": -47.93},
    opacity=1,
    labels={
        'COEF_VARIACAO': 'Coeficiente de Variação (%)',
        'COD_REG': 'Código da Região'
    },
    width=1200,
    height=800,
    hover_name='NOME_REG',
)

# --- Layout e estilo ---
fig.update_layout(
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
    coloraxis_colorbar={
        'title': {'text': 'Coef. Variação (%)', 'side': 'right'}
    }
)
fig.update_traces(marker_line_width=0.2, selector=dict(type='choroplethmapbox'))

# --- Mostra o gráfico ---
st.plotly_chart(fig, use_container_width=True)

# --- Salvar localmente (opcional) ---
#fig.write_html("mapa_coef_variacao.html")
#fig.write_image("mapa_coef_variacao.png")



