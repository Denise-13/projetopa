import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Sistema de Visualização - IBGE",
    initial_sidebar_state="expanded"
)

# Exibir a logo do IBGE centralizada
st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <img src="https://imagensempng.com.br/wp-content/uploads/2023/05/274-1.png" alt="Logo IBGE" width="180"/>
    </div>
""", unsafe_allow_html=True)

# Estilo e estrutura continuam os mesmos
st.markdown("""
    <style>
    .titulo-principal {
        text-align: center;
        font-size: 3rem;
        color: #1f4e79;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .descricao {
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }
    .secao-cartoes {
        display: flex;
        justify-content: space-around;
        margin-top: 30px;
        margin-bottom: 30px;
    }
    .cartao {
        width: 30%;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.05);
        text-align: center;
        font-size: 1.05rem;
        font-weight: 500;
    }
    .graficos {
        background-color: #e0f7fa;
    }
    .mapa {
        background-color: #fff3e0;
    }
    .dados {
        background-color: #f3e8ff;
    }
    .titulo-cartao {
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .rodape {
        text-align: center;
        font-size: 0.9rem;
        color: gray;
        margin-top: 50px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='titulo-principal'>Sistema de Visualização de Dados - IBGE</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='descricao'>
        Este sistema interativo permite explorar de forma simples e visual os dados do <b>Censo 2022</b> com foco no <b>uso da internet</b> por região do Brasil.
        <br>Ideal para <b>profissionais</b>, <b>estudantes</b> e <b>curiosos</b> que desejam entender melhor os padrões de conectividade do país 📶.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='secao-cartoes'>
    <div class='cartao graficos'>
        <div class='titulo-cartao'>📈 Gráficos</div>
        Compare o número de usuários e variações entre regiões de forma visual e interativa.
    </div>
    <div class='cartao mapa'>
        <div class='titulo-cartao'>🗺️ Mapa Interativo</div>
        Veja como o acesso à internet está distribuído geograficamente no país.
    </div>
    <div class='cartao dados'>
        <div class='titulo-cartao'>⚙️ Tratamento de Dados</div>
        Veja os dados brutos e o processo de preparação para análise.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='rodape'>Fonte dos dados: IBGE - SIDRA | Desenvolvido por Denise 💜</div>", unsafe_allow_html=True)
