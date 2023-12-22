import json
from models.modelo import Modelo

class Estado:
    def __init__(self, id, id_pais, nome, habitantes, tamanho, capital, municipios):
        self.__id = id
        self.__id_pais = id_pais
        self.__nome = nome
        self.__habitantes = habitantes
        self.__tamanho = tamanho
        self.__capital = capital
        self.__municipios = municipios

    def get_id(self): return self.__id
    def get_id_pais(self): self.__id_pais
    def get_nome(self): return self.__nome
    def get_habitantes(self): return self.__habitantes 
    def get_tamanho(self): return self.__tamanho
    def get_capital(self): return self.__capital
    def get_municipios(self): return self.__municipios
    
    def set_id(self, id): 
        self.__id = id 

    def set_id_pais(self, id_pais):
        if type(id_pais) == int:
            self.__id_pais = id_pais
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

    def set_capital(self, capital):
        if capital != '':
            self.__capital = capital
        else: raise ValueError("Escolha um nome")

    def set_municipios(self, municipios):
        if type(municipios) == int:
            self.__municipios = municipios
        else: raise ValueError()

    def __str__(self):
        return f"Id: {self.__id} - País: {self.__id_pais} - Nome: {self.__nome} - Hab: {self.__habitantes} - Tamanho: {self.__tamanho} - Capital: {self.__capital} - Municipios: {self.__municipios}"

class NEstado(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Estados.json", mode="r") as arquivo:
                estados_json = json.load(arquivo)
                for obj in estados_json:
                    aux = Estado(obj["_Estado__id"], obj["_Estado__id_pais"], obj["_Estado__nome"], obj["_Estado__habitantes"], obj["_Estado__tamanho"], obj["_Estado__capital"], obj["_Estado__municipios"])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Estados.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)




# class NEstado:
#     __estados = []
#     @classmethod
#     def inserir(cls, obj):
#         cls.abrir()
#         id = 0
#         for aux in cls.__estados:
#             if aux.get_id() > id: id = aux.get_id()
#         obj.set_id(id + 1)
#         cls.__estados.append(obj)
#         cls.salvar()
    
#     @classmethod
#     def listar(cls):
#         cls.abrir()
#         return cls.__estados

#     @classmethod
#     def listar_id(cls, id):
#         cls.abrir()
#         for obj in cls.__estados:
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
#             aux.set_id_pais(obj.get_id_pais())
#             aux.set_municipios(obj.get_municipios())
#             aux.set_capital(obj.get_capital())
#             cls.salvar()

#     @classmethod
#     def excluir(cls, obj):
#         cls.abrir()
#         aux = cls.listar_id(obj.get_id())
#         if aux is not None:
#             cls.__estados.remove(aux)
#             cls.salvar()

#     @classmethod
#     def abrir(cls):
#         cls.__estados = []
#         try:
#             with open("Estados.json", mode="r") as arquivo:
#                 estados_json = json.load(arquivo)
#                 for obj in estados_json:
#                     aux = Estado(obj["_Estado__id"], obj["_Estado__id_pais"], obj["_Estado__nome"], obj["_Estado__habitantes"], obj["_Estado__tamanho"], obj["_Estado__capital"], obj["_Estado__municipios"])
#                     cls.__estados.append(aux)
#         except FileNotFoundError:
#             pass

#     @classmethod
#     def salvar(cls):
#         with open("Estados.json", mode="w") as arquivo:
#             json.dump(cls.__estados, arquivo, default=vars)