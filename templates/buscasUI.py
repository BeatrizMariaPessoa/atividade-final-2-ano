import streamlit as st
import time

class BuscasUI:
    def main():
        st.header("Buscas")
        BuscasUI.buscas()
    def buscas():
        tab1, tab2, tab3 = st.tabs(["País","Estado","Cidade"])
        with tab1:
            st.header("Buscar país")
            opcao = st.selectbox('Escolha um país',('Bolivia','Brasil','China','Opção genérica'))
            st.write('País selecionado:', opcao)
            if st.button("Ver informações do país"):
                st.success('')
                time.sleep(2)
                st.rerun()
        with tab2:
            st.header("Buscar estado")
            es = st.selectbox('Escolha o estado',('op1','op2','op3'))
            st.write('País selecionado:', opcao)
            st.write('Estado selecionado:', es)
            if st.button("Ver informações do estado"):
                st.success('')
                time.sleep(2)
                st.rerun()
        with tab3:
            st.header("Buscar estado")
            cid = st.selectbox('Escolha a cidade',('op1','op2','op3'))
            st.write('País selecionado:', opcao)
            st.write('Estado selecionado:', es)
            st.write('Cidade selecionada:', cid)
            if st.button("Ver informações da cidade"):
                st.success('')
                time.sleep(2)
                st.rerun()
BuscasUI.main()
        