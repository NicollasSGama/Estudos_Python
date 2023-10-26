import flet as ft


def main(page: ft.Page):
    def eventoMensagem(e):
        texto = f'Nome:{input_name.value} Senha: {input_pass.value}'
        mensagem.value = texto
        page.update()

    page.title = 'Login'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    title = ft.Text('Login')
    icon_user = ft.Icon(ft.icons.BOY)
    icon_pass = ft.Icon(ft.icons.PASSWORD)
    input_name = ft.TextField(label='Nome')
    input_pass = ft.TextField(label='Senha')
    btn_enter = ft.ElevatedButton(text='Entrar', on_click=eventoMensagem)
    mensagem = ft.Text(value='')


    line_one = ft.Row(controls=[title],
                      alignment=ft.MainAxisAlignment.CENTER)
    line_two = ft.Row(controls=[icon_user, input_name],
                      alignment=ft.MainAxisAlignment.CENTER)
    line_three = ft.Row(controls=[icon_pass, input_pass],
                        alignment=ft.MainAxisAlignment.CENTER)
    line_four = ft.Row(controls=[btn_enter],
                       alignment=ft.MainAxisAlignment.CENTER)
    line_five = ft.Row(controls=[mensagem],
                       alignment=ft.MainAxisAlignment.CENTER)
    column = ft.Column(controls=[line_one, line_two, line_three, line_four, line_five])

    page.add(column)
    page.update()


ft.app(target=main)
