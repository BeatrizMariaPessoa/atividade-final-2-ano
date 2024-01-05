import streamlit as st
from views import View
import time

class CompararPaisesUI:
    def main():
        st.header("Comparar dados")
        CompararPaisesUI.comparar_paisesUI()
    
    def comparar_paisesUI():
        paises = View.pais_listar()
        opcao1 = st.selectbox('Escolha o primeiro país', paises)
        opcao2 = st.selectbox('Escolha o segundo país', paises)
        maior_tamanho = View.comparar_tamanho(opcao1.get_tamanho(), opcao1.get_nome(), opcao2.get_nome(), opcao2.get_tamanho())
        maior_hab = View.comparar_habitantes(opcao1.get_habitantes(), opcao2.get_habitantes(), opcao1.get_nome(), opcao2.get_nome())
        if st.button("Comparar"):
            st.write(maior_tamanho)
            st.write(maior_hab)
            
            time.sleep(2)
            # st.rerun()
