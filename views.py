from models.cidade import Cidade,NCidade
from models.estado import Estado,NEstado
from models.pais import Pais,NPais
from models.usuario import Usuario,NUsuario
import datetime

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
        for usuario in View.usuario_listar():
            if usuario.get_nome() == "admin": return
        View.usuario_inserir("admin", "admin", "0000", "admin")

    def usuario_login(email, senha):
        for usuario in View.usuario_listar():
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
     
    def estado_inserir(id_pais, nome, habitantes, tamanho, capital, municipios):
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

    def comparar_tamanho(tamanho1, tamanho2):
        if tamanho1 > tamanho2:
            return tamanho1
        elif tamanho1 < tamanho2:
            return tamanho2
        else:
            return "Os valores são iguais."
    
    def comparar_habitantes(hab1,hab2):
        if hab1 > hab2:
            return hab1
        elif hab1 < hab2:
            return hab2
        else: return "Os valores são iguais"




    
