class Animal:
    def __init__(self, nome, idade, cor, genero, especie, porte):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.genero = genero
        self.especie = especie
        self.porte = porte


class Cachorro(Animal):
    def __init__(self, patas, pelagem, raca, nome, idade, cor, genero, especie, porte):
        super().__init__(nome, idade, cor, genero, especie, porte)
        self.patas = patas
        self.pelagem = pelagem
        self.raca = raca


A = Animal('Bob', '3', 'preto', 'masculino', 'canis familiaris', 'grande')
print(A.nome)
B = Animal