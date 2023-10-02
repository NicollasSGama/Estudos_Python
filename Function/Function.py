def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.

    least_difference(1, 5, -5)
    4"""
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print(least_difference(10, 12, 31))

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),  # Python allows trailing commas in argument lists. How nice is that?
)

help(least_difference)

print(1, 2, 3, sep='<')


def mult_by_five(x):
    return 5 * x


def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))


print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n',  # '\n' is the newline character - it starts a new line
)


def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5


print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

help(round)
print(round(3.14159, 2))


# def retornoDuasCasas(num):
#     """Retorna o número digitado mais duas casas decimais deste.
#     >>> retornoDuasCasas(3.14159)
#     3.14"""
#     return round(num, 2)
# print(retornoDuasCasas(25.2564896))
#
# help(retornoDuasCasas)

def return_num(num):
    """
    Retorna o número digitado de acordo com o ndigits:
        -> round(num, -1) retornará na base 10;
        -> round(num, -2) retornará na base 100;
        -> round(num, -3) retornará na base 1000;
        -> e assim por diante.
        --------
        Exemplos:
        --------
        -> print(round(338.424, -2))
           338.000
        -> print(round(2.166.000, -3))
           2.166.000
    """
    return round(num, -2)


print(return_num(222.12341234))
help(return_num)


# -------------------------------------------------------------
# Função nomeada
# -------------------------------------------------------------
def funcao_nomeada():
    return 'Oi'


# -------------------------------------------------------------
# Função anônima - função reservada
# -------------------------------------------------------------
anonima = lambda: 'Oi'


# -------------------------------------------------------------
# Função classe
# -------------------------------------------------------------
class FuncaoClasse:
    def __call__(self):  # Dunder call para chamar a função em classe.
        return 'Oi'  # Classe que emula uma função


# -------------------------------------------------------------
# Função anônima  - o máx. que é possível fazer com lambda
# -------------------------------------------------------------

anonima = lambda param: param + 2
anonima_plus = lambda param1, param2: param1 + param2


# -------------------------------------------------------------
# Função nomeada
# -------------------------------------------------------------

def soma_posicional(x, y):
    """
    x e y são parâmentros posicionais
    :param x:
    :param y:
    :return:
    """
    return x + y


soma_posicional(1, 2)


# -------------------------------------------------------------
# função nomeada(x=1, y=3): (x, y)::default(francês) na falta
# de alguma coisa use esse parâmentro
# -------------------------------------------------------------


def soma_nomeados(x=7, y=7):
    """
    x e y são parâmentros nomeados,
    ou seja,
    na falta de x ou y,
    o valor 7 será utilizado

    :param x:
    :param y:
    :return:
    """
    print(f'x:{x}, y:{y}')
    return x + y


soma_nomeados(x=1)


# -------------------------------------------------------------
# A partir do Python 3.6 o '*' pode ser utilizado como
# paramentro, que diz que tudo que estiver do '*' para atrás
# só poderá ser chamado de 'maneira nomeada'
# -------------------------------------------------------------
def soma_explicitamente_nomeados(*, x=7, y=7):
    """
    x e y são parâmentros nomeados,
    ou seja,
    na falta de x ou y,
    o valor 7 será utilizado

    :param x:
    :param y:
    :return:
    """
    print(f'x:{x}, y:{y}')
    return x + y


# soma_explicitamente_nomeados(1) # não é possível alterar pois é um paramentro posicional
soma_explicitamente_nomeados(x=1, y=2)  # é possível alterar pois é um paramentro nomeado


# -------------------------------------------------------------

def soma_explicitamente_nomeados_ordem(x=7, *, y=7):
    """
    x e y são parâmentros nomeados,
    ou seja,
    na falta de x ou y,
    o valor 7 será utilizado

    :param x:
    :param y:
    :return:
    """
    print(f'x:{x}, y:{y}')
    return x + y


# soma_explicitamente_nomeados_ordem(1, 1) # agora 'x' pode ser posicional, mas o y não
soma_explicitamente_nomeados_ordem(1, y=10)


# -------------------------------------------------------------
# No Python 3.8 Função explicitamente posicionais (x, y, /)
# -------------------------------------------------------------


def soma_explicitamente_posicionais(x, y, /):
    """
    x e y são parâmentros nomeados,
    ou seja,
    na falta de x ou y,
    o valor 7 será utilizado

    :param x:
    :param y:
    :return:
    """
    print(f'x:{x}, y:{y}')
    return x + y


# soma_explicitamente_posicionais(x=1, y=2) # aceita somente paramentros posicionais e não nomeados
soma_explicitamente_posicionais(1, 2)


# -------------------------------------------------------------
# Função que contêm todas as atribuições:
# -> '*': para restringir à nomeadas;
# -> '/': para restringir à posicionais.
# -------------------------------------------------------------
def soma_tudo(x, y, /, z, *, w):
    print(f'x:{x}, y:{y}, z:{z}, w:{w}')
    return sum((x, y, z, w))


soma_tudo(1, 1, 1, w=1)
# -------------------------------------------------------------
