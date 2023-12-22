import streamlit as st

class CompararCidadesUI:
    def main():
        st.header("Comparar dados")
        CompararCidadesUI.comparar_cidadesUI()
    
    def comparar_cidadesUI():
        opcao1_pais = st.selectbox('Escolha o primeiro país',('Bolivia','Brasil','China','Opção genérica'))
        opcao1_es = st.selectbox('Escolha o primeiro estado',('op1','op2','op3'))
        opacao1_cid = st.selectbox('Escolha a primeira cidade',('op1','op2','op3'))

        opcao2_pais = st.selectbox('Escolha o segundo país',('Bolivia','Brasil','China','Opção genérica'))
        opcao2_es = st.selectbox('Escolha o segundo estado',('op1','op2','op3'))
        opacao2_cid = st.selectbox('Escolha a segunda cidade',('op1','op2','op3'))
        st.write("Quem possui maiores atributos e a diferença entre o primeiro e o segundo")

        