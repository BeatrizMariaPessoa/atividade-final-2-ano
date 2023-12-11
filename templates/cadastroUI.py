import streamlit as st
# import pandas as pd
# from views import View
import time

class Cadastrar_seUI:
  def main():
    st.header("Abrir Conta no Sistema")
    Cadastrar_seUI.abrir_conta()
    
  def abrir_conta():
        nome = st.text_input("Informe o nome")
        idade = st.text_input("Informe sua idade")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Crie uma senha")
        pais = st.text_input("Informe o país que você nasceu")
        estado = st.text_input("Informe o estado que você nasceu")
        cidade = st.text_input("Informe a cidade que você nasceu")
        st.text_input("Informe a senha")
        if st.button("Inserir"):
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()