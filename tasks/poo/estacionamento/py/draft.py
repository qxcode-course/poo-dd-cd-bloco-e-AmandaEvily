from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import math

class Veiculo(ABC):
    def __init__(self, id_veiculo, tipo):
        self.id = id_veiculo
        self.tipo = tipo
        self.entrada = datetime.now()

    @abstractmethod
    def calcular_valor(self, hora_saida):
        pass

    def to_string(self):
        data_formatada = self.entrada.strtime("%d/%m/%Y %H:%M:%S")
        return f"Tipo: {self.tipo} | ID: {self.id} | Entrada:{data_formatada}"
    
class Bicicleta(Veiculo):
    def __init__(self, id_veiculo):
        super().__init__(id_veiculo, "Bicicleta")

    def calcular_valor(self, hora_saida):
        return 3.00
    