from random import *

caracteres = '0123456789abcdABCD@#$%'

def gerar(qtde):
    senha = ''
    for n in range(qtde):
        senha += choice(caracteres)
    return senha

print(gerar(10))

