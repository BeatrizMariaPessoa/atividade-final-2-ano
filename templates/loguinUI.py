import streamlit as st
from views import View
import time

class LoginUI:
  def main():
    st.header("Faça o login com seu e-mail e senha")
    LoginUI.entrar()
  def entrar():
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Login"):
      user = View.usuario_login(email, senha)
      if user is not None:
        st.success("Login realizado com sucesso")
        st.success("Bem-vindo(a), " + user.get_nome())
        st.session_state["Usuario_id"] = user.get_id()
        st.session_state["Usuario_nome"] = user.get_nome()
      else:
        st.error("Usuário ou senha inválido(s)")
      time.sleep(2)
      st.rerun()