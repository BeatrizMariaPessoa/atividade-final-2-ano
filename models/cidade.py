class Cidade:
    def __init__(self, id, id_estado, id_pais, nome, habitantes, tamanho):
        self.__id = id
        self.__id_estado = id_estado
        self.__id_pais = id_pais
        self.__nome = nome
        self.__habitantes = habitantes
        self.__tamanho = tamanho

    def get_id(self): return self.__id 
    def get_id_estado(self): self.__id_estado
    def get_id_pais(self): return self.__id_pais
    def get_nome(self): return self.__nome
    def get_habitantes(self): return self.__habitantes 
    def get_tamanho(self): return self.__tamanho 
    
    def set_id(self, id): 
        self.__id = id 

    def set_id_estado(self, id_estado): 
        self.__id_estado = id_estado

    def set_id_pais(self, id_pais): 
        self.__id_pais = id_pais

    def set_nome(self,nome): 
        self.__nome = nome

    def set_habitantes(self, habitantes):
        self.__habitantes = habitantes

    def set_tamanho(self, tamanho):
        self.__tamanho = tamanho

    def __str__(self):
        return f"Id: {self.__id} - Pais: {self.__id_estado} - Estado: {self.__id_estado} - nome: {self.__nome} - Hab: {self.__habitantes} - tamanho: {self.__tamanho}"

class NCliente:
    @classmethod