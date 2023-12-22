import streamlit as st
import json
from models.modelo import Modelo

class Usuario:
    def __init__(self, id, nome, email, fone, senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__senha = senha

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha

    def set_id(self, id): self.__id == id
    def set_nome(self, nome): 
        if nome == '':
            raise ValueError("Preencha o nome")
        else: self.__nome = nome
        return self.__nome
    def set_email(self, email): 
        if email == '':
            raise ValueError("Preencha o e-mail")
        else: self.__email = email
        return self.__email
    def set_fone(self, fone): 
        if fone == '':
            raise ValueError("Preencha o telefone")
        else: self.__fone = fone
        return self.__fone
    def set_senha(self, senha): 
        if senha == '':
            raise ValueError("Preencha a senha")
        else: self.__senha = senha
        return self.__senha
    
    def __str__(self):
        return f"Id:{self.__id} - Nome:{self.__nome} - E-mail{self.__email} - Telefone:{self.__fone}"


class NUsuario(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("usuarios.json", mode="r") as arquivo:
                usuarios_json = json.load(arquivo)
                for obj in usuarios_json:
                    aux = Usuario(obj["_Usuário__id"], 
                                obj["_Usuário__nome"], 
                                obj["_Usuário__email"],
                                obj["_Usuário__fone"],
                                obj["_Usuário__senha"])
            cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("usuarios.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)




# class NUsuario:
#     _usuarios = []

#     @classmethod
#     def inserir(cls,obj):
#         cls.abrir()
#         id = 0
#         for aux in cls.__usuarios:
#             if aux.get_id() > id: id = aux.get_id()
#         obj.set_id(id + 1)
#         cls.__clientes.append(obj)
#         cls.salvar()

#     @classmethod
#     def listar(cls):
#         cls.abrir
#         return cls.__usuarios
    
#     @classmethod
#     def listar_id(cls, id):
#         cls.abrir()
#         for obj in cls.__usuarios:
#             if obj.get_id() == id: return obj
#         return None
    
#     @classmethod
#     def atualizar(cls, obj):
#         cls.abrir()
#         aux = cls.listar_id(obj.get_id())
#         if aux is not None:
#             aux.set_nome(obj.get_nome())
#             aux.set_email(obj.get_email())
#             aux.set_fone(obj.get_fone())
#             aux.set_senha(obj.get_senha())
#             cls.salvar()

#     @classmethod
#     def excluir(cls, obj):
#         cls.abrir()
#         aux = cls.listar_id(obj.get_id())
#         if aux is not None:
#             cls.__usuarios.remove(aux)
#             cls.salvar()

#     @classmethod
#     def abrir(cls):
#         cls.__usuarios = []
#         try:
#             with open("usuarios.json", mode="r") as arquivo:
#                 usuarios_json = json.load(arquivo)
#                 for obj in usuarios_json:
#                     aux = Usuario(obj["_Usuário__id"], 
#                                 obj["_Usuário__nome"], 
#                                 obj["_Usuário__email"],
#                                 obj["_Usuário__fone"],
#                                 obj["_Usuário__senha"])
#             cls.__usuarios.append(aux)
#         except FileNotFoundError:
#             pass

#     @classmethod
#     def salvar(cls):
#         with open("usuarios.json", mode="w") as arquivo:
#             json.dump(cls.__usuarios, arquivo, default=vars)