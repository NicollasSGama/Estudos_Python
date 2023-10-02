class Pessoa:

    def __init__(self, *, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeClasse} esta falando")


class Aluno(Pessoa):
    pass


class Professor(Pessoa):
    pass


aluno = Aluno("Carlos", 34)
professor = Professor("José", 55)
print(aluno.nome)
