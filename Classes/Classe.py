# ---------------------------------------
# Atributo é aquilo que o tipo necessita como definição
# Método possíveis funções embutidas em um tipo de dado
# ---------------------------------------
class Gatinho:
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.mingual_com_fome = False
        self.mingual_andou = 0

    def miar(self):
        if self.mingual_com_fome:
            return 'MIAAAUUUUUUUUUU'
        return 'Miau, Miau'

    def andar(self):
        self.mingual_andou += 1
        self.mingual_com_fome = True
        return 'Mingau andando'

    @property  # é uma propriedade -- definida apartir de atributos
    # atributo dinâmico - definido em tempo de execução
    def velho(self):
        return True if self.idade > 3 else False

    @property
    def cansado(self):
        return True if self.mingual_andou > 5 else False


mingau = Gatinho('Mingau', 'preto', 2)


# print(mingau.nome)
# print(mingau.miar())
# print(mingau.andar())
# print(mingau.miar())

# print(mingau.velho)
# print(mingau.cansado)
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.cansado)
# ---------------------------------------
# geometria
# ---------------------------------------
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):  # dunder que representa uma classe. Posso utilizar diversas vezes
        return 'Ponto({}, {})'.format(self.x, self.y)


ponto_1 = Ponto(2, 2)
ponto_2 = Ponto(3, 5)
ponto_3 = Ponto(1, 9)
print(ponto_1)
print(ponto_2)
print(ponto_3)


class Linha:
    def __init__(self, p_1, p_2):
        self.ponto_1 = p_1
        self.ponto_2 = p_2

    def distancia_x(self):
        return self.ponto_1.x - self.ponto_2.x


linha_1 = Linha(ponto_1, ponto_3)
print(linha_1.distancia_x())
