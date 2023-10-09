from abc import ABC, abstractmethod


# class Pessoa:
#
#     def __init__(self, *, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         self.nomeClasse = self.__class__.__name__
#
#     def falar(self):
#         print(f"{self.nomeClasse} esta falando")
#
#
# class Aluno(Pessoa):
#     pass
#
#
# class Professor(Pessoa):
#     pass
#
#
# aluno = Aluno("Carlos", 34)
# professor = Professor("José", 55)
# print(aluno.nome)


class Conta(ABC):
    def __init__(self, valor: float, cliente: str):
        self.__saldo = valor  # Privar o parâmetro para que este só seja acessado por meio da classe
        self.cliente = cliente
        self.__status = True
        self.__id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def status(self):
        return self.__status

    def alterar_status(self, status: bool):
        self.__status = status

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float):
        self.__saldo -= valor

    def deposito(self, valor: float):
        if self.__status:
            self.__saldo += valor
        else:
            raise 'A conta não está ativa'  # Força a tratar a sub-rotina com um try quando for chamada

    @abstractmethod  # Força à classe que herdá-la a utilizar a função
    def saque(self, valor: int):
        pass


class Conta_Corrente(Conta):

    def __init__(self, valor: float, cliente: str, limite: float):
        super().__init__(valor, cliente)
        self.__limite = limite

    def saque(self, valor: float):
        if self.status:
            if isinstance(valor, (int, float)):
                if self.saldo >= valor:
                    self.saldo = valor
                elif self.saldo + self.__limite >= valor:
                    self.saldo = self.saldo - valor
                    self.__limite = self.__limite + self.saldo
                    print('Você está no limite')
                else:
                    raise 'Saldo não cobre o valor de saque'
            else:
                raise 'Digite um valor válido'
        else:
            raise 'A conta não está ativa'


class Conta_Poupaca(Conta):

    def saque(self, valor: float):
        if self.status:
            if self.saldo >= valor:
                self.saldo = valor
            else:
                raise 'Saldo não cobre o valor de saque'
        else:
            raise 'A conta não está ativa'


cp = Conta_Poupaca(valor=1500, cliente='Pedrinho')
cc = Conta_Corrente(valor=1400, cliente='Joselito', limite=1200)
print(f'Este é o saldo da conta R${cp.saldo}.')
cp.deposito(1000)
print(f'Este é o saldo da conta R${cp.saldo}.')
cp.saque(1999)
print(f'Este é o saldo da conta R${cp.saldo}.')
# print('*' * 30)
# print(cc.saldo)
# cc.deposito(1573)
# print(cc.saldo)
# cc.saque(4000)
# print(cc.saldo)


class Cliente:
    def __init__(self, nome: str, nascimento: str):
        self.nome = nome
        self.nascimento = nascimento
        self.__id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
