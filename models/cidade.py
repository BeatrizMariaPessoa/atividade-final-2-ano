import json
from models.modelo import Modelo

class Cidade:
    def __init__(self, id, id_estado, nome, habitantes, tamanho):
        self.__id = id
        self.__id_estado = id_estado
        self.__nome = nome
        self.__habitantes = habitantes
        self.__tamanho = tamanho

    def get_id(self): return self.__id 
    def get_id_estado(self): return self.__id_estado
    def get_nome(self): return self.__nome
    def get_habitantes(self): return self.__habitantes 
    def get_tamanho(self): return self.__tamanho 
    
    def set_id(self, id): 
        self.__id = id 

    def set_id_estado(self, id_estado):
        if type(id_estado) == int:
            self.__id_estado = id_estado
        else: raise ValueError()

    def set_nome(self, nome):
        if nome != '':
            self.__nome = nome
        else: raise ValueError("Escolha um nome")

    def set_habitantes(self, habitantes):
        if habitantes < 0:
            raise ValueError("Valor inválido")
        else:
            self.__habitantes = habitantes

    def set_tamanho(self, tamanho):
        if tamanho <= 0:
            raise ValueError("Tamanho de território inválido")
        else:
            self.__tamanho = tamanho

    def __str__(self):
        return f"Id:{self.__id} - Estado:{self.__id_estado} - Nome:{self.__nome} - Hab:{self.__habitantes} - Tamanho:{self.__tamanho}"

class NCidade(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("cidades.json", mode="r") as arquivo:
                cidades_json = json.load(arquivo)
                for obj in cidades_json:
                    aux = Cidade(obj["_Cidade__id"], obj["_Cidade__id_estado"], obj["_Cidade__nome"], obj["_Cidade__habitantes"], obj["_Cidade__tamanho"])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("cidades.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)






# class NCidade:
#     __cidades = []
#     @classmethod
#     def inserir(cls, obj):
#         cls.abrir()
#         id = 0
#         for aux in cls.__cidades:
#             if aux.get_id() > id: id = aux.get_id()
#         obj.set_id(id + 1)
#         cls.__cidades.append(obj)
#         cls.salvar()
    
#     @classmethod
#     def listar(cls):
#         cls.abrir()
#         return cls.__cidades

#     @classmethod
#     def listar_id(cls, id):
#         cls.abrir()
#         for obj in cls.__cidades:
#             if obj.get_id() == id: return obj
#         return None
    
#     @classmethod
#     def atualizar(cls, obj):
#         cls.abrir()
#         aux = cls.listar_id(obj.get_id())
#         if aux is not None:
#             aux.set_nome(obj.get_nome())
#             aux.set_habitantes(obj.get_habitantes())
#             aux.set_tamanho(obj.get_tamanho())
#             aux.set_id_estado(obj.get_id_estado())
#             cls.salvar()

#     @classmethod
#     def excluir(cls, obj):
#         cls.abrir()
#         aux = cls.listar_id(obj.get_id())
#         if aux is not None:
#             cls.__cidades.remove(aux)
#             cls.salvar()

#     @classmethod
#     def abrir(cls):
#         cls.__cidades = []
#         try:
#             with open("cidades.json", mode="r") as arquivo:
#                 cidades_json = json.load(arquivo)
#                 for obj in cidades_json:
#                     aux = Cidade(obj["_Cidade__id"], obj["_Cidade__id_estado"], obj["_Cidade__nome"], obj["_Cidade__habitantes"], obj["_Cidade__tamanho"])
#                     cls.__cidades.append(aux)
#         except FileNotFoundError:
#             pass

#     @classmethod
#     def salvar(cls):
#         with open("cidades.json", mode="w") as arquivo:
#             json.dump(cls.__cidades, arquivo, default=vars)