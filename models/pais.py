import streamlit as st
import json

class Pais:
    def __init__(self, id, nome, habitantes, tamanho, moeda, idioma, fuso_horario, capital):
        self.__id = id
        self.__nome = nome
        self.__habitantes = habitantes
        self.__tamanho = tamanho
        self.__moeda = moeda
        self.__idioma = idioma
        self.__fuso_horario = fuso_horario
        self.__capital = capital

    def set_id(self, id): self.__id = id
    def set_nome(self,nome):
        if nome == '':
            raise ValueError("Preencha qual o nome do país")
        else: self.__nome = nome
        return nome
    def set_habitantes(self, habitantes):
        if habitantes == "":
            raise ValueError("Preencha o número de habitantes")
        elif habitantes <= 0:
            raise ValueError("O número de habitantes deve ser maior que 0")
        else:
            self.__habitantes = habitantes
            return self.__habitantes
    def set_tamanho(self, tamanho):
        if tamanho == "":
            raise ValueError("Preencha o tamanho do país")
        elif tamanho <= 0:
            raise ValueError("O tamanho do país deve ser maior que 0")
        else:
            self.__tamanho = tamanho
            return self.__tamanho
    def set_moeda(self,moeda):
        if moeda == '':
            raise ValueError("Preencha qual o nome da moeda")
        else: self.__moeda = moeda
        return moeda
    def set_idioma(self, idioma):
        if idioma == '':
            raise ValueError("Preencha qual o idioma do país")
        else: self.__idioma = idioma
        return self.__idioma
    def set_fuso_horario(self, fuso_horario):
        if fuso_horario == '':
            raise ValueError("Preencha qual o fuso horário do país")
        else: self.__fuso_horario = fuso_horario
        return self.__fuso_horario
    def set_capital(self,capital):
        if capital == '':
            raise ValueError("Preencha qual a capital do país")
        else: self.__capital = capital
        return capital
    
    def get_id(self):return self.__id
    def get_nome(self):return self.__nome
    def get_habitantes(self):return self.__habitantes
    def get_tamanho(self):return self.__tamanho
    def get_moeda(self):return self.__moeda
    def get_idioma(self):return self.__idioma
    def get_fuso_horario(self):return self.__fuso_horario
    def get_capital(self):return self.__capital

    def __str__(self):
        return f"id:{self.__id} - Nome:{self.__nome} - Habitantes:{self.__habitantes} - Tamanho:{self.__tamanho} - Moeda:{self.__moeda} - Idioma:{self.__idioma} - Fuso horário:{self.__fuso_horario} - Capital:{self.__capital}"
    
class NPais:
    _paises = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__paises:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__paises.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__paises

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__paises:
            if obj.get_id() == id: return obj
        return None
    
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            aux.set_nome(obj.get_nome())
            aux.set_habitantes(obj.get_habitantes())
            aux.set_tamanho(obj.get_tamanho())
            aux.set_moeda(obj.get_moeda())
            aux.set_idioma(obj.get_idioma())
            aux.set_capital(obj.get_capital())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__paises.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__cidades = []
        try:
            with open("paises.json", mode="r") as arquivo:
                cidades_json = json.load(arquivo)
                for obj in paises_json:
                    aux = Pais(obj["PaisId"], obj["_Paisnome"], obj["_Paishabitantes"], obj["_Paistamanho"], obj["_Paismoeda"], obj["_Paisidioma"], obj["_Paisfuso_horario"], obj["_Paiscapital"])
                    cls.__paises.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("paises.json", mode="w") as arquivo:
            json.dump(cls.__paises, arquivo, default=vars)