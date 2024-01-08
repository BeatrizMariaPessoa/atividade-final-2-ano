import streamlit as st
import json
from models.modelo import Modelo

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
    def set_habitantes(self, habitantes):
        if habitantes == "":
            raise ValueError("Preencha o número de habitantes")
        elif habitantes <= 0:
            raise ValueError("O número de habitantes deve ser maior que 0")
        else:
            self.__habitantes = habitantes
    def set_tamanho(self, tamanho):
        if tamanho == "":
            raise ValueError("Preencha o tamanho do país")
        elif tamanho <= 0:
            raise ValueError("O tamanho do país deve ser maior que 0")
        else:
            self.__tamanho = tamanho
    def set_moeda(self,moeda):
        if moeda == '':
            raise ValueError("Preencha qual o nome da moeda")
        else: self.__moeda = moeda
    def set_idioma(self, idioma):
        if idioma == '':
            raise ValueError("Preencha qual o idioma do país")
        else: self.__idioma = idioma
    def set_fuso_horario(self, fuso_horario):
        if fuso_horario == '':
            raise ValueError("Preencha qual o fuso horário do país")
        else: self.__fuso_horario = fuso_horario
    def set_capital(self,capital):
        if capital == '':
            raise ValueError("Preencha qual a capital do país")
        else: self.__capital = capital
    
    def get_id(self):return self.__id
    def get_nome(self):return self.__nome
    def get_habitantes(self):return self.__habitantes
    def get_tamanho(self):return self.__tamanho
    def get_moeda(self):return self.__moeda
    def get_idioma(self):return self.__idioma
    def get_fuso_horario(self):return self.__fuso_horario
    def get_capital(self):return self.__capital

    def __str__(self):
        return f"Id:{self.__id} - Nome:{self.__nome} - Habitantes:{self.__habitantes:.0f} - Tamanho:{self.__tamanho:.0f} - Moeda:{self.__moeda} - Idioma:{self.__idioma} - Fuso-Hoário{self.__fuso_horario:.0f} - Capital:{self.__capital}"
    
class NPais(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("paises.json", mode="r") as arquivo:
                paises_json = json.load(arquivo)
                for obj in paises_json:
                    aux = Pais(obj["_Pais__id"], obj["_Pais__nome"], obj["_Pais__habitantes"], obj["_Pais__tamanho"], obj["_Pais__moeda"], obj["_Pais__idioma"], obj["_Pais__fuso_horario"], obj["_Pais__capital"])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("paises.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)
