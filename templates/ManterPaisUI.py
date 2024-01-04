import streamlit as st
import time
import pandas as pd
import numpy as np
from views import View
from models.modelo import Modelo

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
        capital = st.text_input("Informe a capital do país")
        if st.button("Inserir"):
            View.pais_inserir(0, nome, habitantes, tamanho, moeda, idioma, fuso_horario, capital)
            st.success("País inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def Listar():
        paises = View.pais_listar()
        if len(paises) == 0:
            st.write("Nenhum país cadastrado")
        else:
            dic = []
            for obj in paises: 
                id = obj.get_id()
                nome = obj.get_nome()
                habitantes = obj.get_habitantes()
                tamanho = obj.get_tamanho()
                moeda = obj.get_moeda()
                idioma = obj.get_idioma()
                fuso_horario = obj.get_fuso_horario()
                capital = obj.get_capital()
                dic.append([id, nome, habitantes, tamanho, moeda, idioma, fuso_horario, capital])
            df = pd.DataFrame(dic, columns=['id','Nome','Habitantes','Tamanho','Moeda','Idioma','Fuso Horário','Capital'])
            st.dataframe(df)

    def Atualizar():
        paises = View.pais_listar()
        if len(paises) == 0:
            st.write("Nenhum país cadastrado")
        else:
            op = st.selectbox("Atualização de Paises", paises)

            nome = st.text_input("Informe o novo nome", op.get_nome())
            habitantes = st.number_input("Informe o novo número de habitantes", op.get_habitantes())
            tamanho = st.number_input("Informe o novo tamanho do país(km²)", op.get_tamanho())
            moeda = st.text_input("Informe o novo nome da moeda", op.get_moeda())
            idioma = st.text_input("Informe novo idioma", op.get_idioma())
            fuso_horario = op.get_fuso_horario()
            capital = st.text_input("Informe qual a nova capital do país", op.get_capital())
            if st.button("Atualizar"):
                id = op.get_id()
                View.pais_atualizar(id, nome, habitantes, tamanho, moeda, idioma,fuso_horario, capital)
                st.success("País atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def Excluir():
        paises = View.pais_listar()
        if len(paises) == 0:
            st.write("Nenhum país cadastrado")
        else:
            op = st.selectbox("Exclusão de paises", paises)
            if st.button("Excluir"):
                id = op.get_id()
                View.pais_excluir(id)
                st.success("País excluído com sucesso")
                time.sleep(2)
                st.rerun()