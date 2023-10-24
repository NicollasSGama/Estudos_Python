# listas é um agrupamento de dados heterogêneos
# podendo conter, portanto, tuplas, outras listas, string etc.

l = [[1, 2], 'a', (3, 4), 5]

# Há nativamente no Python, um método de trabalhar com dados homogêneos e economizar memória

from array import array

a = array('i', [1, 2, 3, 4, 5, 6])

print(a.typecode)  # 'i'
print(a.itemsize)  # 4 bytes - tamanho do dado que pode entrar


# O que quer dizer array
# Array com 1 dimensão
vetor = [1, 2, 3, 4, 5]

# Array com 2 dimensões
matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [1, 2, 3, 4, 5]
]