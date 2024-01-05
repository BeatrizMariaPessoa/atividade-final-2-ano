import streamlit as st
import time
import pandas as pd
import numpy as np
from views import View

class ManterUsuarioUI:
  def main():
    st.header("Cadastro de usuarios")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterUsuarioUI.listar()
    with tab2: ManterUsuarioUI.inserir()
    with tab3: ManterUsuarioUI.atualizar()
    with tab4: ManterUsuarioUI.excluir()

  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      View.usuario_inserir(nome, email, fone, senha)
      st.success("usuario inserido com sucesso")
      time.sleep(2)
      st.rerun()
      
  def listar():
    usuarios = View.usuario_listar()
    if len(usuarios) == 0:
      st.write("Nenhum usuario cadastrado")
    else:
      dic = []
      for obj in usuarios: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def atualizar():
    usuarios = View.usuario_listar()
    if len(usuarios) == 0:
      st.write("Nenhum usuario cadastrado")
    else:
      op = st.selectbox("Atualização de usuarios", usuarios)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      email = st.text_input("Informe o novo e-mail", op.get_email())
      fone = st.text_input("Informe o novo fone", op.get_fone())
      senha = st.text_input("Informe a nova senha")
      if st.button("Atualizar"):
        id = op.get_id()
        View.usuario_atualizar(id, nome, email, fone, senha)
        st.success("usuario atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    usuarios = View.usuario_listar()
    if len(usuarios) == 0:
      st.write("Nenhum usuario cadastrado")
    else:
      op = st.selectbox("Exclusão de usuarios", usuarios)
      if st.button("Excluir"):
        id = op.get_id()
        View.usuario_excluir(id)
        st.success("usuario excluído com sucesso")
        time.sleep(2)
        st.rerun()