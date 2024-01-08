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
        paise = View.pais_listar()
        pais = st.selectbox('Escolha um país', paise)
        id_pais = pais.get_id()
        nome = st.text_input("Informe o nome")
        habitantes = st.number_input("Informe o número de habitantes")
        tamanho = st.number_input("Informe o tamanho do estado(km)")
        capital = st.text_input("Informe qual a capital do estado")
        municipios = st.number_input("Informe a quantidade de municipios")
        if st.button("Inserir"):
            View.estado_inserir(0,id_pais, nome, habitantes, tamanho, capital, municipios)
            st.success("Estado inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def Listar():
        estados = View.estado_listar()
        if len(estados) == 0:
            st.write("Nenhum estado cadastrado")
        else:  
            dic = [{"ID Estado": estado.get_id(), "ID País": estado.get_id_pais(), "Nome": estado.get_nome(), "Habitantes" : estado.get_habitantes(), "Tamanho": estado.get_tamanho(), "Capital" : estado.get_capital(), "Municípios" : estado.get_municipios()} for estado in estados]
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def Atualizar():
        estados = View.estado_listar()
        if len(estados) == 0:
            st.write("Nenhum estado cadastrado")
        else:
            op = st.selectbox("Atualização de Estado", estados)
            id_pais = op.get_id_pais()
            nome = st.text_input("Informe o novo nome", op.get_nome())
            habitantes = st.number_input("Informe o novo número de habitantes", op.get_habitantes())
            tamanho = st.number_input("Informe o novo tamanho do estado(km²)", op.get_tamanho())
            capital = st.text_input("Informe qual a nova capital do estado", op.get_capital())
            municipios = st.number_input("Informe a nova quantidade de municipios", op.get_municipios())
            if st.button("Atualizar"):
                id = op.get_id()
                View.estado_atualizar(id, id_pais, nome, habitantes, tamanho, capital, municipios)
                st.success('Estado atualizado com sucesso.')
                time.sleep(2)
                st.rerun()

    def Excluir():
        estados = View.estado_listar()
        if len(estados) == 0:
            st.write("Nenhum estado cadastrado")
        else:
            op = st.selectbox("Exclusão de Estados", estados)
            if st.button("Excluir"):
                id = op.get_id()
                View.estado_escluir(id)
                st.success("Estado excluído com sucesso")
                time.sleep(2)
                st.rerun()