import streamlit as st
import time
import pandas as pd
import numpy as np

class ManterCidadeUI:
    def main():
        st.header("Cidade")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir","Listar","Atualizar","Excluir"])
        with tab1: ManterCidadeUI.Inserir()
        with tab2: ManterCidadeUI.Listar()
        with tab3: ManterCidadeUI.Atualizar()
        with tab4: ManterCidadeUI.Excluir()

    def Inserir():
        estado = st.selectbox('Selecione o estado em que a cidade se localiza', ('Amazonas','Rio Grande do Norte','São Paulo'))
        nome = st.text_input("Informe o nome da cidade")
        habitantes = st.number_input("Informe o número de habitantes")
        tamanho = st.number_input("Informe o tamanho da cidade(km²)")
        if st.button("Inserir"):
            st.success("Cidade inserida com sucesso.")
            time.sleep(2)
            st.rerun()

    def Listar():
        @st.cache_data
        def load_data():
            return pd.DataFrame(
            {
                "Nome": ['Manaus','Natal'],
                "Habitantes": [2020000, 890400],
                "Tamanho(km²)": [11401, 167.4],
                "Estado": ['Amazonas','Rio Grande do Norte']
            }
        )
        st.checkbox("Use container width", value=False, key="use_container_width")
        df = load_data()
        st.dataframe(df, use_container_width=st.session_state.use_container_width)

    def Atualizar():
        ids = st.selectbox('Selecione o id da cidade a ser atualizada',(0,1,2,3,4))
        nome = st.text_input("Novo nome")
        habitantes = st.number_input("Informe o novo número de habitantes")
        tamanho = st.number_input("Informe o novo tamanho da cidade(km²)")
        if st.button("Atualizar"):
            st.success('Dados atualizados com sucesso.')
            time.sleep(2)
            st.rerun()

    def Excluir():
        nomes = st.selectbox('Selecione o nome da cidade a ser excluída',('Manaus','Natal','São Paulo'))
        if st.button("Excluir"):
            st.success('Cidade excluída com sucesso.')
            time.sleep(2)
            st.rerun()