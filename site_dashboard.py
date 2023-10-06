import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Dashboards - Elotech")

# Decorator (annotation) sempre acima de uma função
# Este decorator serve para armazenar o CSV em cache, com isso não carrega a cada reload.
@st.cache_data
def carregar_dados():
  return pd.read_csv(".\\arquivos\\metricas.csv")

with st.container():
  st.subheader("Meu primeiro site com Streamlit")
  st.title("Dashboard - Elotech")
  st.write("Informações extraídas das ferramentas JIRA e Movidesk")
  st.write("Para mais informações, acessar o [JIRA](https://jira.elotech.com.br/) ou o [Movidesk](https://elotech.movidesk.com/)")

with st.container():
  st.write("---")

  metricas = carregar_dados()
  selectBox = st.selectbox("Selecione o mês de entrega", ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"
                                                          , "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
  st.area_chart(metricas, x="Done", y="Assignee")