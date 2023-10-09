# Crie uma aplicação que vai ter um classe do tipo Piloto e outra do tipo Carro
# Faça a Associação deles. Lembrando que queremos somente o nome de ambos
# E a classe carro tem um método chamado andar que mostra uma mensagem 'Estou dirigindo o carro{nome do carro}'

class Piloto:
    def __init__(self, nome):
        self.__nome = nome
        self.carro = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


class Carro:
    def __init__(self, modelo):
        self.__modelo = modelo

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    def __str__(self):
        return 'Estou dirigindo um {}'.format(self.__modelo)


piloto_1 = Piloto(nome='Pedro')
modelo_carro = Carro(modelo='Uno')
# ----------------------------------
piloto_1.carro = modelo_carro
print(piloto_1.carro)
