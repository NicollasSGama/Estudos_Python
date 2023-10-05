from PySimpleGUI import (
    Text, Input, Window,
    WIN_CLOSED, Button,
    HSeparator, Table,
    Frame, Column, theme,
    Image
)

tipo = [
    [
        'Conta Poupança'
    ],

    [
        'Conta Corrente'
    ]
]
def janela_cliente():
    layout_cliente = [
        [
            Text(text='Conta'),
            Input(key='-ID-'),
            Button(button_text='CONECTAR')
        ],

        [
            Text(text='Deposito'),
            Input(key='-DEPOSITAR-'),
            Button(button_text='DEPOSITAR')
        ],

        [
            Text(text='Saque'),
            Input(key='-SAQUE-'),
            Button(button_text='SAQUE')
        ],

        [
            HSeparator()
        ],

        [
            Text('Saldo'),
            Input(key='-SALDO-',
                  readonly=True)
        ]
    ]

    layout = [
        [
            Frame(title='CONTA',
                  layout=layout_cliente)
        ]
    ]

    return Window(title='CONTA',
                  layout=layout)


janela = janela_cliente()
# janela.read()

def janela_conta():
    pass