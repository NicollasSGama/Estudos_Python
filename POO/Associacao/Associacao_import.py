from POO.Associacao.Associacao import (
    Escritor, Ferramenta
)
escritor = Escritor('Pedro')
f1 = Ferramenta('Caneta')
f2 = Ferramenta('Computador')

escritor.ferramenta = f1

print(escritor.ferramenta.nome)



