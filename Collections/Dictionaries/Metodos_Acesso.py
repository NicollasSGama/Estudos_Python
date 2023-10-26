dicionario = {
    'string': 'Fusca',
    'booleano': True,
    'inteiro': 1234,
    'lista': ['string', 12e34, False]
}
# -------------------------------------------
# Métodos em dicionários
# -------------------------------------------
# Acesso
# ------
# .get() -- acessa o valor da chave
# ----------------
print(dicionario.get('string'))
# ------
# .keys() -- retorna uma lista com todas as
# chaves do dicionário
# ----------------
print(dicionario.keys())
dicionario['complexo']=4e32
print(dicionario.keys())
# ------
# .values() -- retorna uma lista com todos os
# valores do dicionário
# ----------------
print(dicionario.values())
dicionario['ano']=2023
print(dicionario.values())
# ------
# .items() -- retorna uma tupla com todos os
# valores e as respectivas chaves do dicionário
# ----------------
print(dicionario.items())
# -------------------------------------------
# Verificar se há a chave ou valor no dict
# -------------------------------------------
match dicionario:
    case _ if 'inteiro' in dicionario:
        print('Existe no dicionário')
    case _:
        print('Não existe no dicionário')