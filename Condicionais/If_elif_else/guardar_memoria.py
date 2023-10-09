# Booleano
# --------
# em uma condicional, se o valor estiver gravado na memória, este será True
# se for número e este for igual a 0, será False
# se for número e este for menor ou maior que 0, será True
variavel = 0
if variavel:
    print(f'{variavel}: Dentro')
else:
    print(f'{variavel}: Fora')

variavel = 1
if variavel:
    print(f'{variavel}: Dentro')
else:
    print(f'{variavel}: Fora')

# String
# ------
# se em uma String estiver vazia "", esta será tida como False
texto = ''
if texto:
    print(f'{texto}: Dentro')
else:
    print(f'{texto}: Fora')

texto = 'algo'
if texto:
    print(f'{texto}: Dentro')
else:
    print(f'{texto}: Fora')

lista = [1, 2, 3, 4, 5, 6, 7]

valor = [x for x in lista if x % 2 == 0]  # comprehension

for x in lista:
    if x % 2 == 0:
        valor.append(x)

print(valor)

tuple_2 = ('Carro', 'Avião', 'Barco', 'Barco_1', 'Moto', 'Caminhão')
veiculo = [x for x in tuple_2 if 'Avião' in x]

for x in tuple_2:  # for x in range(len(tuple_2))  /  print(tuple_2[x])
    if 'Barco' in x:
        veiculo.append(x)

print(veiculo)
# -------------------
import timeit

# comprehension e generation
