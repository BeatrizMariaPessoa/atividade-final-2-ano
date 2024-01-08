import streamlit as st
from views import View
import time

class CompararCidadesUI:
    def main():
        st.header("Comparar dados")
        CompararCidadesUI.comparar_cidadesUI()
    
    def comparar_cidadesUI():
        paises = View.pais_listar()
        pais = st.selectbox('Escolha o país', paises)
        pais_id = pais.get_id()
        estados = View.listar_estados(pais_id)
        if len(estados) == 0:
            st.write("nenhum estado desse país foi cadastrado")
        else:
            estado = st.selectbox('Escolha o estado', estados)
            estado_id = estado.get_id()
            cidades = View.listar_cidades(estado_id)
            if len(cidades) == 0:
                st.write("nenhuma cidade desse estado foi cadastrada")
            else:
                opcao1 = st.selectbox('Escolha a primeira cidade', cidades)
                opcao2 = st.selectbox('Escolha a segunda cidade', cidades)
                maior_tamanho = View.comparar_tamanho(opcao1.get_tamanho(), opcao1.get_nome(), opcao2.get_nome(), opcao2.get_tamanho())
                maior_hab = View.comparar_habitantes(opcao1.get_habitantes(), opcao2.get_habitantes(), opcao1.get_nome(), opcao2.get_nome())
                if st.button("Comparar"):
                    st.write(maior_tamanho)
                    st.write(maior_hab)
                    time.sleep(2)
