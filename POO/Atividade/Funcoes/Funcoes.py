from POO.Atividade.Telas.Tela import *

janela_login, janela_menu, janela_cliente, janela_busca, janela_animal = login(), None, None, None, None

while True:
    janela, eventos, valores = read_all_windows()
    match eventos:
        case WIN_CLOSED:
            break
    match janela:
        case janela_login:
            break
