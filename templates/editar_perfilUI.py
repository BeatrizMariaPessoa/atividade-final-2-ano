import streamlit as st
import time
from views import View

class EditarPerfilUI:
        def main():
             st.header("Edite os dados do seu perfil")
             EditarPerfilUI.mudar_dados()
        def mudar_dados():
            usuario = View.usuario_listar()
            if st.session_state["usuario_id"] == usuario[0].get_id():
                id = st.session_state["usuario_id"]
                email = st.text_input("Informe o novo e-mail")
                fone = st.text_input("Informe o novo telefone")
                senha = st.text_input("Informe a nova senha")
                if st.button("Mudar dados"):
                    View.editar_perfil(id, "Admin", email, fone, senha)
                    st.success("Dados do Admin atualizados com sucesso")
                    time.sleep(2)
                    st.rerun()
            else:
                id = st.session_state["usuario_id"]
                nome = st.text_input("Informe o novo nome")
                email = st.text_input("Informe o novo e-mail")
                fone = st.text_input("Informe o novo fone")
                senha = st.text_input("Informe a nova senha")
                if st.button("Mudar dados"):
                    View.editar_perfil(id, nome, email, fone, senha)
                    st.success("Dados do usuario atualizados com sucesso")
                    time.sleep(2)
                    st.rerun()