import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome,dt_nasc, tipo_cliente):
    if nome and dt_nasc <= date.today():
        with open ("clientes.csv","a",encoding="utf-8") as file:
            file.write(f"{nome},{dt_nasc}, {tipo_cliente}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de Clientes", 
    page_icon="📕"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente: ",
                     key="nome_cliente")

dt_nasc = st.date_input("Data de Nascimento:", format="DD/MM/YYYY")

tipo_cliente = st.selectbox("Tipo do cliente",
                            ["Pessoa Jurídica", "Pessoa Física"])

btn_cadastrar = st.button("Cadastrar", 
                          on_click=gravar_dados,
                          args=[nome,dt_nasc, tipo_cliente])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success ("Cliente Cadastrado com Sucesso!",
                    icon="✅")
    else: 
        st.error("Houve algum problema no Cadastro! ",
                 icon="❌")