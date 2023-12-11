import streamlit as st
import time 

class EditarPerfilUI:
    def main():
        st.header("Editar perfil")
        EditarPerfilUI.editar_perfil()
    
    def editar_perfil():
        st.text_input("Insira o novo e-mail")
        st.text_input("Insira o novo telefone")
        st.text_input("Insira a nova senha")
        if st.button("Editar"):
            st.success('Perfil editado com sucesso!')
            time.sleep(2)
            st.rerun()

EditarPerfilUI.main()