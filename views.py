from models.cidade import Cidade,NCidade
from models.estado import Estado,NEstado
from models.pais import Pais,NPais
from models.usuario import Usuario,NUsuario
import datetime
import streamlit as st

class View:
    def usuario_inserir(nome, email, fone, senha):
        usuario = Usuario(0, nome, email, fone, senha)
        NUsuario.inserir(usuario)

    def usuario_listar():
        return NUsuario.listar()
    
    def usuario_listar_id():
        return NUsuario.listar_id()
    
    def usuario_atualizar(id, nome, email, fone, senha):
        usuario = Usuario(id, nome, email, fone, senha)
        NUsuario.atualizar(usuario)

    def usuario_excluir(id):
        usuario = Usuario(id,"", "", "", "")
        NUsuario.excluir(usuario)

    def usuario_admin():
        if len(View.usuario_listar()) == 0:
            View.usuario_inserir("admin", "admin@g", "0000", "admin")


    def usuario_login(email, senha):
        lista = View.usuario_listar()


        for usuario in lista:
            if usuario.get_email() == email and usuario.get_senha() == senha:
             
                return usuario
        return None
    
    def cidade_inserir(id_estado, nome, habitantes, tamanho):
        cidade = Cidade(0, id_estado, nome, habitantes, tamanho)
        NCidade.inserir(cidade)
    
    def cidade_listar():
        return NCidade.listar()
    
    def cidade_listar_id():
        return NCidade.listar_id()
    
    def cidade_atualizar(id, id_estado, nome, habitantes, tamanho):
        cidade = Cidade(id, id_estado, nome, habitantes, tamanho)
        NCidade.atualizar(cidade)

    def cidade_escluir(id):
        cidade = Cidade(id, "", "", "", "")
        NCidade.excluir(cidade)
     
    def estado_inserir(id, id_pais, nome, habitantes, tamanho, capital, municipios):
        estado = Estado(0, id_pais, nome, habitantes, tamanho, capital, municipios)
        NEstado.inserir(estado)

    def estado_listar():
        return NEstado.listar()
    
    def estado_listar_id():
        return NEstado.listar_id()
    
    def estado_atualizar(id, id_pais, nome, habitantes, tamanho, capital, municipios):
        estado = Estado(id, id_pais, nome, habitantes, tamanho, capital, municipios)
        NEstado.atualizar(estado)

    def estado_escluir(id):
        estado = Estado(id, "", "", "", "", "", "")
        NEstado.excluir(estado)

    def pais_inserir(id, nome, habitantes, tamanho, moeda, idioma, fuso_horario, capital):
        pais = Pais(0, nome, habitantes, tamanho, moeda, idioma, fuso_horario, capital)
        NPais.inserir(pais)
    
    def pais_listar():
        return NPais.listar()
    
    def pais_listar_id():
        return NPais.listar_id()
    
    def pais_atualizar(id, nome, habitantes, tamanho, moeda, idioma, fuso_horario, capital):
        pais = Pais(id, nome, habitantes, tamanho, moeda, idioma, fuso_horario, capital)
        NPais.atualizar(pais)

    def pais_excluir(id):
        pais = Pais(id, "", "", "", "", "", "", "")
        NPais.excluir(pais)

    def comparar_tamanho(tamanho1, nome1, nome2, tamanho2):
        if tamanho1 > tamanho2:
            return f'A opção com maior tamanho é {nome1} e seu tamanho é {tamanho1:.0f} km²'
        elif tamanho1 < tamanho2:
            return f'A opção com maior tamanho é {nome2} e seu tamanho é {tamanho2:.0f} km²'
        else:
            return "Os valores são iguais."
    
    def comparar_habitantes(hab1,hab2, nome1, nome2):
        if hab1 > hab2:
            return f'A opção com maior população é {nome1} e seu número é de {hab1:.0f} de habitantes'
        elif hab1 < hab2:
            return f'A opção com maior população é {nome2} e seu número é de {hab2:.0f} de habitantes'
        else: return "Os valores são iguais"

    def editar_perfil(id, nome, email, fone, senha):
        NUsuario.atualizar(Usuario(id, nome, email, fone, senha))

    def listar_estados(id_pais):
        estados_do_pais = []
        estados = View.estado_listar
        for obj in estados:
            if obj.get_id_pais() == id_pais: 
                estados_do_pais.append(obj)
        return estados_do_pais

    def listar_cidades(id_estado):
        cidades_do_estado = []
        cidades = View.cidade_listar
        for obj in cidades:
            if obj.get_id_estado() == id_estado:
                cidades_do_estado.append(obj)
        return cidades_do_estado
    
