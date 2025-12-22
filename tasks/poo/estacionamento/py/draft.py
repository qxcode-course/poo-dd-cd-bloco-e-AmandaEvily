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
    
class Moto(Veiculo):
    def __init__(self, id_veiculo):
        super().__init__(id_veiculo, "Moto")

    def calcular_valor(self, hora_saida):
        diferença = hora_saida - self.entrada
        minutos = diferenca.total_seconds() / 60
        valor = minutos / 20
        return valor
    
class Carro(Veiculo):
    def __init__(self, id_veiculo):
        super().__init__(id_veiculo, "Carro")

    def calcular_valor(self, hora_saida):
        diferenca = hora_saida - self.entrada
        minutos = diferenca.total_seconds() / 60
        valor = minutos / 10
        if valor < 5.00:
            return 5.00
        return valor
    
class SistemaEstacionamento:
    def __init__(self):
        self.veiculos_estacionados = {}

    def registrar_entrada(self, tipo, id_veiculo):
        if id_veiculo in self.veiculos_estacionados:
            print(f"Erro: O veículo com ID {id_veiculo} já está no estacionamento.")
            return
        
        veiculo = None
        tipo = tipo.lower()

        if tipo == "bicicleta" or tipo =="bike":
            veiculo = Bicicleta(id_veiculo)
        elif tipo == "moto":
            veiculo = Moto(id_veiculo)
        elif tipo == "carro":
            veiculo = Carro(id_veiculo)
        else:
            print("Tipo de veículo inválido.")

        self.veiculos_estacionados[id_veiculo] = veiculo
        print(f"Entrada registrada: {veiculo.to_string()}")

    def registrar_saida(self, id_veiculo):
        if id_veiculo not in self.veiculos_estacionados: 
            print(f"Erro: Veículo com ID {id_veiculo} não encontrado.")
            return
        
        veiculo = self.veiculos_estacionados[id_veiculo]
        hora_saida = datetime.now()

        valor_a_pagar = veiculo.calcular_valor(hora_saida)

        def self.veiculos_estacionados[id_veiculo]

        tempo_permanencia = hora saida - veiculo.entrada
        minutos_totais = int(tempo_permanencia.total_seconds() / 60)

        



