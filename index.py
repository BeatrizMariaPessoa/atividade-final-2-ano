import streamlit as st
from templates.cadastroUI import Cadastrar_seUI
from templates.editar_perfilUI import EditarPerfilUI
from templates.loguinUI import LoginUI
from templates.comparar_paisesUI import CompararPaisesUI
from templates.comparar_estadosUI import CompararEstadosUI
from templates.comparar_cidadesUI import CompararCidadesUI
# from templates.buscasUI import BuscasUI
from templates.editar_infos_geraisUI import EditarInfosUI
from templates.ManterCidadeUI import ManterCidadeUI
from templates.ManterUserUI import ManterUsuarioUI
from templates.ManterEstadoUI import ManterEstadoUI
from templates.ManterPaisUI import ManterPaisUI
from templates.abrircontaUI import AbrirContaUI
from views import View


class IndexUI:
#         def menu_visitante():
#                 op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
#                 if op == "Login": LoginUI.main()
#                 if op == "Abrir Conta": AbrirContaUI.main() 
                
#         def menu_admin():
#                 op = st.sidebar.selectbox("Menu", ["ManterUsuarioUI", "ManterPaisUI", "ManterEstadoUI", "ManterCidadeUI", "Editar Perfil", "EditarInformacoes",])
#                 if op == "ManterPaisUI": ManterPaisUI.main()
#                 if op == "ManterEstadoUI": ManterEstadoUI.main()
#                 if op == "ManterCidadeUI": ManterCidadeUI.main()
#                 if op == "ManterUsuarioUI": ManterUsuarioUI.main()
#                 if op == "Editar Perfil": EditarPerfilUI.main()
#                 if op == "EditarInformacoes": EditarInfosUI.main()

#         def menu_usuario():
#                 op = st.sidebar.selectbox("Menu", ["Editar Perfil", "Comparar Paises", "Comparar Estados", "Comparar Cidades"])
#                 if op == "Editar Perfil": EditarPerfilUI.main()
#                 if op == "Comparar Paises": CompararPaisesUI.main()
#                 if op == "Comparar Estados": CompararEstadosUI.main()
#                 if op == "Comparar Cidades": CompararCidadesUI.main()
        
#         def btn_logout():
#                 if st.sidebar.button("Logout"):
#                         del st.session_state["usuario_id"]
#                         del st.session_state["usuario_nome"]
#                         st.rerun()

#         def sidebar():
#                 if "usuario_id" not in st.session_state:
#                         IndexUI.menu_visitante()   
#                 else:
#                         st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
#                         if st.session_state["usuario_nome"] == "admin": IndexUI.menu_admin()
#                         else: IndexUI.menu_usuario()
#                         IndexUI.btn_logout()  
#         def main():
#                 View.usuario_admin()
#                 IndexUI.sidebar()
# IndexUI.main()

        def não_logado():
                op = st.sidebar.selectbox("Menu", ["Cadastre-Se","Loguin","ManterUsuarioUI",
        "ManterPaisUI","ManterEstadoUI","ManterCidadeUI","Editar Perfil","Comparar Paises",
          "Comparar Estados", "Comparar Cidades", "EditarInformacoes"])
                if op == "Cadastre-Se": Cadastrar_seUI.main()
                if op == "Editar Perfil": EditarPerfilUI.main()
                if op == "Loguin": LoginUI.main()
                if op == "Comparar Paises": CompararPaisesUI.main()
                if op == "Comparar Estados": CompararEstadosUI.main()
                if op == "Comparar Cidades": CompararCidadesUI.main()
                if op == "EditarInformacoes": EditarInfosUI.main()
                if op == "ManterPaisUI": ManterPaisUI.main()
                if op == "ManterEstadoUI": ManterEstadoUI.main()
                if op == "ManterCidadeUI": ManterCidadeUI.main()
                if op == "ManterUsuarioUI": ManterUsuarioUI.main()
        op = "Loguin"

IndexUI.não_logado()
