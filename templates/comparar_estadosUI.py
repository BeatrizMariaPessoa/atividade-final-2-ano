import streamlit as st
from views import View
import time


class CompararEstadosUI:
    def main():
        st.header("Comparar dados")
        CompararEstadosUI.comparar_estadosUI()
    


    def comparar_estadosUI():
        paises = View.pais_listar()
        pais = st.selectbox('Escolha o país', paises)
        pais_id = pais.get_id()
        estados = View.listar_estados(pais_id)
        opcao1 = st.selectbox('Escolha o primeiro estado', estados)
        opcao2 = st.selectbox('Escolha o segundo estado', estados)
        maior_tamanho = View.comparar_tamanho(opcao1.get_tamanho(), opcao1.get_nome(), opcao2.get_nome(), opcao2.get_tamanho())
        maior_hab = View.comparar_habitantes(opcao1.get_habitantes(), opcao2.get_habitantes(), opcao1.get_nome(), opcao2.get_nome())
        if st.button("Comparar"):
            st.write(maior_tamanho)
            st.write(maior_hab)
            st.success("")
            time.sleep(2)