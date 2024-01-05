import streamlit as st
import time
import pandas as pd
import numpy as np
from views import View

class ManterCidadeUI:
    def main():
        st.header("Cidade")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir","Listar","Atualizar","Excluir"])
        with tab1: ManterCidadeUI.Inserir()
        with tab2: ManterCidadeUI.Listar()
        with tab3: ManterCidadeUI.Atualizar()
        with tab4: ManterCidadeUI.Excluir()

    def Inserir():
        estados = View.estado_listar()
        estado = st.selectbox('Selecione o estado em que a cidade se localiza', estados)
        id_estado = estado.get_id()
        nome = st.text_input("Informe o nome da cidade")
        habitantes = st.number_input("Informe o número de habitantes")
        tamanho = st.number_input("Informe o tamanho da cidade(km²)")
        if st.button("Inserir"):
            View.cidade_inserir(id_estado, nome, habitantes, tamanho)
            st.success("Cidade inserida com sucesso.")
            time.sleep(2)
            st.rerun()

    def Listar():
        cidades = View.cidade_listar()
        if len(cidades) == 0:
            st.write("Nenhuma cidade cadastrada")
        else:
            dic = []
            for obj in cidades: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def Atualizar():
        cidades = View.cidade_listar()
        if len(cidades) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de cidades", cidades)
            id_estado = st.text_input("Informe o novo estado", op.get_id_estado())
            nome = st.text_input("Informe o novo nome", op.get_nome())
            habitantes = st.text_input("Informe o novo n° de habitantes", op.get_habitantes())
            tamanho = st.text_input("Informe o novo tamanho", op.get_tamanho())
            if st.button("Atualizar"):
                id = op.get_id()
                View.cliente_atualizar(id, id_estado, nome, habitantes, tamanho)
                st.success("Cidade atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def Excluir():
        cidades = View.cidade_listar()
        if len(cidades) == 0:
            st.write("Nenhuma cidade no banco de dados")
        else:
            op = st.selectbox("Exclusão de cidades", cidades)
            if st.button("Excluir"):
                id = op.get_id()
                View.cidade_escluir(id)
                st.success("Cidade excluída com sucesso")
                time.sleep(2)
                st.rerun()