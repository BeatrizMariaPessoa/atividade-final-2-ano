import streamlit as st
from templates.cadastroUI import Cadastrar_seUI
from templates.editar_perfilUI import EditarPerfilUI
from templates.loguinUI import LoginUI
from templates.comparar_paisesUI import CompararPisesUI
from templates.comparar_estadosUI import CompararEstadosUI
from templates.comparar_cidadesUI import CompararCidadesUI
from templates.buscasUI import BuscasUI
from templates.editar_infos_geraisUI import EditarInfosUI
from templates.ManterCidadeUI import ManterCidadeUI
from templates.ManterEstadoUI import ManterEstadoUI
from templates.ManterPaisUI import ManterPaisUI
from templates.abrircontaUI import AbrirContaUI


class IndexUI:
        def menu_visitante():
                op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
                if op == "Login": LoginUI.main()
                if op == "Abrir Conta": AbrirContaUI.main() 
                
        def menu_admin():
                op = st.sidebar.selectbox("Menu", ["ManterUserUI", "ManterPaisUI", "ManterEstadoUI", "ManterCidadeUI", "Editar Perfil", "EditarInformacoes",])
                if op == "ManterPaisUI": ManterPaisUI.main()
                if op == "ManterEstadoUI": ManterEstadoUI.main()
                if op == "ManterCidadeUI": ManterCidadeUI.main()
                if op == "Editar Perfil": EditarPerfilUI.main()
                if op == "EditarInformacoes": EditarInfosUI.main()

        def menu_usuario():
                op = st.sidebar.selectbox("Menu", ["Editar Perfil", "Buscas", "Comparar Paises", "Comparar Estados", "Comparar Cidades"])
        

        def não_logado():
                op = st.sidebar.selectbox("Menu", ["Cadastre-Se","Loguin","ManterUserUI",
        "ManterPaisUI","ManterEstadoUI","ManterCidadeUI","Editar Perfil","Buscas"
        ,"Comparar Paises", "Comparar Estados", "Comparar Cidades", "EditarInformacoes"])
                if op == "Cadastre-Se": Cadastrar_seUI.main()
                if op == "Editar Perfil": EditarPerfilUI.main()
                if op == "Loguin": LoginUI.main()
                if op == "Comparar Paises": CompararPisesUI.main()
                if op == "Comparar Estados": CompararEstadosUI.main()
                if op == "Comparar Cidades": CompararCidadesUI.main()
                if op == "Buscas": BuscasUI.main()
                if op == "EditarInformacoes": EditarInfosUI.main()
                if op == "ManterPaisUI": ManterPaisUI.main()
                if op == "ManterEstadoUI": ManterEstadoUI.main()
                if op == "ManterCidadeUI": ManterCidadeUI.main()
        op = "Loguin"

IndexUI.não_logado()
