from PySimpleGUI import (
    Text, Input, Button,
    Window, Frame, Push,
    HSeparator, Column,
    VSeparator, read_all_windows,
    WIN_CLOSED
)


# --------------------------------------------
# Tela Login
# --------------------------------------------

def login():
    layout_contato = [
        [
            Text('CPF')
        ],

        [
            Input(key='-CPF-')
        ],

        [
            Text('Senha')
        ],

        [
            Input(key='-SENHA-')
        ],

        [
            HSeparator()
        ],

        [
            Button('FECHAR',
                   key='-FECHAR-'),
            Push(),
            Button('ENTRAR',
                   key='-ENTRAR-')
        ]
    ]

    layout = [
        [
            Frame('LOGIN',
                  layout_contato)
        ]
    ]

    return Window('TELA_ENTRAR',
                  layout)


janela_login = login()
janela_login.read()

# --------------------------------------------
# Tela Menu
# --------------------------------------------
def menu():
    layout = [
        [
            Button('CADASTRAR CLIENTE')
        ],

        [
            Button('CADASTRAR ANIMAL ')
        ],
    ]

    layout = [
        [
            Frame('',
                  layout)
        ]
    ]
    return Window('CADASTRAR',
                  layout)


janela_menu = menu()
janela_menu.read()

# --------------------------------------------
# Tela Cliente
# --------------------------------------------

def tela_cliente():
    layout_cadastro = [
        [
            Text('Nome')
        ],

        [
            Input(key='-NOME-')
        ],

        [
            Text('CPF')
        ],

        [
            Input(key='-CPF-')
        ],

        [
            Text('Tel.')
        ],

        [
            Input(key='-TEL-')
        ],

        [
            HSeparator()
        ],

        [
            Button('VOLTAR'),
            Push(),
            Button('CADASTRAR')
        ]
    ]

    layout = [
        [
            Frame('CADASTRAR',
                  layout_cadastro)
        ]
    ]

    return Window('TELA_CLIENTE',
                  layout)


janela_cliente = tela_cliente()
janela_cliente.read()

# --------------------------------------------
# Tela Animal_Cliente
# --------------------------------------------

def tela_animal_cliente():
    layout_busca = [
        [
            Text('CPF')
        ],

        [
            Input(key='-CPF-')
        ],

        [
            HSeparator()
        ],

        [
            Button('VOLTAR'),
            Push(),
            Button('BUSCAR')
        ]
    ]

    layout = [
        [
            Frame('BUSCA',
                  layout_busca)
        ]
    ]

    return Window('TELA_BUSCA',
                  layout)


janela_busca = tela_animal_cliente()
janela_busca.read()

# --------------------------------------------
# Tela Animal
# --------------------------------------------

def tela_animal():
    layout_esquerda = [
        [
            Text('Nome')
        ],

        [
            Input(key='-NOME-')
        ],

        [
            Text('Idade')
        ],

        [
            Input(key='-IDADE-')
        ],

        [
            Text('Raça')
        ],

        [
            Input(key='-RACA-')
        ],

        [
            HSeparator()
        ],

        [
            Button('VOLTAR')
        ]
    ]

    layout_direita = [
        [
            Text('Espécie')
        ],

        [
            Input(key='-ESPECIE-')
        ],

        [
            Text('Cor')
        ],

        [
            Input(key='-COR-')
        ],

        [
            Text('Porte')
        ],

        [
            Input(key='-PORTE-')
        ],

        [
            HSeparator()
        ],

        [
            Push(),
            Button('CADASTRAR')
        ]
    ]

    layout_esquerda_direita = [
        [
            Column(layout_esquerda),
            VSeparator(),
            Column(layout_direita)
        ]
    ]

    layout = [
        [
            Frame('CADASTRAR',
                  layout_esquerda_direita)
        ]
    ]

    return Window('TELA_ANIMAL',
                  layout)


janela_animal = tela_animal()
janela_animal.read()

# janela_login, janela_menu, janela_cliente, janela_busca, janela_animal = login(), None, None, None, None
#
# while True:
#     janela, eventos, valores = read_all_windows()
#     match janela:
#         case janela_login:
#             break
