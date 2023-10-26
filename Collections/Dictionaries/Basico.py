# -------------------------------------------
# Método para guardar valores com chaves
# -------------------------------------------
comida_pais = {
    'italia': 'pizza',
    'portugal': 'bacalhau',
    'argentina': 'vinho'
}
print(comida_pais)
print('-'*50)
print(comida_pais['italia'])
# -------------------------------------------
# Característica do dicionário
# -------------------------------------------
# A chave só aloca um espaço para um valor.
# Não é possível pôr chaves duplicadas
# ----------------
comida_pais_2 = {
    'italia': 'pizza',
    'portugal': 'bacalhau',
    'argentina': 'vinho',
    'argentina': 'doce-leite'
}

print(comida_pais_2)
print('-'*50)
print(comida_pais_2['argentina'])
# ----------------
# Por meio do len() é possível contabilizar
# quantos itens há no dicionário
# ----------------
print(len(comida_pais_2))
# ----------------
# O dicionário suporta todo o tipo de dado
# e outras collections
# ----------------
dicionario = {
    'string': 'Fusca',
    'booleano': True,
    'inteiro': 1234,
    'lista': ['string', 12e34, False]
}
print(dicionario)
# -------------------------------------------
# Para construir um dicionário é necessário
# atribuir a função 'dict' antes dos valores
# e atribuir chaves a estes
# -------------------------------------------
dicionario_criacao = dict(nome='Pedro',
                          idade=32,
                          habilitado=False)
print(dicionario_criacao)


