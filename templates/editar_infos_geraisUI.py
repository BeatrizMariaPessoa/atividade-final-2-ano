import streamlit as st
import time 

class EditarInfosUI:
    def main():
        st.header("Editar informações gerais de todas as classes")
        tab1, tab2, tab3 = st.tabs(["Editar Pais","Editar Estado","Editar Cidade"])
        with tab1: EditarInfosUI.editar_pais()
        with tab2: EditarInfosUI.editar_estado()
        with tab3: EditarInfosUI.editar_cidade()
    
    def editar_pais():
        pais = st.selectbox('Escolha um país',('Bolivia','Brasil','China','Opção genérica'))
        nome1 = st.text_input("Insira o novo Nome")
        habitantes1 = st.text_input("Insira a nova quantidade de habitantes do país")
        tamanho1 = st.text_input("Insira o novo tamanho do país")
        moeda1 = st.text_input("Insira a nova moeda do país")
        idioma1 = st.text_input("Insira o novo idioma do país")
        fuso = st.text_input("Insira o novo fuso-horário do país")
        capital = st.text_input("Insira a nova capital do país")
        if st.button("Editar dados do país"):
            st.success('Dados do país atualizados com sucesso!')
            time.sleep(2)
            st.rerun()
    def editar_estado():
        es = st.selectbox('Escolha o estado',('op1','op2','op3'))
        nome = st.text_input("Insira o novo Nome do estado")
        habitantes = st.text_input("Insira a nova quantidade de habitantes do estado")
        tamanho = st.text_input("Insira o novo tamanho do estado")
        capital = st.text_input("Insira a nova capital do estado")
        municipios = st.text_input("Insira a nova quantidade de municipios do estado")
        if st.button("Editar dados do Estado"):
            st.success('Dados do estado atualizados com sucesso!')
            time.sleep(2)
            st.rerun()
    def editar_cidade():
        cid = st.selectbox('Escolha a cidade',('op1','op2','op3'))
        nome = st.text_input("Insira o novo Nome da cidade")
        habitantes = st.text_input("Insira a nova quantidade de habitantes da cidade")
        tamanho = st.text_input("Insira o novo tamanho da cidade")
        if st.button("Editar dados da cidade"):
            st.success('Dados da cidade atualizados com sucesso!')
            time.sleep(2)
            st.rerun()