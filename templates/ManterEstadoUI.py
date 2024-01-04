import streamlit as st
import time
import pandas as pd
import numpy as np
from views import View

class ManterEstadoUI:
    def main():
        st.header("Estado")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir","Listar","Atualizar","Excluir"])
        with tab1: ManterEstadoUI.Inserir()
        with tab2: ManterEstadoUI.Listar()
        with tab3: ManterEstadoUI.Atualizar()
        with tab4: ManterEstadoUI.Excluir()

    def Inserir():
        # TA ERRADO E PRECISA CONCERTAR
        paises = View.pais_listar
        pais = st.selectbox('Escolha um país',())
        nome = st.text_input("Informe o nome")
        habitantes = st.number_input("Informe o número de habitantes")
        tamanho = st.number_input("Informe o tamanho do estado(km)")
        capital = st.text_input("Informe qual a capital do estado")
        municipios = st.number_input("Informe a quantidade de municipios")
        if st.button("Inserir"):
            View.estado_inserir(0, id_pais)
            st.success("Estado inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def Listar():
        @st.cache_data
        def load_data():
            return pd.DataFrame(
            {

                "Nome": ['op1','op2'],
                "Habitantes": ['2','6'],
                "Tamanho": ['10','20'],
                "Qnt. de Municipios": ['3','7'],
                "Capital": ['Brasília','Washington'],
            }
        )
        st.checkbox("Use container width", value=False, key="use_container_width")
        df = load_data()
        st.dataframe(df, use_container_width=st.session_state.use_container_width)

    def Atualizar():
        ids = st.selectbox('Selecione o id do estado a ser atualizado',(0,1,2,3,4))
        nome = st.text_input("Novo nome")
        habitantes = st.number_input("Informe o novo número de habitantes")
        tamanho = st.number_input("Informe o novo tamanho do estado(km)")
        capital = st.text_input("Informe qual a nova capital do estado")
        municipios = st.number_input("Informe a nova quantidade de municipios")
        if st.button("Atualizar"):
            st.success('Estado atualizado com sucesso.')
            time.sleep(2)
            st.rerun()

    def Excluir():
        nomes = st.selectbox('Selecione o nome do estado a ser excluído',('op1','op2','op3','op4'))
        if st.button("Excluir"):
            st.success('estado excluído com sucesso.')
            time.sleep(2)
            st.rerun()