import streamlit as st
import pandas as pd
from views import View
import time

class Cadastrar_seUI:
  def main():
    st.header("Abrir Conta no Sistema")
    Cadastrar_seUI.abrir_conta()
    
  def abrir_conta():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe seu telefone")
        senha = st.text_input("Crie uma senha")
        if st.button("Inserir"):
            View.usuario_inserir(nome, email, fone, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()