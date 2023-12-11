import streamlit as st

class CompararEstadosUI:
    def main():
        st.header("Comparar dados")
        CompararEstadosUI.comparar_estadosUI()
    
    def comparar_estadosUI():
        opcao1_pais = st.selectbox('Escolha o primeiro país',('Bolivia','Brasil','China','Opção genérica'))
        opcao1_es = st.selectbox('Escolha o primeiro estado',('op1','op2','op3'))

        opcao2_pais = st.selectbox('Escolha o segundo país',('Bolivia','Brasil','China','Opção genérica'))
        opcao2_es = st.selectbox('Escolha o segundo estado',('op1','op2','op3'))
        st.write("Quem possui maiores atributos e a diferença entre o primeiro e o segundo")