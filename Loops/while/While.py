# numero = [0, 0, 0, 0, 0]
# x = 0
# while x < 5:
#     numero[x] = int(input('Número %d:' % (x + 1)))
#     x += 1
# while True:
#     escolhido = int(input('Qual posição você quer imprimir (0 para sair): '))
#     if escolhido == 0:
#         break
#     print('Você escolheu o número: %d' % (numero[escolhido - 1]))


# ------------
# Cópia lista
# ------------

# L = [1, 2, 3, 4, 5]
# V = L[:]
# V[0] = 6
# print(L)
# print(V)
# ------------
# Fazer um programa que leia duas listas e que gere uma terceira com os elementos de ambas
# ------------

lista_1 = list()
lista_2 = list()
lista_3 = list()
x = 0

while x < 5:
    elemento_1 = int(input('Digite o %d° número da 1° lista: ' % (x + 1)))
    lista_1.append(elemento_1)
    x += 1
    if x == 5:
        x = 0
        print('#' * 30)
        while x < 5:
            elemento_2 = int(input('Digite o %dº número da 2º lista: ' % (x + 1)))
            lista_2.append(elemento_2)
            x += 1

lista_3 = lista_1[:] + lista_2[:]

print(lista_3)
