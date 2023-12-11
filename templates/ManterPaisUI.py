import streamlit as st
import time
import pandas as pd
import numpy as np

class ManterPaisUI:
    def main():
        st.header("País")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir","Listar","Atualizar","Excluir"])
        with tab1: ManterPaisUI.Inserir()
        with tab2: ManterPaisUI.Listar()
        with tab3: ManterPaisUI.Atualizar()
        with tab4: ManterPaisUI.Excluir()

    def Inserir():
        nome = st.text_input("Informe o nome")
        habitantes = st.number_input("Informe o número de habitantes")
        tamanho = st.number_input("Informe o tamanho do país(km²)")
        moeda = st.text_input("Informe o nome da moeda")
        idioma = st.text_input("Informe o idioma")
        fuso_horario = st.number_input("Informe o fuso horário")
        capital = st.text_input("Informe qual a capital do país")
        if st.button("Inserir"):
            st.success("País inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def Listar():
        @st.cache_data
        def load_data():
            return pd.DataFrame(
            {
                "Nome": ['Brasil','EUA'],
                "Moeda": ['BRL','USD'],
                "Idioma": ['Português','Inglês'],
                "Fuso Horário": ['-3','-7'],
                "Capital": ['Brasília','Washington'],
            }
        )
        st.checkbox("Use container width", value=False, key="use_container_width")
        df = load_data()
        st.dataframe(df, use_container_width=st.session_state.use_container_width)

    def Atualizar():
        ids = st.selectbox('Selecione o id do país a ser atualizado',(0,1,2,3,4))
        nome = st.text_input("Novo nome")
        habitantes = st.number_input("Informe o novo número de habitantes")
        tamanho = st.number_input("Informe o novo tamanho do país(km²)")
        moeda = st.text_input("Informe o novo nome da moeda")
        idioma = st.text_input("Informe novo idioma")
        capital = st.text_input("Informe qual a nova capital do país")
        if st.button("Atualizar"):
            st.success('País atualizado com sucesso.')
            time.sleep(2)
            st.rerun()

    def Excluir():
        nomes = st.selectbox('Selecione o nome do país a ser excluído',('Brasil','EUA','Inglaterra','Alemanha'))
        if st.button("Excluir"):
            st.success('País excluído com sucesso.')
            time.sleep(2)
            st.rerun()