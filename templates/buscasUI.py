import streamlit as st
import time
from views import View

class BuscasUI:
    def main():
        st.header("Buscas")
        BuscasUI.buscas()
    def buscas():
        tab1, tab2, tab3 = st.tabs(["País","Estado","Cidade"])

        with tab1:
            st.header("Buscar país")
            nome = st.text_input("Informe o nome do país")
            if st.button("Buscar o país"):
                pais = View.buscar_pais(nome)
                if pais == None:
                    st.write("País não encontrado")
                else:
                    st.write(pais)
        with tab2:
            st.header("Buscar estado")
            nome = st.text_input("Informe o nome do estado")
            if st.button("Buscar o estado"):
                estado = View.buscar_estado(nome)
                if estado == None:
                    st.write("País não encontrado")
                else:
                    st.write(estado)
        with tab3:
            st.header("Buscar cidade")
            nome = st.text_input("Informe o nome da cidade")
            if st.button("Buscar a cidade"):
                cidade = View.buscar_cidade(nome)
                if cidade == None:
                    st.write("Cidade não encontrada")
                else:
                    st.write(cidade)
