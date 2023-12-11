import streamlit as st

class CompararPisesUI:
    def main():
        st.header("Comparar dados")
        CompararPisesUI.comparar_pisesUI()
    
    def comparar_pisesUI():
        opcao1 = st.selectbox('Escolha o primeiro país',('Bolivia','Brasil','China','Opção genérica'),)
        opcao2 = st.selectbox('Escolha o segundo país',('Bolivia','Brasil','China','Opção genérica'))
        st.write("Quem possui maiores atributos e a diferença entre o primeiro e o segundo")
    
